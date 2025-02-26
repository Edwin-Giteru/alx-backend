import { createClient } from "redis";

const client = createClient();

client.on("error", (err)=> {
    console.log("Redis client not connected to the server ", err);
});
await client.connect().then( async () => {
    console.log("Redis client connected to the server");

    const key = "ALX";
    await client.del(key)

    await client.hSet(key, "PortLand", 50);
    await client.hSet(key, "Seattle", 80);
    await client.hSet(key, "New York", 20);
    await client.hSet(key, "Bogota", 20);
    await client.hSet(key, "Cali", 40);
    await client.hSet(key, "Paris", 2);

    const result = await client.hGetAll(key);
    console.log(result);

});
