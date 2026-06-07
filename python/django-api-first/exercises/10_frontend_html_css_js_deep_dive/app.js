const STARTER_ROWS = [
  { learner: "Amina", source: "web", score: 97 },
  { learner: "Jon", source: "mobile", score: 88 },
  { learner: "Rhea", source: "partner", score: 92 },
  { learner: "Noah", source: "web", score: 84 },
];

const form = document.querySelector("#filter-form");
const queryInput = document.querySelector("#query");
const message = document.querySelector("#filter-message");
const resultsBody = document.querySelector("#results-body");

function renderRows(rows) {
  if (!rows.length) {
    resultsBody.innerHTML = '<tr><td colspan="3">No matching learners found.</td></tr>';
    return;
  }

  resultsBody.innerHTML = rows
    .map(
      (row) => `
        <tr>
          <td>${row.learner}</td>
          <td>${row.source}</td>
          <td>${row.score}</td>
        </tr>
      `,
    )
    .join("");
}

function filterRows(query) {
  const normalized = query.trim().toLowerCase();
  return STARTER_ROWS.filter((row) => row.learner.toLowerCase().includes(normalized));
}

function describeRows(rows) {
  return rows.map((row) => `${row.learner} from ${row.source}`).join(", ");
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const query = queryInput.value;
  const rows = query ? filterRows(query) : STARTER_ROWS;
  renderRows(rows);
  message.textContent = rows.length
    ? `Showing ${rows.length} matching learner(s): ${describeRows(rows)}.`
    : "No learners matched. Update the data source or try a new query.";
});

renderRows(STARTER_ROWS);
