const { errorWrapper } = require("./utils");

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

  module.exports = { apiGet,getLastUrlCSV };