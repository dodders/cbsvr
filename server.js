var request = require('request');

console.log('starting...')

var url = 'http://74.208.159.205:5000/Sensors?where={"type":"F", "node_id":"41"}'
//var url = 'http://74.208.159.205:5000/Sensors' 

request(url, function(err, resp, body) {
	//console.log(err);
	//console.log(resp);
    console.log('body retrieved! processing...')
    var sensorData = JSON.parse(body)
    console.log(sensorData._items.length, ' items found.')
    var curData = [] //array of objects {'date': dateObj, 'value': valueObj}

    sensorData._items.forEach(function(el) {
        var ct = 0;
        curData.concat({'count': ct, 'value': ct});
        ct++;
        console.log(ct, curData);
    }, this);
    console.log(curData)
});

/*fetch('http://74.208.159.205:5000/Sensors').then(function(resp) {
	console.log(resp)
});*/

/*ax({
    method: 'get',
    //url: 'https://jsonplaceholder.typicode.com/posts/1'
    url: 'http://74.208.159.205:5000/Sensors'
})
    .then(function(resp){
        console.log(resp.data._meta)
    })*/


