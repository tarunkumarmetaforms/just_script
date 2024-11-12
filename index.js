const fs = require("fs");

function convertToNumberedFormat(inputFile, outputFile) {
  fs.readFile(inputFile, "utf8", (err, data) => {
    if (err) {
      console.error("Error reading file:", err);
      return;
    }

    const lines = data.split("\n");
    let numberedContent = "";
    let lineNumber = 0;
    let isInsideChunk = false;

    lines.forEach((line) => {
      const trimmedLine = line.trim();
      const indentation = line.match(/^\s*/)[0]; // Capture leading whitespace

      if (trimmedLine.startsWith("<!-- START Chunk")) {
        isInsideChunk = true;
        lineNumber = 0;
        numberedContent += line + "\n";
      } else if (trimmedLine.startsWith("<!-- END Chunk")) {
        isInsideChunk = false;
        numberedContent += line + "\n";
      } else if (isInsideChunk) {
        if (trimmedLine) {
          lineNumber++;
          // Remove extra spaces between attributes, but keep indentation
          let cleanedLine = trimmedLine.replace(/\s+/g, " ");
          // Remove space before closing bracket of empty tags
          cleanedLine = cleanedLine.replace(/\s+\/>/g, "/>");
          numberedContent += `${lineNumber}: ${indentation}${cleanedLine}\n`;
        }
        // Remove this else block to skip empty lines within chunks
      } else {
        numberedContent += line + "\n";
      }
    });

    fs.writeFile(outputFile, numberedContent, "utf8", (err) => {
      if (err) {
        console.error("Error writing file:", err);
      } else {
        console.log("Conversion completed successfully.");
      }
    });
  });
}

// Usage
const inputFile = "input.html";
const outputFile = "output.txt";
convertToNumberedFormat(inputFile, outputFile);
