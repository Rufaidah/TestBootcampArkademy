<!DOCTYPE html>
<html>
<head>
	<title>Json</title>
</head>
<body>
<?php
	//base url
	$base_url = "http://".$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
	//file menjadi string
	$result = file_get_contents($base_url."biodata.json");
	//string menjadi object
	$json_object = json_decode($result, true);

	//print data object
	echo "Nama : ".$json_object->nama."<br/>";
	echo "Addres : ".$json_object->addres."<br/>";
	echo "Hobbies : ".$json_object->hobbies."<br/>";
	echo "Married : ".$json_object->is_married."<br/>";
	echo "Married : ".$json_object->married."<br/>";
	echo "School : ".$json_object->school."<br/>";
	echo "Skills : ".$json_object->skills;
?>
</body>
</html>
