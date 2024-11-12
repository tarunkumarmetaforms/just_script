const fs = require("fs");

function generatePythonFile(inputFile, outputFile) {
  fs.readFile(inputFile, "utf8", (err, data) => {
    if (err) {
      console.error("Error reading file:", err);
      return;
    }

    const chunks = data.split(/<!-- START Chunk.*?-->/).slice(1);
    let pythonContent = `
qnr2_examples: List[BaseSystemPrompt | BaseExample] = [
    BaseSystemPrompt(system_prompt=chunk_part_extractor_system_prompt),`;

    chunks.forEach((chunk, index) => {
      const cleanedChunk = chunk.split("<!-- END Chunk")[0].trim();
      pythonContent += `
    Example(
        input=textwrap.dedent(
            """
${cleanedChunk}
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),`;
    });

    pythonContent += "\n]";

    fs.writeFile(outputFile, pythonContent, "utf8", (err) => {
      if (err) {
        console.error("Error writing file:", err);
      } else {
        console.log("Python file generated successfully.");
      }
    });
  });
}

// Usage
const inputFile = "output.txt";
const outputFile = "output.py";
generatePythonFile(inputFile, outputFile);
