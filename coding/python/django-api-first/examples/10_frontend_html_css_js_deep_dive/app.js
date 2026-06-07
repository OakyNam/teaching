const MOCK_SUBMISSIONS = [
  { source: "web", learner: "Amina", score: 97 },
  { source: "mobile", learner: "Jon", score: 88 },
  { source: "partner", learner: "Rhea", score: 92 },
];

const statusText = document.querySelector("#status-text");
const refreshButton = document.querySelector("#refresh-button");
const signupForm = document.querySelector("#signup-form");
const formMessage = document.querySelector("#form-message");
const submissionRows = document.querySelector("#submission-rows");

async function loadHealth() {
  await new Promise((resolve) => setTimeout(resolve, 120));
  return { status: "ok", checkedAt: "2024-09-01T09:30:00Z" };
}

function renderHealth(payload) {
  statusText.textContent = `${payload.status.toUpperCase()} · checked ${payload.checkedAt}`;
  statusText.className = `status-pill status-pill--${payload.status}`;
}

function renderRows(rows) {
  submissionRows.innerHTML = rows
    .map(
      (row) => `
        <tr>
          <td>${row.source}</td>
          <td>${row.learner}</td>
          <td>${row.score}</td>
        </tr>
      `,
    )
    .join("");
}

function validateEmail(value) {
  return value.includes("@") && value.includes(".");
}

async function refreshStatus() {
  statusText.textContent = "Refreshing...";
  statusText.className = "status-pill status-pill--loading";
  try {
    renderHealth(await loadHealth());
  } catch (error) {
    statusText.textContent = "ERROR · failed to load API health";
    statusText.className = "status-pill status-pill--error";
  }
}

signupForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const email = new FormData(signupForm).get("email")?.toString() ?? "";
  formMessage.textContent = validateEmail(email)
    ? `Thanks, ${email}. We would POST this to /api/v1/subscribers/.`
    : "Enter a real email so the backend serializer can validate it too.";
});

refreshButton.addEventListener("click", refreshStatus);
renderRows(MOCK_SUBMISSIONS);
refreshStatus();
