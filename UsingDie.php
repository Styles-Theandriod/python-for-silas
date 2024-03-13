<?php

$file = 'example.txt';

// Attempt to open a file
$handle = fopen($file, 'r');

// Check if the file was successfully opened
if (!$handle) {
    die("Unable to open file: $file"); // Terminate the script with an error message
}

// Continue with the rest of the script if the file was opened successfully
echo "File opened successfully.";

// Close the file handle
fclose($handle);

?>
