$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the values of the form fields
        var username = $('#username').val();
        var password = $('#password').val();

        // Simple validation example
        if (username && password) {
            // TO DO: Implement actual login logic here, e.g., AJAX request to server
            
            // Redirect to request.html after successful login
            window.location.href = 'request.html';
        } else {
            alert('Please enter both username and password.');
        }
    });
});
