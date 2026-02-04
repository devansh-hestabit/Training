const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// ✅ HEALTH CHECK
app.get("/health", (req, res) => {
  res.send("Server is healthy");
});

mongoose.connect("mongodb://mongo:27017/logindb")
  .then(() => console.log("MongoDB connected"))
  .catch(err => console.error(err));

const UserSchema = new mongoose.Schema({
  email: String,
  password: String
});

const User = mongoose.model("User", UserSchema);

app.post("/register", async (req, res) => {
  const user = new User(req.body);
  await user.save();
  res.send("User registered");
});

app.post("/login", async (req, res) => {
  const user = await User.findOne(req.body);
  if (!user) return res.status(401).send("Invalid credentials");
  res.send("Login successful");
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});
