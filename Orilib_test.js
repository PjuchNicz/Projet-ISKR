const api_url_datagouv = "https://www.data.gouv.fr/api/1"
const slug_france_comp_dataset = "repertoire-national-des-certifications-professionnelles-et-repertoire-specifique"
const endpoint_france_comp_dataset = "/datasets/"

const https = require('https');
const fs = require('fs');
async function main(){
  console.log("Launch")
  const url_france_comp_dataset = api_url_datagouv+endpoint_france_comp_dataset+slug_france_comp_dataset
  const result_france_comp_dataset = await api_get(url_france_comp_dataset)
  const resources = result_france_comp_dataset.resources
  const zip_url = get_last_url_csv(resources)
  console.log(zip_url ? zip_url : "Error no zip")
  download_zip(zip_url)
}

async function api_get(url){
  //Function to make a fetch to an url and return the json result
  return fetch(url, {method: 'GET', headers: {'Content-Type': 'application/json'}})
  .then((response) => response.json())
}

function get_last_url_csv(ressources){
  //Function to extract the last url from ressources
  //Add filter or sort to be sure to get the last ?
  for (const item of ressources){
    if(item.title.includes("export-fiches-csv-")){
      return item.url
    }
  }
  return null
}

function download_zip(url){

  const file = fs.createWriteStream(filename_from_url(url)+".zip");
  const request = https.get(url, function(response) {
   response.pipe(file);

   // after download completed close filestream
   file.on("finish", () => {
       file.close();
       console.log("Download Completed");
       //TODO function to send zip to cloud storage
       console.log(`${filename_from_url(url)}.zip`)
       uploadFile(`${filename_from_url(url)}.zip`).catch(console.error);
       unzip_file(filename_from_url(url));
       
       
   });
});
}
function filename_from_url(url){
  //Function to extract the filename from an url
  return url.split('/').pop().split('.')[0];
}
var AdmZip = require("adm-zip");
function unzip_file(filename){
  console.log("a")
  //Function to unzip a file
  var zip = new AdmZip(`${filename}.zip`);
  //var zipEntries = zip.getEntries();
  zip.extractAllTo(/*target path*/ `./${filename}/`, /*overwrite*/ true);
}
const bucketName = 'france-competence-test.appspot.com';
// Imports the Google Cloud client library
const {Storage} = require('@google-cloud/storage');

// Creates a client
const storage = new Storage();

async function uploadFile(filename) {
  const options = {
    destination: filename,

  };

  await storage.bucket(bucketName).upload(filename, options);
  console.log(`${filename} uploaded to ${bucketName}`);
}









module.exports = {main}