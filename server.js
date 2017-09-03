require('fetch')
var request = require('request');

console.log('starting...')

request('http://74.208.159.205:5000/Sensors', function(err, resp, body) {
	console.log(err);
	console.log(resp);
	console.log(body);
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


