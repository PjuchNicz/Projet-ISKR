const { get } = require("./process");
const { exportAllCsv,jsonToFirebase, csvToJson } = require("./database");

async function run() {
  console.log("Launch");
  csvToJson(
    "./export-fiches-csv-2023-01-11/export_fiches_CSV_Certificateurs_2023_01_11.csv"
  ).then((json) => {
    exportAllCsv("./export-fiches-csv-2023-01-11")
  });

  //await 
  //const value = await get()
}

run();
