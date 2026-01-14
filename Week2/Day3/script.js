const questions = document.querySelectorAll(".faq-question");

questions.forEach(question => {
  question.addEventListener("click", () => {
    const item = question.parentElement;

    // Close others
    document.querySelectorAll(".faq-item").forEach(faq => {
      if (faq !== item) {
        faq.classList.remove("active");
        faq.querySelector(".icon").textContent = "+";
      }
    });

    // Toggle current
    item.classList.toggle("active");

    const icon = question.querySelector(".icon");
    icon.textContent = item.classList.contains("active") ? "−" : "+";
  });
});
