#!/usr/prog/php/4.4.9/bin/php

echo "Hello there...\n"

// nope, php is meant to be embeded html script
// to be processed by web server
// so above does't quite run when called as:
// /usr/prog/php/4.4.9/bin/php tin1.php  

/* code must be marked as <?php ?> */
// below will actually execute
<?php
echo "Hello 2"
?>


// this is actually nice, so html code with php
// can just be passed to php as-is, no edit, and
// it will parse output as web server would have displayed back to client
// makes debugging code easier!
