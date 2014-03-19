var express = require('express');
var port = process.env.PORT || 8000;
var app = express();

 
app.get('/', function(request, response) {
    response.sendfile(__dirname + '/index.html');
}).configure(function() {
    app.use('/', express.static(__dirname + '/'));
});

app.get('/api/city-data', function (request, response) {
				// Fetch JSON
				response.sendfile(__dirname + '/scraper/sencha_data.json');
}).configure(function() {
    app.use('/', express.static(__dirname + './'));
});

app.listen(port)