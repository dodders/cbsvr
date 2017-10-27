var request = require('request')

console.log('starting...')
var url = 'http://localhost:5000/test'

request(url, function(err, resp, body) {
    console.log('retrieved!', err, resp, body)
})