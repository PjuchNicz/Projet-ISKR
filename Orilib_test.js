const api_url_datagouv = "https://www.data.gouv.fr/api/1";
const slug_france_comp_dataset =
  "repertoire-national-des-certifications-professionnelles-et-repertoire-specifique";
const endpoint_france_comp_dataset = "datasets";

const https = require("https");
const fs = require("fs");
const bucketName = "france-competence-test.appspot.com";
const { Storage } = require("@google-cloud/storage");
const storage = new Storage();
const AdmZip = require("adm-zip");

async function main() {
  const url = `${api_url_datagouv}/${endpoint_france_comp_dataset}/${slug_france_comp_dataset}`;
  try {
    const result = await apiGet(url);
    const resources = result.resources;
    const zipUrl = getLastUrlCSV(resources);
    if (zipUrl) {
      console.log(`Found ${zipUrl}`);
      getFile(zipUrl);
    } else {
      throw new Error("No zip found");
    }
  } catch (error) {
    console.log(`Error: ${error.message}`);
  }
}

async function apiGet(url) {
  // Function to fetch get to url and return json
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });
    if (!response.ok) {
      throw new Error(`${response.status}: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    errorWrapper("apiGet", error);
  }
}

function getLastUrlCSV(resources) {
  //Return the url of the lastest csv file
  try {
    const last_url =
      resources
        .filter((item) => item.title.includes("export-fiches-csv-")) //Only keep export-fiches-csv-
        .reduce((prev, curr) => (prev.title > curr.title ? prev : curr), {}) //Get the lastest date
        .url || null; //If there is no url in the last item, return null
    if (last_url == null) {
      throw new Error("No last url found");
    }
    return last_url;
  } catch (err) {
    errorWrapper("getLastUrlCSV", err);
  }
}

function getFile(url) {
  try {
    const file = fs.createWriteStream(filenameFromUrl(url) + ".zip");
    const request = https.get(url, function (response) {
      response.pipe(file);
      // after download
      file.on("finish", () => {
        file.close();
        const file_name = filenameFromUrl(url);
        const zip_name = `${file_name}.zip`;
        console.log(`Download of ${zip_name} Completed`);
        uploadFile(zip_name);
        unZip(file_name);
      });
    });
  } catch (err) {
    errorWrapper("getFile", err);
  }
}

function unZip(filename) {
  //Function to unzip a file
  try {
    var zip = new AdmZip(`${filename}.zip`);
    zip.extractAllTo(/*target path*/ `./${filename}/`, /*overwrite*/ true);
    console.log(`${filename}.zip unzip at ./${filename}/`)
  } catch (err) {
    errorWrapper("unZip", err);
  }
}

async function uploadFile(filename) {
  try {
    const options = {
      destination: filename,
    };
    try {
      await storage.bucket(bucketName).upload(filename, options);
      console.log(`${filename} uploaded to ${bucketName}`);
    } catch (err) {
      throw new Error(`An error occured while uploading ${filename} to ${bucketName}. Error: ${err.message}`);
    }
  } catch (err) {
    errorWrapper("uploadFile", err);
  }
}

function errorWrapper(function_name, err) {
  // Function to add the name of the function in the message of the error.
  // It is usefull for debuging.
  e = new Error(`${function_name}: ${err.message}`);
  e.stack = err.stack;
  throw e;
}

function filenameFromUrl(url) {
  //Return the filename from an url
  return url.split("/").pop().split(".")[0];
}

module.exports = { main };
