
JavaScript
==========

took a class on jQuery, dealt thw AJAX, UI, etc.
maybe see the code folder in dropbox.

There was also the taxonomy reporter html page that called jQuery to provide some basic sorting and highligiting to tables, client side code so just need to access the html.

Node.js
=======

some server that use js on the server-side...


npm
===

- package manager for js.
- lots of js packages out there.

- run as user, not as root, as it add js library to an existing project
- js on client side?  or need server support???

- npm can install packages locally (eg by user for a project) or globally (ie system-wide by root)
- sudo npm  back in version 5.7.1 changed ownership of system files and broke the OS!!  There may not be a lot of reason why package need to be installed globally... 

- npm look at package.json and install all dependencies listed in it.
- package-lock.json list exact version of package use to prevent changing version.


- this may help understand better about npm: 
  https://www.npmjs.com/package/express


- kinda descent intro to npm
  https://webpack.js.org/guides/getting-started/
  i guess it install package locally, need a web server to serve them.
  but js still run client-side on browser, just that js not loaded via public url but served from my server?

- may want to start with this node.js intro
  https://codeburst.io/the-only-nodejs-introduction-youll-ever-need-d969a47ef219


.. code:: bash

        npm init                # creates a barebone package.json

        npm install ... 


will create a folder called node_module in current dir

will update package.json, which list all requirements.  the file must exist first.




