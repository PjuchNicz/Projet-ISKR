const { filenameFromUrl, errorWrapper } = require("./utils");
const https = require("https");
const fs = require("fs");
const { Storage } = require("@google-cloud/storage");
const storage = new Storage();
const AdmZip = require("adm-zip");

require('dotenv').config();
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
    const bucketName = process.env.BUCKET_NAME;
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
  module.exports = { getFile,unZip,uploadFile };