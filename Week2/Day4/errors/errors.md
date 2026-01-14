# Error Log

## 1. Invalid JSON in LocalStorage
**Where:** loadTodos()  
**Error Message:** Unexpected token n in JSON at position 0  
**Cause:** LocalStorage key `todos` contained corrupted (non-JSON) data  
**Fix:** Wrapped `JSON.parse()` in try/catch and returned an empty array as fallback  

---

## 2. Null DOM Element Reference
**Where:** renderTodos()  
**Error Message:** Cannot set properties of null (setting 'innerHTML')  
**Cause:** `<ul id="todo-list">` was missing from `index.html`  
**Fix:** Restored the missing DOM element and added a null guard check  

---

## 3. Uncaught ReferenceError
**Where:** app.js  
**Error Message:** notDefinedVariable is not defined  
**Cause:** Attempted to log a variable that was never declared  
**Fix:** Removed the invalid reference and verified variable scope  
