import { createClient } from "redis";
const client = createClient();


client.on("error", (err)=> {
    console.log("Redis client not connected to ths server", err);
});

client.connect().then(()=> {
    console.log("Redis client connected to the server");
    client.subscribe("ALXchannel", (message) => {
        console.log(message);
    });

})