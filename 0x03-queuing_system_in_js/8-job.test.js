import kue from "kue";
import createPushNotificationsJobs from "./8-jobs";
const queue = kue.createQueue();

beforeAll(() => {
    queue.testMode.enter();
})
afterAll(() => {
     queue.testMode.exit();
});
afterEach(()=> {
    queue.testMode.clear();
})

describe('createPushNotificationsJobs function', () => {
    it('should create jobs and add them to the queue', () => {
        const jobData = [
            { phoneNumber: '1234567890', message: 'Hello User 1' },
            { phoneNumber: '9876543210', message: 'Hello User 2' }
        ];

        const jobs = createPushNotificationsJobs(jobData);
        
        // Validate the number of jobs in the queue
        expect(queue.testMode.jobs.length).toBe(2);
        
        // Check the job types and data
        expect(queue.testMode.jobs[0].type).toBe('push_notification');
        expect(queue.testMode.jobs[0].data).toEqual(jobData[0]);
        
        expect(queue.testMode.jobs[1].type).toBe('push_notification');
        expect(queue.testMode.jobs[1].data).toEqual(jobData[1]);
        
        // Check job IDs
        expect(jobs[0].id).toBeDefined();
        expect(jobs[1].id).toBeDefined();
    });

    it('should throw an error if the job data is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array')).toThrow('Jobs data must be an array');
    });

    it('should handle an empty array gracefully', () => {
        const jobs = createPushNotificationsJobs([]);
        expect(queue.testMode.jobs.length).toBe(0); // No jobs should be created
        expect(jobs.length).toBe(0); // No jobs returned
    });
});