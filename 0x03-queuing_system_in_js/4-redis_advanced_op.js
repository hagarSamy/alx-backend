import redis from "redis";

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server: ', err);
});

// client.hset('HolbertonSchools', 'Portland', 50,
//     'Seattle', 80, 'New York', 20, 'Bogota', 20,
//     'Cali', 40, 'Paris', 2, redis.print);

client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) {
    console.log("couldn't get the hash ", err)
  }
  console.log(obj);
});
