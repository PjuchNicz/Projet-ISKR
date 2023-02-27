
require('dotenv').config();

const { apiGet, getLastUrlCSV } = require("./data-gouv");
const { filenameFromUrl, errorWrapper } = require("./utils");
const { getFile,unZip,uploadFile } = require("./file");


async function get() {
  const url = `${process.env.API_URL_DATAGOUV}/${process.env.ENDPOINT_FRANCE_COMP_DATASET}/${process.env.SLUG_FRANCE_COMP_DATASET}`;
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



module.exports = { get };
