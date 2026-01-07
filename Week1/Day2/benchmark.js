const { execSync } = require("child_process");
const fs = require("fs");

const concurrencyLevels = [1, 4, 8];
const results = [];

if (!fs.existsSync("logs")) {
  fs.mkdirSync("logs");
}

for (const level of concurrencyLevels) {
  console.log(`⏱ Running with concurrency ${level}...`);

  const start = Date.now();

  execSync(
    `CONCURRENCY=${level} node wordstat.js --file corpus.txt --top 10`,
    { stdio: "ignore" }
  );

  const end = Date.now();

  const timeMs = end - start;

  results.push({
    concurrency: level,
    timeMs
  });

  console.log(`✅ Completed in ${timeMs} ms\n`);
}

fs.writeFileSync(
  "logs/perf-summary.json",
  JSON.stringify(results, null, 2)
);

console.log("📁 Benchmark saved to logs/perf-summary.json");
