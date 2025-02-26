import { createClient } from "redis";

const client = createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

await client.connect()
async function setNewSchool(schoolName, value) {
    try {
        const reply = await client.set(schoolName, value);
        console.log('Reply:', reply);
    } catch (err) {
        console.error('Error setting value:', err);
    }
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await client.get(schoolName);
        console.log(value);
    } catch (err) {
        console.error('Error fetching value:', err);
    }
}



displaySchoolValue("ALX");
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');