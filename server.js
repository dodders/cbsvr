var request = require('request');
var dateformat = require('dateformat')

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
        curData.push({'date': fmtDate(el.time), 'value': fmtTemp(el.value)});
    }, this);
    console.log(curData)
});

function fmtDate(epochtime) {
    var d = new Date(epochtime * 1000)
    return dateformat(d, "yyyy-mmm-dd HH:MM:ss")
}

function fmtTemp(temp) {
    return temp.replace("\'","").replace("\'","").replace('b','').trim()    
}

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


