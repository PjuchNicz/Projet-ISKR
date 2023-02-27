const csv = require("csvtojson");
const { getFirestore } = require("firebase-admin/firestore");
const { initializeApp } = require("firebase-admin/app");
const fs = require("fs");
const path = require("path");

function csvToJson(csvFilePath) {
  return new Promise((resolve, reject) => {
    //https://github.com/Keyang/node-csvtojson
    csv({
      delimiter: ";",
      trim: true,
    })
      .preRawData((csvRawData) => {
        var newData = csvRawData.replace(/\t/g, "");
        return newData;
      })
      .fromFile(csvFilePath)
      .then((jsonObj) => {
        resolve(jsonObj);
      })
      .catch((err) => {
        reject(err);
      });
  });
}

async function jsonToFirebase(name, json) {
  console.log("jsonToFirebase")
  initializeApp();
  const db = getFirestore();
  Object.keys(json).forEach(
    (key) => (json[key] === null) ? json[key] = 'N/A' : json[key]
  );
  for (let i = 0; i < json.length; i++) {
    if (i == 20) break;
    const item = json[i];
    const docRef = db.collection(name).doc();
    await docRef.set(item);
  }
}

async function exportAllCsv(folderPath) {
let buffer = {};
  const files = fs.readdirSync(folderPath);
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const filePath = path.join(folderPath, file);
    const json = await csvToJson(filePath);
    joinCsvOnNumero_Fiche(buffer, json);
    await jsonToFirebase(file, json);
  }
}

function joinCsvOnNumero_Fiche(json1, json2) {
  const result = [];
  for (let i = 0; i < json1.length; i++) {
    const item1 = json1[i];
    const item2 = json2.find((item) => item.Numero_Fiche === item1.Numero_Fiche);
    if (item2) {
      result.push({ ...item1, ...item2 });
    }
  }
  return result;
}



module.exports = { jsonToFirebase, csvToJson,exportAllCsv };
