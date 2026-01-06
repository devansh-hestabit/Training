const fs = require("fs");

console.time("stream-read");

let totalBytes = 0;

const stream = fs.createReadStream("bigfile.txt");

stream.on("data", chunk => {
  totalBytes += chunk.length;
});

stream.on("end", () => {
  console.timeEnd("stream-read");
  console.log("Total bytes read:", totalBytes);
});
