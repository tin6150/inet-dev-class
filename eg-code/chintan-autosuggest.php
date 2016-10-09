<html>


<table align= "center" VSPACE=10 BORDER= 1 width=890 height=100 bordercolor = "black">
<form name="form1" method="POST" action="cgi-bin/pass5.py">
<td width=150 height=150 bgcolor="#FFFF00">
<b>
 GENE NAME<br><br>

<!--AJAX AUTOSUGGEST SCRIPT -->
<script type="text/javascript" src="http://phusem-vml-pathach1.na.novartis.net/searchautosuggest/lib/ajax_framework.js"></script>

<style type="text/css">
/* ---------------------------- */
/* CUSTOMIZE AUTOSUGGEST STYLE  */
#search-wrap input{width:150px; font-size:16px; color:#999999; padding:6px; border:solid 1px #999999;}
#results{width:150px; border:solid 1px #DEDEDE; display:none;}
#results ul, #results li{padding:0; margin:0; border:0; list-style:none;}
#results li {border-top:solid 1px #DEDEDE;}
#results li a{display:block; padding:4px; text-decoration:none; color:#000000; font-weight:bold;}
#results li a small{display:block; text-decoration:none; color:#999999; font-weight:normal;}
#results li a:hover{background:#FFFFCC;}
#results ul {padding:6px;}
</style>
<div id="search-wrap">
<font-size = 16px>Enter Gene Name</font><br>
<input name="search-q" id="search-q" type="text" onkeyup="javascript:autosuggest()"/>
<div id="results"></div>
</div>


 </td>
<td width=150 height=150 bgcolor="#FFFF00">
&nbsp;&nbsp;&nbsp;<input type="checkbox" name="study" value="study"> <B>DATABASE NAME
<br><BR><br>
 <select name="select2">
    <option>E_MEXP_121</option>
    <option>GSE_19449_20559</option>
     <option>NUID_0077_5214</option>
    <option>NUID_0056_4484</option>
</select>
</td>

<td height=50 width=150 bgcolor="#FFFFCC">

<input type="checkbox" name="range" value="range"> <B>SCORE RANGE <br><br>&nbsp;
<br> <select name="select3">
    <option>0.1</option>
    <option>0.2</option>
    <option>0.3</option>
    <option>0.4</option>
    <option>0.5</option>
    <option>0.6</option>
    <option>0.7</option>
    <option>0.8</option>
    <option>0.9</option>
    </select>
</td>

<td width=60 height=150 bgcolor="#FFFF00"><b> DATA LIMIT<br><br><br>
<input type="integer" size=2  name="limit" value="limit">
</td>


<td width=60 height=150 bgcolor="#FFFF00"><b>
ORDER SELECT <br>&nbsp;
<br>
    <select name="select4">
    <option></option>
    <option>ASC</option>
    <option>DESC</option>
    </select>
</td>

</tr>
</table>


<tr>

<td width=100 height = 20>
<br> &nbsp;&nbsp;&nbsp;&nbsp;
<input type="submit" value="Submit">
</td>

<td width=60 height = 20>
<input type="reset" value="Reset!">
</td>


</form>
<BR><br>
                     

</html>
