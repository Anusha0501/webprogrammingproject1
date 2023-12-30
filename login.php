<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve user input
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Replace the following with your actual authentication logic
    if ($email === 'user@example.com' && $password === 'password123') {
        // Authentication successful
        // You can set session variables and redirect to a dashboard or another page
        header('Location: amazon clone.html');
        exit();
    } else {
        // Authentication failed
        // Redirect back to the login page with an error message
        header('Location: login.html?error=1');
        exit();
    }
}
?>
