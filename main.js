const {get} = require("./process");


async function run() {
    console.log("Launch")
    const value = await get()
 }

 run()