
const API_BASE = "http://127.0.0.1:8000";
let token = localStorage.getItem("churn_v2_token") || null;

const loginCard = document.getElementById("loginCard");
const appCard = document.getElementById("appCard");
const loginForm = document.getElementById("loginForm");
const loginError = document.getElementById("loginError");
const logoutBtn = document.getElementById("logoutBtn");

const authHeaders = () => token ? { "Authorization": "Bearer " + token } : {};

function showApp() { loginCard.classList.add("hidden"); appCard.classList.remove("hidden"); }
function showLogin() { appCard.classList.add("hidden"); loginCard.classList.remove("hidden"); }
if (token) showApp(); else showLogin();

loginForm?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(loginForm).entries());
  const res = await fetch(API_BASE + "/auth/login", {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data)
  });
  if (!res.ok) { loginError.classList.remove("hidden"); return; }
  const out = await res.json();
  token = out.access_token;
  localStorage.setItem("churn_v2_token", token);
  loginError.classList.add("hidden");
  showApp();
});

logoutBtn?.addEventListener("click", () => { localStorage.removeItem("churn_v2_token"); token = null; showLogin(); });

const pct = (x) => (100 * x).toFixed(1) + "%";
function setRiskBadge(prob) {
  const badge = document.getElementById("risk");
  badge.className = "badge";
  if (prob >= 0.65) badge.classList.add("high");
  else if (prob >= 0.4) badge.classList.add("medium");
  else badge.classList.add("low");
  badge.textContent = badge.classList.contains("high") ? "High" : badge.classList.contains("medium") ? "Medium" : "Low";
}

document.getElementById("singleForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const payload = Object.fromEntries(new FormData(e.target).entries());
  ["SeniorCitizen","tenure","MonthlyCharges","TotalCharges"].forEach(k => payload[k] = Number(payload[k]));
  const res = await fetch(API_BASE + "/predict", {
    method:"POST", headers: { "Content-Type":"application/json", ...authHeaders() }, body: JSON.stringify(payload)
  });
  if (!res.ok) { alert("Prediction failed. Are you logged in and are artifacts trained?"); return; }
  const out = await res.json();
  document.getElementById("prob").textContent = pct(out.churn_probability);
  setRiskBadge(out.churn_probability);
  const ul = document.getElementById("reasons"); ul.innerHTML = "";
  const bars = document.getElementById("reasonBars"); bars.innerHTML = "";
  const impacts = out.top_reasons.map(r => Math.abs(r.impact)); const maxAbs = Math.max(...impacts, 1);
  out.top_reasons.forEach(r => { const li=document.createElement("li"); li.textContent = `${r.feature} (${r.direction})`; ul.appendChild(li);
    const b=document.createElement("div"); b.className="bar"; const inner=document.createElement("div"); inner.style.width = Math.round(100*Math.abs(r.impact)/maxAbs)+'%'; b.appendChild(inner); bars.appendChild(b); });
  const actions = document.getElementById("actions"); actions.innerHTML = ""; out.recommendations.forEach(a => { const li=document.createElement("li"); li.textContent=a; actions.appendChild(li); });
  document.getElementById("singleResult").classList.remove("hidden");
});

document.getElementById("uploadBtn").addEventListener("click", async () => {
  const f = document.getElementById("csvFile").files[0];
  if (!f) return alert("Choose a CSV file first.");
  const fd = new FormData(); fd.append("file", f);
  const res = await fetch(API_BASE + "/predict_batch", { method:"POST", headers: { ...authHeaders() }, body: fd });
  if (!res.ok) { alert("Batch prediction failed. Check login and CSV columns."); return; }
  const out = await res.json();
  const ex = document.getElementById("batchExamples");
  ex.innerHTML = "<h4>Examples</h4>" + out.summary_examples.map(e => `<div class='card'><b>Row ${e.row_index}</b>: ${pct(e.churn_probability)} (${e.risk})<br/>Reasons: ${e.top_reasons.map(r => r.feature).join(", ")}<br/>Actions: ${e.recommendations.join("; ")}</div>`).join("");
  ex.classList.remove("hidden");
  const tw = document.getElementById("tableWrapper"); const rows = out.preview_rows;
  if (rows && rows.length) { const cols = Object.keys(rows[0]); let html = "<table><thead><tr>" + cols.map(c => `<th>${c}</th>`).join("") + "</tr></thead><tbody>";
    rows.forEach(r => { html += "<tr>" + cols.map(c => `<td>${r[c]}</td>`).join("") + "</tr>"; }); html += "</tbody></table>"; tw.innerHTML = html; tw.classList.remove("hidden"); }
});

const insightsBtn = document.getElementById("insightsBtn"); const modal = document.getElementById("insightsModal");
insightsBtn.addEventListener("click", async (e) => {
  e.preventDefault();
  const res = await fetch(API_BASE + "/insights", { headers: { ...authHeaders() } });
  if (!res.ok) { alert("Load insights failed. Are you logged in?"); return; }
  const out = await res.json();
  const list = document.getElementById("insightsList"); list.innerHTML = "";
  out.top_features.forEach(x => { const row = document.createElement("div"); row.textContent = `${x.feature}: ${x.importance.toFixed(4)}`; list.appendChild(row); });
  modal.showModal();
});
