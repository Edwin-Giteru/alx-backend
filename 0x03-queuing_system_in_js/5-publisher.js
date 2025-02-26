import { createClient } from 'redis';

// Create Redis client
const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish a message after a delay
const publishMessage = (message, time) => {
    setTimeout(async () => {
        console.log(`About to send ${message}`);
        
        try {
             await client.publish('ALXchannel', message);
            
        } catch (err) {
            console.error(`Error publishing message: ${err.message}`);
        }

        // Close client only after the last message
        if (message === 'KILL_SERVER') {
            setTimeout(() => {
                client.quit();
                console.log('Redis client closed');
            }, 1000);
        }
    }, time);
};

// Ensure client is connected before publishing
client.connect().then(() => {
    publishMessage("ALX Student #1 starts course", 100);
    publishMessage("ALX Student #2 starts course", 200);
    publishMessage("KILL_SERVER", 300);
    publishMessage("ALX Student #3 starts course", 400);
    
});
