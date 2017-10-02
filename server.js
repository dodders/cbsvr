var request = require('request');
var dateformat = require('dateformat')

console.log('starting...')

var oldurl = 'http://74.208.159.205:5000/Sensors?where={"type":"F","node_id":"41"}'
//url2 is hopefully 7/23/2017 9am to 7/23/2017 10am.
var urlbase = 'http://74.208.159.205:5000/Sensors?page='
var urlparams = '&where={"type":"F","node_id":"41","time":{"$gte":1500814800},"time":{"$lte":1500818400}}'
var url2 = 'http://74.208.159.205:5000/Sensors?page=1&where={"type":"F","node_id":"41","time":{"$gte":1500800400},"time":{"$lte":1500804000}}'
//var url = 'http://74.208.159.205:5000/Sensors' 

//just do this! so odd...
temps = new Map()
totalCt = 0
getPage(1)

function getPage(currpage) {
    var url = urlbase.concat(currpage).concat(urlparams)
    console.log('retrieving url:', url)
    request(url, function(err, resp, body) {
        console.log('body retrieved! processing...')
        var sensorData = JSON.parse(body)
        console.log(sensorData._items.length, ' items found.')
        sensorData._items.forEach(function(el) {
            temps.set(fmtDate(el.time), fmtTemp(el.value))
            totalCt = totalCt + 1
            //graphData.push({'date': fmtDate(el.time), 'value': fmtTemp(el.value)});
        }, this)
        
        // for (var [key, value] of temps.entries()) {
        //     arr.push({'date' : key, 'value': value})
        // }

        if (sensorData._links.next != null) {
            getPage(currpage + 1)
        } else {
            console.log('no more pages to retrieve.')
            console.log('final output:\n', temps)
            console.log('total points retrieved:', totalCt, ' and total ppm:', temps.size)
        }
    });
}

function fmtDate(epochtime) {
    var d = new Date(epochtime * 1000)
    //use date format to limit measurements to 1 per minute.
    //return dateformat(d, "yyyy-mmm-dd HH:MM") 
    return dateformat(d, "yyyy-mmm-dd HH") 
}

function fmtTemp(temp) {
    return temp.replace("\'","").replace("\'","").replace('b','').trim()    
}