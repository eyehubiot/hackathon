/*
get all events from all subdevices on a given subdevice
output to console
limitation: results are not sorted ina sensible way
@paul_tanner 16/11/2013
*/
var request=require('request');
var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
var hostname='https://config28.flexeye.com';
rl.on('line',function(line) {
  json=JSON.parse(line);
  for (var subdev in json.data) {
    var url='/v1/iot_Default/dms/'+json.devmgr+'/devices/'+json.device+'/subDevices/'+subdev+'/events';
    console.log("requesting from",hostname+url);
    request({
      port: 443,
      uri: hostname + url,
      method: 'GET',
      auth: {
        user: json.user,
        pass: json.pass
      }
    }, function (err,arg2,result) {
      var json2=JSON.parse(result);
      for (i in json2.events) {
        url=json2.events[i].uri;
        request({
          port: 443,
          uri: url,
          method: 'GET',
          auth: {
            user: json.user,
            pass: json.pass,
          }
        }, function (err,arg2,result2) {
          var json3=JSON.parse(result2);
          console.log('event',json3.timeStamp,json3.source,json3.payload);
        });
      }
    });
  }
});
