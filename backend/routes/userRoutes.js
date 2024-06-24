import express from "express";
import { registerUser, authUser } from "../controllers/userControllers.js";

const router = express.Router();

router.post("/auth", authUser);
router.post("/register", registerUser);

export default router;
