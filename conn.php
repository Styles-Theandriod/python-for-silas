<?php

$host = 'localhost'; // Remove "http://" from the host
$db_name = "school_db";
$user = "student";
$password = '';

// Create Connection 
$mysqli = new mysqli($host, $user, $password, $db_name);

// Check the connection 
if ($mysqli->connect_error) {
    die("Error connecting to database: " . $mysqli->connect_error);
} else {
    echo "Connection established";
}

?>
