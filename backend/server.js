const express = require("express");
const mongoose = require("mongoose");
const dotenv = require("dotenv").config({ path: "../.env" });

const app = express();

// Start server and connect to MongoDB
const PORT = process.env.PORT || 3001;
app.listen(PORT, async () => {
  console.log(`Server running on port ${PORT}`);
  try {
    await mongoose.connect(process.env.MONGODB_URI);
    console.log("Connected to MongoDB");
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
});
