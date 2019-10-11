<?php 

ini_set( 'display_errors', 1 );
ini_set( 'error_reporting', E_ALL );

require_once 'vendor/autoload.php';
require_once 'config.php';

class drama extends Illuminate\Database\Eloquent\Model { 
}

if(isset($_GET['d'])) {
  $id = $_GET['d'];
} else {
  $id = 1;
}

$result = $capsule::table('dramas')->where('id', '=', $id)->get();
$result = $result[0];

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1><?php echo $result->title ?></h1>
  <small><?php echo $result->year ?></small>
  <p><?php echo $result->tag ?></p>
  <p><?php echo $result->actor ?></p>
  <p><?php echo $result->director ?></p>
  <p><?php echo $result->detail ?></p>
</body>
</html>