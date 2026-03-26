import express from "express";
import { config } from "dotenv";
import { connectDB } from "./db/connectDB.js";
import { Users } from "./models/model.user.js";
import cors from "cors";
config();
const app = express();
app.use(cors());
app.use(express.json());
const port = 5000 || process.env.PORT;
// GET
app.get("/", async (req, res) => {
const user = await Users.find();
res.send(user);
});

app.post("/", async (req, res) => {
const user = await Users.create(req.body);
res.send(req.body);
});