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

  module.exports = { errorWrapper,filenameFromUrl };