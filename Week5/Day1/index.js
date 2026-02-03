const http = require("http");

const server = http.createServer((req, res) => {
  res.end(
    "This file is running inside docker - Devansh , We can add other modules and make it more complex this is just a test file. \n",
  );
});

server.listen(3000, () => {
  console.log("Server running on port 3000");
});
