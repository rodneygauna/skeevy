const express = require("express");
const dotenv = require("dotenv").config();
const connectDB = require("./config/db");

connectDB();

const app = express();
