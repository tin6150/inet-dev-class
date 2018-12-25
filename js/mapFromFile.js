// https://www.w3schools.com/nodejs/nodejs_filesystem.asp

// this should serve the mapbox html file out to client 
// really just using node js server to serve out file at this point

// ZWEDC_50x50sq.html was from the mapbox folder

// start as
// nodejs mapFromFile.js
// client hit http://bofh:5002

var http = require('http');
var fs = require('fs');

var server = http.createServer(function (req, res) {
  //fs.readFile('ZWEDC_50x50sq.html', 		// work with this one
  fs.readFile('ZWEDC_50x50sq+Plugin.html', 	// fail here, either w/ or w/o "import clause
  function(err, data) {
    //res.writeHead(200, {'Content-Type': 'text/html'});
    //res.writeHead(200, {'Content-Type': 'application/javascript'});
    res.writeHead(200, {'Content-Type': 'text'});
    res.write(data);
    res.end();
  });
});

const hostname = '0.0.0.0';
const port = 5002;

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

