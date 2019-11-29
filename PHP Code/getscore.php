<?php
//connect to database

$user = "button";
$password = "buttonpress";
$ip= "5.189.155.63";
$dbname = "button";

try {
    $dbh = new PDO("mysql:host=$ip;dbname=$dbname", $user, $password);
} catch (PDOException $e) {
    die("DB Conn Error - $e");
}

$sth = $dbh->query('SELECT MAX(buttonID) AS maximum FROM buttons');
$result = $sth->fetch(PDO::FETCH_ASSOC);
echo $result["maximum"];

$dbh = null;

?>