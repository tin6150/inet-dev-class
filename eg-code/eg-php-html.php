
<html>

<H1>eg-php-html.php</H1>
Hello.  This is HTML with embeded call to php.
server side php run.
and results in HTML stream send to client.
<BR>
cannot name this file .html, as apache httpd will then not parse the php tags and process them.
but will be passed verbatim to client, which don't know what to do with php tags.
<BR>



<BR><HR><HR><BR>
Calling chintan's code here... test.php<BR>






<BR><HR><HR><BR>


<I>Calling include('test-tin.php') ...</I><BR>
<?php
include('test-tin.php');
?>
<I>Completed include('test-tin.php') ...</I><BR>


<BR><HR><BR>
<H1>Back to eg-php-html.php</H1>

Include in PHP means embed that code into here
so that executed code has to be HTML parseable.

<BR>

<I>Calling include('tin1.php') ...</I><BR>
skipped.<BR>
<!--?php
include('tin1.php');
?-->
<I>completed include('tin1.php') ...</I><BR>

</html>
