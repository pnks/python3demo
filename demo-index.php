<?php
  $bericht = "<voer hier je bericht in>";
  $naam = "<voer hier je naam in>";
?>

<html>
	<head><title>Bericht van <?php print(htmlentities($naam)); ?></title>
	</head>
	<body>
		<h1><?php print(htmlentities($naam));?> heeft het volgende bericht</h1>
		<p><?php print(htmlentities($bericht));?></p>
	</body>
</html>


