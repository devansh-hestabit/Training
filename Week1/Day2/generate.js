const fs = require("fs");

let text = "lorem ipsum dolor sit amet ";
let bigText = text.repeat(50000);

fs.writeFileSync("corpus.txt", bigText);
