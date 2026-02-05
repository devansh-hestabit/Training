const express = require("express");
const os = require("os");

const app = express();

app.get("/api", (req, res) => {
  res.json({
    message: "Hello from backend , this is a temporary backend server used to check for nginx proxying",
    container: os.hostname() 
  });
});

app.listen(3000, () => {
  console.log("Backend running on port 3000");
});
