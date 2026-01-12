# Week 2, Day 1: Advanced HTML & Accessibility
## 🧠 Key Learnings & Concepts

### 1. HTML Page Structure

I learned how a complete HTML document should be structured, including:

- `<!DOCTYPE html>` for HTML5
- `<html lang="en">` for language declaration
- Proper separation of `<head>` (metadata) and `<body>` (content)
- Use of metadata such as:
  - `charset`
  - `viewport`
  - `description`
  - `canonical`
  - `theme-color`

**Fact:**  
Search engines and assistive technologies rely heavily on correct metadata.

---

### 2. Semantic HTML5 (No `<div>`-Based Layouts)

I learned how to structure a webpage using **meaningful semantic elements**, such as:

- `<header>` for page headers
- `<nav>` for navigation menus
- `<main>` for the primary content
- `<section>` for grouped content
- `<article>` for independent content
- `<aside>` for sidebar content
- `<footer>` for site information

**Fact:**  
Semantic HTML improves:
- Accessibility
- SEO
- Code readability
- Maintainability

---

### 3. Accessibility & ARIA

I learned how to make content usable for screen readers and keyboard users.

Accessibility features implemented:

- Skip-to-content link
- Proper heading hierarchy (`h1` → `h6`)
- Meaningful `alt` text for images
- Associated `<label>` elements for all form inputs
- Keyboard-friendly navigation
- ARIA attributes such as:
  - `aria-label`
  - `aria-describedby`
  - `aria-live`

**Important Rule Learned:**  
> ARIA should only be used when native HTML semantics are not sufficient.

---

### 4. Forms & Native Validation

I learned how to build forms using **HTML-only validation**, including:

- `required`
- `type="email"`, `type="url"`, `type="search"`
- `minlength` / `maxlength`
- `placeholder` vs labels (labels are always required)
- Grouping inputs with `<fieldset>` and `<legend>`

Forms implemented:
- Search form
- Newsletter subscription
- Comment submission
- Contact form

**Fact:**  
HTML can handle many validation tasks without JavaScript.

---

### 5. Media Embedding

I learned how to embed different types of media accessibly:

- Images using `<figure>` and `<figcaption>`
- Videos with:
  - Multiple formats (`mp4`, `webm`)
- Audio with fallback content

**Accessibility Consideration:**  
Captions and transcripts are essential for inclusive media.

---

### 6. Structured Data (Schema.org)

I used **microdata attributes** to describe content meaningfully:

- `BlogPosting`
- `Person`
- `Comment`
- `Organization`
- `PostalAddress`

**Fact:**  
Structured data helps search engines better understand and display content through rich results.

---

## ⚠️ Challenges & Difficulties Faced

### 1. Overusing ARIA

Initially, I added ARIA roles to many elements unnecessarily.  
I learned that semantic HTML already provides accessibility and that excessive ARIA can cause issues.

**Solution:**  
Removed redundant ARIA roles and relied on native HTML elements first.

---

### 2. Form Accessibility

Understanding when to use:
- Visible `<label>`
- `aria-label`

**Solution:**  
Ensured every input had a visible label and only used ARIA when additional clarification was needed.

---

### 3. Large File Organization

As the project grew, the HTML file became large and harder to manage.

**Solution:**  
Used clear comments, consistent indentation, and logical section grouping.
