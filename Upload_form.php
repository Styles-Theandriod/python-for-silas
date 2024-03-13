<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Form</title>
</head>
<body>
    <h2>File Upload Form</h2>
    <!-- <h2>File Upload Form</h2> -->
     
    <form action="upload.php" method="Post" enctype="multipart/form-data">
        <label for="file">Select a file:</label>
        <input type="file" name="file" id="file" required>
        <br>
        <input type="submit" name="submit" value="Upload">
    </form>
</body>
</html>