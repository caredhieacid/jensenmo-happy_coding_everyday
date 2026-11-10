const list = document.getElementById('tasks');
const form = document.getElementById('new-task');
const error = document.getElementById('error');

function render(tasks) {
  list.replaceChildren(...tasks.map((task) => {
    const row = document.createElement('tr');
    const title = document.createElement('td');
    title.textContent = task.title;
    row.append(title);
    return row;
  }));
}

async function load() {
  const response = await fetch('/api/tasks');
  render((await response.json()).tasks);
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  error.textContent = '';
  const response = await fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: form.title.value }),
  });
  if (!response.ok) {
    error.textContent = (await response.json()).error;
    return;
  }
  form.reset();
  load();
});

load();
