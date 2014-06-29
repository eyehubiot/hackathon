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
    var msg=JSON.stringify({
      'source': subdev,
      'type': '1.0',
      'payload': "" + json.data[subdev]
    });
    var url='/v1/iot_Default/dms/'+json.devmgr+'/devices/'+json.device+'/subDevices/'+subdev+'/events';
    // note: auth via a header does not work
    var b64=new Buffer("paul@virtual-techno.com:paulk@virtual-techno.com").toString('base64');
    headers={
      "Authorization": 'Basic  ' + b64
    };
    console.log("sending",msg,"to",hostname + url);
    request({
      uri: hostname + url,
      method: 'POST',
      //headers: headers,
      'auth': {
        'user': json.user,
        'pass': json.pass
      },
      port: 443,
      body: msg
    }, function (err,arg2,arg3) {
      if (err) console.log('callback error',err);
    });
  }
});
