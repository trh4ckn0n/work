(async () => {
  const paths = [
    "/", "/login", "/flas.html", "/logout", "/register", "/enonce",
    "/api/", "/api/v1/users", "/api/v1/data", "/api/v1/items",
    "/api/v1/products", "/api/v1/categories", "/api/v1/orders", "/api/v1/authenticate",
    "/admin", "/admin/dashboard", "/admin/users", "/admin/settings", "/admin/reports",
    "/admin/notifications", "/admin/logs", "/admin/permissions",
    "/dashboard", "/profile", "/profile/edit", "/profile/settings", "/profile/password",
    "/health", "/debug", "/debug/info", "/debug/logs", "/debug/errors", "/debug/stacktrace",
    "/static/app.js", "/static/style.css", "/static/favicon.ico",
    "/static/images/logo.png", "/static/fonts/roboto.ttf", "/static/fonts/roboto-bold.ttf",
    "/search", "/search/results", "/search/query", "/search/filter",
    "/help", "/help/faq", "/help/contact",
    "/terms", "/terms/privacy", "/terms/service",
    "/about", "/about/team", "/about/company", "/about/contact",
    "/sitemap.xml", "/robots.txt",
    "/error", "/error/404", "/error/500", "/error/403", "/error/400", "/error/timeout"
  ];

  const results = [];
  const detectedSigns = new Set();

  const style = document.createElement("style");
  style.innerText = `
    #ffscan { position: fixed; top: 10px; right: 10px; width: 500px; max-height: 92vh; z-index: 99999;
      font-family: 'Courier New', monospace; font-size: 13px; background: #111; color: #eee;
      border: 2px solid #0f0; border-radius: 10px; padding: 10px; box-shadow: 0 0 25px #0f08; overflow-y: auto;
      transition: all 0.3s ease; }
    #ffscan h1 { font-size: 16px; text-align: center; color: #0ff; margin-bottom: 10px; line-height: 1.3em; }
    #ffscan .res { margin-bottom: 4px; padding: 2px 6px; border-left: 4px solid #222; border-radius: 4px; }
    #ffscan .status-200 { border-color: #0f0; color: #0f0; }
    #ffscan .status-403 { border-color: #ff0; color: #ff0; }
    #ffscan .status-404 { border-color: #555; color: #777; }
    #ffscan .status-500 { border-color: #f33; color: #f33; }
    #ffscan .status-0 { border-color: #f0f; color: #f0f; }
    #ffscan textarea { width: 100%; height: 80px; background: #222; color: #ccc; border: 1px solid #444;
      border-radius: 6px; padding: 5px; margin-bottom: 6px; }
    #ffscan button { background: #111; color: #0f0; border: 1px solid #0f0; border-radius: 5px;
      margin: 3px; padding: 4px 8px; cursor: pointer; font-weight: bold; transition: .2s; }
    #ffscan button:hover { background: #0f0; color: #000; }
    #ffscan input[type=file] { margin-top: 5px; display: block; color: #0ff; }
    #ffscan .console { margin-top: 10px; border-top: 1px solid #333; padding-top: 5px; color: #0ff; }
    #ffscan .footer { text-align: center; font-size: 12px; margin-top: 8px; color: #888; }
    #ffscan .toggle { position: absolute; top: -12px; left: -12px; width: 24px; height: 24px;
      background: #0f0; color: #000; border-radius: 50%; font-weight: bold; text-align: center;
      line-height: 24px; cursor: pointer; border: 2px solid #000; box-shadow: 0 0 10px #0f0a; z-index: 100000; }
    #ffscan.collapsed { height: 30px; overflow: hidden; }
    #ffscan.collapsed *:not(.toggle) { display: none !important; }
  `;
  document.head.appendChild(style);

  const box = document.createElement("div");
  box.id = "ffscan";
  box.innerHTML = `
    <div class="toggle" title="Toggle">–</div>
    <h1 id="ff-header">FlaskFinder by TRHACKNON<br>Chargement...</h1>
    <textarea id="ff-words">${paths.join("\n")}</textarea>
    <input type="file" id="ff-file" accept=".txt">
    <button id="ff-scan">Scan</button>
    <button id="ff-export-json">Export JSON</button>
    <button id="ff-export-csv">Export CSV</button>
    <div id="ff-output"></div>
    <div class="console"><b>Detected:</b> <span id="ff-detected">–</span></div>
    <div class="footer">by <span style="color:#f0f">trhacknon</span> – for educational use</div>
  `;
  document.body.appendChild(box);

  document.querySelector(".toggle").onclick = () => box.classList.toggle("collapsed");
  document.getElementById("ff-scan").onclick = scan;
  document.getElementById("ff-export-json").onclick = exportJSON;
  document.getElementById("ff-export-csv").onclick = exportCSV;
  document.getElementById("ff-file").onchange = e => loadFile(e.target.files[0]);

  async function updateHeaderWithInfo() {
    try {
      const res = await fetch("https://api.ipify.org?format=json");
      const data = await res.json();
      const ip = data.ip;
      const now = new Date();
      const date = now.toLocaleDateString();
      const time = now.toLocaleTimeString();
      document.getElementById("ff-header").innerHTML = `FlaskFinder by TRHACKNON<br>${date} ${time} – IP: ${ip}`;
    } catch {
      document.getElementById("ff-header").innerHTML = `FlaskFinder by TRHACKNON<br>Impossible d'obtenir l'IP`;
    }
  }
  await updateHeaderWithInfo();

  async function scan() {
    results.length = 0;
    detectedSigns.clear();
    const output = document.getElementById("ff-output");
    output.innerHTML = "";
    const entries = document.getElementById("ff-words").value.split("\n").map(e => e.trim()).filter(Boolean);
    const base = window.location.origin;
    for (const path of entries) {
      const url = base + path;
      try {
        const res = await fetch(url);
        const type = res.headers.get("Content-Type") || "";
        const server = res.headers.get("Server") || "";
        const body = await res.text();

        if (server.toLowerCase().includes("werkzeug")) detectedSigns.add("Flask (Werkzeug header)");
        if (/flask|werkzeug|traceback|Exception/i.test(body) && res.status === 500) detectedSigns.add("Flask (500 error stack)");
        if (type.includes("json") && /\"message\"|\"error\"|\"code\"/i.test(body)) detectedSigns.add("Flask-like API");

        const line = document.createElement("div");
        line.className = `res status-${res.status}`;
        line.textContent = `[${res.status}] ${path}`;
        output.appendChild(line);

        results.push({ path, status: res.status, contentType: type, server, snippet: body.slice(0, 100).replace(/\s+/g, " ") });
      } catch {
        const errLine = document.createElement("div");
        errLine.className = "res status-0";
        errLine.textContent = `[ERR] ${path}`;
        output.appendChild(errLine);
      }
    }
    document.getElementById("ff-detected").innerText = [...detectedSigns].join(", ") || "Unknown";
    console.log("[FlaskFinder] Results:", results);
  }

  function exportJSON() {
    const blob = new Blob([JSON.stringify(results, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `flaskfinder_${Date.now()}.json`;
    a.click();
  }

  function exportCSV() {
    const header = "path,status,contentType,server,snippet";
    const rows = results.map(r => `"${r.path}","${r.status}","${r.contentType}","${r.server}","${r.snippet.replace(/"/g, '""')}"`);
    const csv = [header, ...rows].join("\n");
    const blob = new Blob([csv], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `flaskfinder_${Date.now()}.csv`;
    a.click();
  }

  function loadFile(file) {
    const reader = new FileReader();
    reader.onload = () => {
      const lines = reader.result.split("\n").map(e => e.trim()).filter(Boolean);
      document.getElementById("ff-words").value = lines.join("\n");
    };
    reader.readAsText(file);
  }
})();
