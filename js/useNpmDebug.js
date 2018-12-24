// https://www.npmjs.com/package/debug

// testing out debug package from npm

// start as nodejs useNpmDebug.js
// as tin@bofh
// but couldn't get it to work fully, get error that i don't want to dig into
// SyntaxError: Block-scoped declarations (let, const, function, class) not yet supported outside strict mode
// oh, the os included nodejs is 4.2.6, and it need a newer version 7.4
// i suppose os version is much older than what nodejs provides  *sigh*



var debug = require('debug')('http')
  , http = require('http')
  , name = 'My App';

/*
var http = require('http');  
var uc = require('upper-case');  
var debug = require('debug');  
*/

// fake app

//debug('booting %o', name);

http.createServer(function(req, res){
  res.statusCode = 200;
  //debug(req.method + ' ' + req.url);
  res.end('hello\n');
}).listen(5002, function(){
  debug('listening');
  //res.end('hello-end-by-tin\n');
});

// fake worker of some kind

//require('./useNpmDebug_worker');
