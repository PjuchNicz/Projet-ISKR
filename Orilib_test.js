const api_url_datagouv = "https://www.data.gouv.fr/api/1"
const slug_france_comp_dataset = "repertoire-national-des-certifications-professionnelles-et-repertoire-specifique"
const endpoint_france_comp_dataset = "/datasets/"


async function main(){
  console.log("Launch")
  const url_france_comp_dataset = api_url_datagouv+endpoint_france_comp_dataset+slug_france_comp_dataset
  const result_france_comp_dataset = await api_get(url_france_comp_dataset)
  const resources = result_france_comp_dataset.resources
  const zip_url = get_last_url_csv(resources)
  console.log(zip_url ? zip_url : "Error no zip")

}

async function api_get(url){
  //Function to make a fetch to an url and return the json result
  fetch(url, {method: 'GET', headers: {'Content-Type': 'application/json'}})
  .then((response) => {console.log(response);return response.json()})
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

module.exports = {main}