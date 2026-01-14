import { saveTodos, loadTodos } from "./storage/localStorage.js";

let todos = loadTodos();

const input = document.querySelector("#todo-input");
const list = document.querySelector("#todo-list");

function renderTodos() {
  list.innerHTML = "";

  todos.forEach((todo) => {
    const li = document.createElement("li");
    li.textContent = todo.text;

    if (todo.completed) {
      li.classList.add("completed");
    }

    li.onclick = () => toggleTodo(todo.id);

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "❌";
    deleteBtn.onclick = (e) => {
      e.stopPropagation();
      deleteTodo(todo.id);
    };
    const editBtn = document.createElement("button");
    editBtn.textContent = "✏️";
    editBtn.onclick = (e) => {
      e.stopPropagation();
      editTodo(todo.id);
    };

    li.appendChild(editBtn);

    li.appendChild(deleteBtn);
    list.appendChild(li);
  });
}

function addTodo(text) {
  todos.push({ id: Date.now(), text, completed: false });
  saveTodos(todos);
  renderTodos();
}

function toggleTodo(id) {
  todos = todos.map((t) =>
    t.id === id ? { ...t, completed: !t.completed } : t
  );
  saveTodos(todos);
  renderTodos();
}
function editTodo(id) {
  const todo = todos.find((t) => t.id === id);
  if (!todo) return;

  const newText = prompt("Edit todo:", todo.text);

  if (newText === null) return;

  const trimmed = newText.trim();
  if (!trimmed) return;

  todo.text = trimmed;
  saveTodos(todos);
  renderTodos();
}

function deleteTodo(id) {
  todos = todos.filter((t) => t.id !== id);
  saveTodos(todos);
  renderTodos();
}

input.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && input.value.trim()) {
    addTodo(input.value.trim());
    input.value = "";
  }
});

renderTodos();
