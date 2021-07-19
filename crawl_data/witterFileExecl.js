const XLSX = require("xlsx");
const fs = require("fs");
const readline = require("readline");

const readFile = async (path) => {
  const data = [];
  const rd = readline.createInterface({
    input: fs.createReadStream(`./test/${path}`),
    crlfDelay: Infinity,
  });
  for await (const line of rd) {
    // Each line in input.txt will be successively available here as `line`.
    data.push(line);
  }
  return data;
};

const run = async () => {
  const listFile = fs.readdirSync("./test");
  const rows = [];
  for await (const file of listFile) {
    const data = await readFile(file);
    const element = {};
    data.forEach((item, index) => {
      const e = item.split(":");
      element[e[0].toUpperCase()] = e[1];
    });
    element["id"] = data.length;
    console.log(element);
    rows.push(element);
  }

  const newBook = XLSX.utils.book_new();
  const newSheet = XLSX.utils.json_to_sheet(rows);
  XLSX.utils.book_append_sheet(newBook, newSheet, "Sheet1");
  XLSX.writeFile(newBook, "country.xlsx");
};

run();
