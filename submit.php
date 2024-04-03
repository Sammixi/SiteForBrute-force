<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    include 'db_connect.php';
    // Collecte des data du form
    $pseudo = htmlspecialchars($_REQUEST['pseudo']);
    $password = htmlspecialchars($_REQUEST['password']);
    $password = md5($password);
    if (empty($pseudo) || empty($password)) {
        echo "Tous les éléments sont requis !";
    } else {
        $sql = "INSERT INTO user (pseudo, password) VALUES (?, ?)";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ss", $pseudo, $password);

        if ($stmt->execute()) {
            echo "New record created successfully";
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
        $conn->close();
    }
}
