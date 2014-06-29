/*
test data for test_post.js and test_get.js
*/
json={
  devmgr: "DeviceManager_VT",
  device: "temp_humidity",
  user: "paul@virtual-techno.com",
  pass: "<ask paul>",
  data: {
    temp: Math.floor(Math.random()*25*100)/100,
    humidity: Math.floor(Math.random()*100*100)/100,
  }
}
process.stdout.write(JSON.stringify(json)+"\n");
if (process.argv[2]) {
  setInterval(function() {
    process.stdout.write(JSON.stringify(json)+"\n");
  },process.argv[2]);
}
