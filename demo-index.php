<?php
$naam = "<voer hier je naam in>";
$bericht = <<<ENDOFMESSAGE
<voer hier je bericht in>
ENDOFMESSAGE;
?>

<html>
	<head><title>Bericht van <?php print(htmlentities($naam)); ?></title>
	</head>
	<body>
		<h1><?php print(htmlentities($naam));?> heeft het volgende bericht</h1>
		<pre><?php print(htmlentities($bericht));?></pre>
	</body>
</html>


