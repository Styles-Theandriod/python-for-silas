<?php

    $userInput = $_POST['user_email']; // is assuring that the user is from a post request 


    //Validate email address
    if(filter_var($userInput, FILTER_VALIDATE_EMAIL)){
        // sanitize the email 
        $sanitizedEmail = filter_var($userInput, FILTER_SANITIZE_EMAIL);

        // use the sanitized email in your code 
        echo "Valid and sanitized email: $sanitizedEmail";
    }else {
        echo "Invalid email address";
    }



?>