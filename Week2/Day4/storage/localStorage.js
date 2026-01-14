// storage/localStorage.js
const STORAGE_KEY = "todos";

export function saveTodos(todos) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
  } catch (err) {
    logError(err);
  }
}

export function loadTodos() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  } catch (err) {
    logError(err);
    return [];
  }
}

function logError(error) {
  console.error(error);
}
