import express from "express";
import {loginPost} from "../controllers/auth.controller"

const authRoute = express.Router();

authRoute.post("/login", loginPost)

export default authRoute;