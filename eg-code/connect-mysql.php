<?php 
	/* the content-type stuff will be done by PHP automagically?? 
	echo 'Content-Type: text/html; charset=utf8';
	echo '\n\n\n';
	*/
	echo '<HTML>';
        echo 'Hello world <br />';

        //include('config.php'); 
        //$db_host= "phusem-vml-pathach1.na.novartis.net";  //"localhost";  TCP need to use 127.0.0.1
        $db_host= "127.0.0.1";
        $db_name="test";
        $username="test";
        $password="Passw0rD";

        $db_con=mysql_connect($db_host,$username,$password);
        $connection_string=mysql_select_db($db_name);
        $con = mysql_connect($db_host,$username,$password);
        if (!$con) {
        die ("connection error: " .mysql_error());}
         else {
        echo "good... $con";}

        echo '<br />';
        echo 'Bye world <br />';
        mysql_select_db($db_name);
        mysql_close($db_con);

	echo '</HTML>';
        exit();       
?>
