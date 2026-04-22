import express from "express";
const router = express.Router();

import { handleRegister, handleLogin, handleLogout, handleResetPwdEmail,verifyEmail, handleResetPwd } from "../controller/authController.js";

router.post("/register", handleRegister);
router.post("/login", handleLogin);
router.post("/logout", handleLogout);
router.post("/verifyemail", verifyEmail);

router.post("/forgetpwd", handleResetPwdEmail);
router.post("/resetpwd", handleResetPwd);

export default router;
