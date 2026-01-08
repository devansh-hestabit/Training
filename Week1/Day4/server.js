const http = require("http");
const url = require("url");

const server = http.createServer((req, res) => {
  const parsed = url.parse(req.url, true);

  if (parsed.pathname === "/echo") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(req.headers, null, 2));
  }

  else if (parsed.pathname === "/slow") {
    const delay = parseInt(parsed.query.ms) || 1000;
    setTimeout(() => {
      res.end("Delayed response: " + delay + " ms");
    }, delay);
  }

  else if (parsed.pathname === "/cache") {
    res.writeHead(200, {
      "Cache-Control": "public, max-age=60",
      "ETag": "demo-etag"
    });
    res.end("Cache enabled");
  }

  else {
    res.statusCode = 404;
    res.end("Not Found");
  }
});

server.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
