#!/usr/bin/env node

function chunkArray(array, chunks) {
  const result = [];
  const chunkSize = Math.ceil(array.length / chunks);

  for (let i = 0; i < array.length; i += chunkSize) {
    result.push(array.slice(i, i + chunkSize));
  }

  return result;
}
function processChunk(words) {
  return new Promise((resolve) => {
    const wordCount = {};
    let longestWord = "";
    let shortestWord = words[0] || "";

    for (const word of words) {
      wordCount[word] = (wordCount[word] || 0) + 1;

      if (word.length > longestWord.length) longestWord = word;
      if (word.length < shortestWord.length) shortestWord = word;
    }

    resolve({
      wordCount,
      longestWord,
      shortestWord,
      totalWords: words.length
    });
  });
}

const fs = require("fs");
const concurrency = parseInt(process.env.CONCURRENCY) || 4;



const args = process.argv.slice(2);


const fileIndex = args.indexOf("--file");
if (fileIndex === -1) {
  console.error("❌ Please provide --file argument");
  process.exit(1);
}
const filePath = args[fileIndex + 1];


const topIndex = args.indexOf("--top");
let topN = 5;
if (topIndex !== -1) {
  topN = parseInt(args[topIndex + 1]);
}

const text = fs.readFileSync(filePath, "utf-8");


const allWords = text
  .toLowerCase()
  .split(/\s+/)
  .filter(Boolean);

const chunks = chunkArray(allWords, concurrency);

Promise.all(chunks.map(chunk => processChunk(chunk)))
  .then(results => {

    const finalWordCount = {};
    let longestWord = "";
    let shortestWord = results[0].shortestWord;
    let totalWords = 0;

    for (const result of results) {
      totalWords += result.totalWords;

      if (result.longestWord.length > longestWord.length) {
        longestWord = result.longestWord;
      }

      if (result.shortestWord.length < shortestWord.length) {
        shortestWord = result.shortestWord;
      }

      for (const word in result.wordCount) {
        finalWordCount[word] =
          (finalWordCount[word] || 0) + result.wordCount[word];
      }
    }

    const uniqueWords = Object.keys(finalWordCount).length;

    const topWords = Object.entries(finalWordCount)
      .sort((a, b) => b[1] - a[1])
      .slice(0, topN);

    console.log("📊 Word Statistics (Concurrency:", concurrency, ")");
    console.log("Total words:", totalWords);
    console.log("Unique words:", uniqueWords);
    console.log("Longest word:", longestWord);
    console.log("Shortest word:", shortestWord);
    console.log(`Top ${topN} most repeated words:`);

    for (const [word, count] of topWords) {
      console.log(`${word} → ${count}`);
    }
const stats = {
  totalWords,
  uniqueWords,
  longestWord,
  shortestWord,
  topWords: topWords.map(([word, count]) => ({
    word,
    count
  }))
};

if (!fs.existsSync("output")) {
  fs.mkdirSync("output");
}

fs.writeFileSync(
  "output/stats.json",
  JSON.stringify(stats, null, 2)
);

});
