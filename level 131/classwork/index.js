import express from "express";
import {config} from "dotenv";

config();
const app = express();
const port = 5000 || process.env.PORT;

app.listen(port, ()=> {
console.log("App is connected!", port);
});