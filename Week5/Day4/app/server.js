const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/html" });

  res.end(`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Devansh | Local HTTPS Environment</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            margin: 0;
            padding: 0;
          }
          .container {
            max-width: 900px;
            margin: 60px auto;
            background: #ffffff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 12px rgba(0,0,0,0.1);
          }
          h1 {
            color: #1f2933;
          }
          p {
            color: #4a5568;
            line-height: 1.7;
          }
          .info {
            margin-top: 30px;
            padding: 20px;
            background: #edf2f7;
            border-left: 5px solid #3182ce;
          }
          footer {
            margin-top: 40px;
            font-size: 14px;
            color: #718096;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Local HTTPS Development Environment</h1>

          <p>
            This application is running inside a Docker-based local development
            environment with HTTPS enabled using a trusted self-signed certificate.
          </p>

          <div class="info">
            <p><strong>Domain:</strong> devansh-hestabit.local</p>
            <p><strong>HTTPS Termination:</strong> NGINX</p>
            <p><strong>Backend:</strong> Node.js (HTTP)</p>
            <p><strong>Purpose:</strong> Learning & internal development</p>
          </div>

          <footer>
            <p>
              This setup mirrors real-world production architecture where SSL is
              terminated at the reverse proxy layer.
            </p>
          </footer>
        </div>
      </body>
    </html>
  `);
});

server.listen(3000, () => {
  console.log("Backend running on port 3000");
});
