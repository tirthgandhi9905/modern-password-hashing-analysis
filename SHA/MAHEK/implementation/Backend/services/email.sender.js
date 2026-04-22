import { sendEmail } from "./nodemailer.js";
import { Verification_Email_Template } from "../email-templates/verify_email.template.js";
import { Welcome_Email_Template } from "../email-templates/welcome_email.template.js";

function buildResetTemplate(resetLink) {
  return `
    <h2>Password Reset Request</h2>
    <p>You requested to reset your password.</p>
    <p>Click the link below to set a new password (valid for 15 minutes):</p>
    <a href="${resetLink}" target="_blank" rel="noopener noreferrer">${resetLink}</a>
    <p>If you did not request this, you can ignore this email.</p>
  `;
}

async function SendVerificationCode(email, verificationCode) {
  const html = Verification_Email_Template.replace("{verificationCode}", verificationCode);
  await sendEmail({
    to: email,
    subject: "Verify your email",
    html,
  });
}

async function WelcomeEmail(email, name) {
  const html = Welcome_Email_Template.replace("{name}", name);
  await sendEmail({
    to: email,
    subject: "Welcome",
    html,
  });
}

async function SendResetPwdEmail(email, resetLink) {
  await sendEmail({
    to: email,
    subject: "Password reset link",
    html: buildResetTemplate(resetLink),
  });
}

export { SendVerificationCode, WelcomeEmail, SendResetPwdEmail };
