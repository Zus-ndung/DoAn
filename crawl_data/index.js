const cheerio = require("cheerio");
const request = require("request");
const fs = require("fs");
const readline = require("readline");

const wirteFile = (filename, text) => {
  fs.writeFile(`./data/${filename}.txt`, text, (error) => {
    if (error) {
      console.log(error);
    } else {
      console.log(`Crawl ${filename} OK`);
    }
  });
};

const readFile = async () => {
  const data = [];
  const rd = readline.createInterface({
    input: fs.createReadStream("./countryList.txt"),
    crlfDelay: Infinity,
  });
  for await (const line of rd) {
    // Each line in input.txt will be successively available here as `line`.
    data.push(line);
  }
  return data;
};

const crawlData = (countryList) => {
  const baseUrl = "https://vi.wikipedia.org/wiki/";
  for (const country of countryList) {
    request(`${baseUrl}${country}`, (err, res, body) => {
      if (res?.statusCode === 200) {
        const $ = cheerio.load(body);
        let countryInformation = $("span.country-name").text();

        $("table.infobox > tbody > tr").each(function () {
          let elememt = $(this).text();
          elememt = elememt.trim();
          if (elememt.length !== 0) {
            let newElememt = "";
            for (let i = 0; i < elememt.length; i++) {
              newElememt += elememt.charAt(i);
            }
            newElememt = newElememt.replace(String.fromCharCode(160), " ");
            countryInformation += `\n${newElememt}`;
          }
        });
        wirteFile(country, countryInformation);
      }
    });
  }
};

const runStart = async () => {
  const data = await readFile();
  crawlData(data);
};
runStart();
