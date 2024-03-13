<?php

error_reporting(E_ALL);
ini_set('display_errors', 1);
// jklnlln



    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // check if the file was uploaded without errors 
        if (isset($_FILES["file"]) && $_FILES["file"]["error"] == 0) {
            // Specify the directory where you want to upload the uploaded file
            $target_dir = "uploads/";
            $target_file = $target_dir . basename($_FILES["file"]["name"]);

            // check if the file already exists 
            if (file_exists($target_file)) {
                echo "File already exists. Please try again later!";
            } else {
                // Move the file to the specified directory 
                if (move_uploaded_file($_FILES["file"]["name"], $target_file)) {
                    echo "The file " . htmlspecialchars(basename($_FILES["file"]["name"])) . " has been uploaded.";
                } else {
                    echo "Sorry, there was an error uploading your file.";
                }
            }
        } else {
            echo "Error: " . $_FILES["file"]["error"];
        }
    }
?>
