import express from "express";
import mongoose from "mongoose";
import { config } from "dotenv";

config();
const app = express();
const port = 5000;
app.listen(port, () => {
    console.log("app is connected");
})

