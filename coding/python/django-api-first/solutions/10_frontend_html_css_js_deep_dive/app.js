const FALLBACK_ROWS = [
  { learner: "Amina", source: "web", score: 97, status: "accepted" },
  { learner: "Jon", source: "mobile", score: 88, status: "queued" },
  { learner: "Rhea", source: "partner", score: 92, status: "accepted" },
];

const refreshButton = document.querySelector("#refresh-button");
const statusEl = document.querySelector("#health-status");
const form = document.querySelector("#subscriber-form");
const messageEl = document.querySelector("#subscriber-message");
const tableBody = document.querySelector("#submission-table-body");

function renderRows(rows) {
  tableBody.innerHTML = rows
    .map(
      (row) => `
        <tr>
          <td>${row.learner}</td>
          <td>${row.source}</td>
          <td>${row.score}</td>
          <td>${row.status}</td>
        </tr>
      `,
    )
    .join("");
}

async function fetchHealth() {
  await new Promise((resolve) => setTimeout(resolve, 120));
  return { status: "ok", checkedAt: "2024-09-01T09:30:00Z" };
}

function setHealthState(kind, text) {
  statusEl.className = `pill pill--${kind}`;
  statusEl.textContent = text;
}

function validateEmail(value) {
  return value.includes("@") && value.includes(".");
}

refreshButton.addEventListener("click", async () => {
  setHealthState("loading", "Refreshing health...");
  try {
    const payload = await fetchHealth();
    setHealthState("ok", `${payload.status.toUpperCase()} · ${payload.checkedAt}`);
  } catch (error) {
    setHealthState("error", "ERROR · health check failed");
  }
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const email = new FormData(form).get("email")?.toString() ?? "";
  messageEl.textContent = validateEmail(email)
    ? `Looks good, ${email}. Django can now POST this to /api/v1/subscribers/.`
    : "Enter a valid email so the browser and serializer agree on validation.";
});

renderRows(FALLBACK_ROWS);
refreshButton.click();
