const cheerio = require("cheerio");
const request = require("request");
const fs = require("fs");

request(
  "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_qu%E1%BB%91c_gia_c%C3%B3_ch%E1%BB%A7_quy%E1%BB%81n",
  (err, res, body) => {
    if (res?.statusCode === 200) {
      const $ = cheerio.load(body);
      let countryList = "";
      $(
        "#mw-content-text > div.mw-parser-output > table > tbody > tr > td:nth-child(1) > b > a"
      ).each(function () {
        countryList += `\n${$(this).text()}`;
      });
      wirteFile("countryList", countryList);
    }
  }
);

const wirteFile = (filename, text) => {
  fs.writeFile(`./${filename}.txt`, text, (error) => {
    if (error) {
      console.log(error);
    } else {
      console.log("OK");
    }
  });
};
