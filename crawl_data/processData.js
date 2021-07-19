const fs = require("fs");
const readline = require("readline");
const readFile = async () => {
  const data = [];
  const rd = readline.createInterface({
    input: fs.createReadStream("./data/Angola.txt"),
    crlfDelay: Infinity,
  });
  for await (const line of rd) {
    // Each line in input.txt will be successively available here as `line`.
    data.push(line);
  }
  return data;
};

const run = async () => {
  const data = await readFile();
  const result = {};
  result.Ten = data[0];
  data.forEach((item, index) => {
      
  })
};
