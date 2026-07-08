const form = document.querySelector("#scan-form");
const result = document.querySelector("#result");
const riskLevel = document.querySelector("#risk-level");
const riskScore = document.querySelector("#risk-score");
const button = form.querySelector("button");

function cleanPayload(payload) {
  return Object.fromEntries(
    Object.entries(payload)
      .map(([key, value]) => [key, value.trim()])
      .filter(([, value]) => value.length > 0)
  );
}

function setResult(data) {
  const level = data.risk_level || "waiting";
  riskLevel.textContent = level;
  riskLevel.className = `badge ${level}`;
  riskScore.textContent = Number(data.risk_score || 0).toFixed(2);
  result.textContent = JSON.stringify(data, null, 2);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  button.disabled = true;
  button.textContent = "Scanning...";

  const payload = cleanPayload({
    text: document.querySelector("#text").value,
    url: document.querySelector("#url").value,
    web: document.querySelector("#web").value,
  });

  try {
    const response = await fetch("/api/v1/scan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    setResult(response.ok ? data : { risk_score: 0, risk_level: "low", error: data });
  } catch (error) {
    setResult({ risk_score: 0, risk_level: "low", error: String(error) });
  } finally {
    button.disabled = false;
    button.textContent = "Scan";
  }
});
