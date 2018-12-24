// https://www.w3schools.com/nodejs/nodejs_filesystem.asp

// this should serve the mapbox html file out to client 
// really just using node js server to serve out file at this point

// ZWEDC_50x50sq.html was from the mapbox folder

// start as
// nodejs mapFromFile.js
// client hit http://bofh:5002

var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
  fs.readFile('ZWEDC_50x50sq.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
  });
}).listen(5002);
