import kue from "kue"
const queue = kue.createQueue();

queue.process('push_notification_code', async (job, done) => {
    try {
        console.log(`Processing job ${job.id} with data:`, job.data);

        await sendNotification(job.data.phoneNumber, job.data.message);

        done();
    } catch (error) {
        console.error(`Error processing job ${job.id}:`, error);
        done(error); 
    }
});

async function sendNotification(phoneNumber, message) {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(` Sending notification to ${phoneNumber}, with message: ${message}`);
            resolve();
        }, 1000);
    });
}