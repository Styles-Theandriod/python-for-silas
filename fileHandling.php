<?php 
$file = fopen("example.txt", "r"); // Open for reading

$content = fread($file, filesize("example.txt"));

echo $content;

// Reading from a File:

// To read the contents of a file, you can use functions like fread() or fgets()
// OR
while (!feof($file)) {
    $line = fgets($file);
    // Process each line
}

// Writing to a File:

// To write data to a file, use functions like fwrite().

$file = fopen("example.txt", "w"); // Open for writing
fwrite($file, "Hello, World!\n");
fclose($file);



// Appending to a File:

// To append data to an existing file, use the mode "a" (append) with fopen().

$file = fopen("example.txt", "a"); // Open for appending
fwrite($file, "Appending new data.\n");
fclose($file);


// Closing a File:

// Always close a file when you are done with it using fclose()
fclose($file);


// Checking if a File Exists:
// To check if a file exists, use the file_exists() function.

if (file_exists("example.txt")) {
    // File exists
} else {
    // File does not exist
}


// Deleting a File:
// To delete a file, use the unlink() function.
unlink("example.txt");


// file Permissions:
// You can set file permissions using chmod().
chmod("example.txt", 0644); // Example: read and write for owner, read for others


// Working with Directories:

// PHP also provides functions for working with directories, such as mkdir() to create a directory and rmdir() to remove a directory.

mkdir("new_directory");
rmdir("new_directory");


?>