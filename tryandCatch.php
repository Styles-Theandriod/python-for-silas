<?php

// Custom error handler function
function customErrorHandler($errno, $errstr, $errfile, $errline) {
    echo "<b>Error:</b> [$errno] $errstr in $errfile on line $errline<br>";
}

// Set custom error handler
set_error_handler("customErrorHandler");

// Function to divide two numbers
function divide($dividend, $divisor) {
    if ($divisor == 0) {
        throw new Exception("Division by zero");
    }
    return $dividend / $divisor;
}

// Example of exception handling
try {
    // Attempt division
    $result = divide(10, 0);
    echo "Result: $result<br>"; // This line won't be executed
} catch (Exception $e) {
    // Handle the exception
    echo "<b>Caught exception:</b> " . $e->getMessage() . "<br>";
} finally {
    echo "Finally block executed<br>";
}

// Example of triggering an error
$undefinedVariable = $nonExistentVariable; // This will trigger an error

// This line won't be executed due to the error
echo "This line won't be executed";

?>
