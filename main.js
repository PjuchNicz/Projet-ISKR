const lib = require("./Orilib_test");


async function start() {
    console.log("Launch")
    const value = await lib.main()
 }

 start()