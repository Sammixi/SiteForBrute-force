<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer votre compte</title>
    <link rel="stylesheet" href="style.css">
    
</head>
<header>
    <a href="login.html">Se connecter</a>
</header>
<body>
    
    <h2>Crée ton mdp</h2>
    <form action="submit.php" method="POST">
        <div>
            <label for="pseudo">Login:</label><br>
            <input type="text" id="pseudo" name="pseudo" required>
        </div>
        <div>
            <label for="password">Mot de passe :</label><br>
            <input type="password" minlength="8" id="password" name="password" required>
            
        </div>
        <div>
            <input type="submit" value="S'enregistrer">
        </div>
    </form>
</body>
</html>