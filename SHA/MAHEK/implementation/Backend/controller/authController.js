import crypto from "crypto";
import bcrypt from "bcryptjs";
import User from "../models/User.js";
import { setUser, generateHashPassword } from "../services/auth.js";
import { SendResetPwdEmail, SendVerificationCode, WelcomeEmail } from "../services/email.sender.js";

async function handleRegister (req, res) {
  try {
    const { username, email, password} = req.body;
    if (!username || !email || !password) {
      return res.status(400).json({ message: "All fields are Required" });
    }

    // Check if user already exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ message: "User already exists" });
    }

    const hashedPassword = await generateHashPassword(password);

    const verificationCode = Math.floor(100000 + Math.random() * 900000).toString();

    // Hash the code
    const hashedCode = crypto
    .createHash("sha256")
    .update(verificationCode)
    .digest("hex");

    await User.create({
    username,
    email,
    password: hashedPassword,
    isVerified: false,
    verificationCode: hashedCode,
    verificationCodeExpires: new Date(Date.now() + 10 * 60 * 1000)
    });

    SendVerificationCode(email, verificationCode);
    res.status(201).json({ message: "User registered successfully" });
  }
  catch (err) {
    console.error("user register error:", err);
    return res.status(400).json({ success: false, message: err.message });
  } 
}

async function handleLogin (req, res) {
  try {
    const userToken = req.cookies?.token;
    if(userToken) 
      return res.status(400).json({message:"You are already logged in, go to home page"});

    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ message: "Provide email and password" });
    }

    const user = await User.findOne({ email });  
    if (!user) {
      return res.status(401).json({ message: "Invalid email or password" });
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(401).json({ message: "Invalid email or password" });
    }

    if (!user.isVerified) {
      return res.status(401).json({ message: "Email not verified" });
    }

    const token = setUser(user);
    res.cookie("token", token, {
      httpOnly: true,
      sameSite: "none",
      secure: true,
      maxAge: 7 * 24 * 60 * 60 * 1000,
      path: "/",
    });

    return res.json({ message: "Login successful", token, user: { username: user.username, email: user.email } });
  }
  catch (err) {
    console.error("user login error:", err);
    return res.status(400).json({ success: false, message: err.message });
  }
};

async function handleLogout (req, res) {
  try {
    // Optionally, you could blacklist the JWT's jti via redis for logout, but most use short exp. Here, just clear cookie.
    res.clearCookie("token", { httpOnly: true, sameSite: "none", secure: true, path: "/" });
    return res.json({ message: "Logged out" });
  }
  catch (err) {
    console.error("user logout error:", err);
    return res.status(400).json({ success: false, message: err.message });
  }
};

async function verifyEmail(req, res) {
  try {
    const { email, code } = req.body;

    if (!email || !code) {
      return res.status(400).json({ message: "All fields are required" });
    }

    const user = await User.findOne({ email });
    if (!user) {
      return res.status(400).json({ message: "Invalid user" });
    }

    // Hash incoming code
    const hashedIncomingCode = crypto
      .createHash("sha256")
      .update(code)
      .digest("hex");

    // Compare + expiry check
    if (
      user.verificationCode !== hashedIncomingCode ||
      !user.verificationCodeExpires ||
      user.verificationCodeExpires.getTime() < Date.now()
    ) {
      return res.status(400).json({ message: "Invalid or expired code" });
    }

    // Mark verified
    user.isVerified = true;
    user.verificationCode = null;
    user.verificationCodeExpires = null;

    await user.save();

    WelcomeEmail(user.email, user.username);

    return res.status(200).json({ message: "Email verified successfully" });

  } catch (err) {
    return res.status(500).json({ message: err.message });
  }
}

async function handleResetPwdEmail(req, res) {
  try {
    const { email } = req.body;

    if (!email) {
      return res.status(400).json({ message: "Email is required" });
    }

    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }

    const resetToken = crypto.randomBytes(32).toString("hex");

    const resetTokenHash = crypto
      .createHash("sha256")
      .update(resetToken)
      .digest("hex");

    // Save in DB
    user.resetPasswordToken = resetTokenHash;
    user.resetPasswordExpires = new Date(Date.now() + 15 * 60 * 1000); // 15 min
    await user.save();

    // Send link
    const appUrl = "http://localhost:5000";
    const resetLink = `${appUrl}/bidsphere/user/resetpwd?token=${resetToken}&email=${encodeURIComponent(email)}`;

    await SendResetPwdEmail(email, resetLink);

    return res.status(200).json({ message: "Reset email sent" });
  } catch (err) {
    return res.status(500).json({ message: err.message });
  }
}

async function handleResetPwd(req, res) {
  try {
    const { token, email } = req.query;
    const { newPassword, confirmNewPassword } = req.body;

    if (!token || !email || !newPassword || !confirmNewPassword) {
      return res.status(400).json({ message: "All fields required" });
    }

    if (newPassword !== confirmNewPassword) {
      return res.status(400).json({ message: "Passwords do not match" });
    }

    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }

    // 🔐 Hash incoming token
    const incomingTokenHash = crypto
      .createHash("sha256")
      .update(token)
      .digest("hex");

    // Validate token + expiry
    if (
      user.resetPasswordToken !== incomingTokenHash ||
      !user.resetPasswordExpires ||
      user.resetPasswordExpires.getTime() < Date.now()
    ) {
      return res.status(400).json({ message: "Invalid or expired token" });
    }

    // Prevent same password reuse
    const isSame = await bcrypt.compare(newPassword, user.password);
    if (isSame) {
      return res.status(400).json({ message: "New password must be different" });
    }

    // Save new password
    user.password = await generateHashPassword(newPassword);

    // Clear token fields
    user.resetPasswordToken = null;
    user.resetPasswordExpires = null;

    await user.save();

    return res.status(200).json({ message: "Password reset successful" });

  } catch (err) {
    return res.status(500).json({ message: err.message });
  }
}


export { handleRegister, handleLogin, handleLogout, verifyEmail, handleResetPwdEmail, handleResetPwd };
