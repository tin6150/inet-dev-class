//  https://nodejs.org/en/docs/guides/getting-started-guide/
// start node server with this file, eg
// nodejs helloWorld.js 


// https://www.w3schools.com/nodejs/nodejs_npm.asp
// installing package, in the current dir, run 
// npm install upper-case
// it creates node_modules
// and place things there
// it will display warning if there is not package.json file

const http = require('http');	// http is nodejs build-in module

var uc = require('upper-case'); 	// this use npm installed package (which is a js)

//const hostname = '127.0.0.1';
//const port = 3000;
const hostname = '0.0.0.0';
const port = 5002;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.write('\n'); 
  res.write(uc('Hello World\n'));   // call to use uc the upper-case package
  res.write('requested url path: '); 
  res.write(req.url);		// req is input param passed back by the http module
  //res.end('Hello World\n');
  res.end();
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
