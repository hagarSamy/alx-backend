function createPushNotificationsJobs(jobs, queue) {
  if (typeof(jobs) != array) {
    throw new Error('Jobs is not an array');
  };
  jobs.array.forEach(job => {
    queue.create('push_notification_code', job)
    .save((err) => {
      if (!err) console.log('Notification job created: ', job.id);
    });
    
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (error) => {
      console.log(`Notification job ${job.id} failed: ${error}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`)
    })
  });
}
