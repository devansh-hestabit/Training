// Mobile menu toggle
const mobileMenu = document.getElementById("mobileMenu");
const navLinks = document.getElementById("navLinks");

mobileMenu.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

// Fetch and display categories
async function fetchCategories() {
  try {
    const response = await fetch("https://dummyjson.com/products?limit=0");
    const data = await response.json();

    // Update stats
    document.getElementById("productCount").textContent = data.total;

    // Group products by category
    const categoriesMap = {};
    data.products.forEach((product) => {
      if (!categoriesMap[product.category]) {
        categoriesMap[product.category] = {
          name: product.category,
          count: 0,
          image: product.thumbnail,
        };
      }
      categoriesMap[product.category].count++;
    });

    const categories = Object.values(categoriesMap);
    document.getElementById("categoryCount").textContent = categories.length;

    // Render categories
    renderCategories(categories);
  } catch (error) {
    console.error("Error fetching categories:", error);
    document.getElementById("categoriesGrid").innerHTML = `
                    <p style="text-align: center; color: #e53e3e;">Failed to load categories. Please try again later.</p>
                `;
  }
}

function renderCategories(categories) {
  const container = document.getElementById("categoriesGrid");

  const categoryEmojis = {
    beauty: "💄",
    fragrances: "🌸",
    furniture: "🛋️",
    groceries: "🛒",
    "home-decoration": "🏠",
    "kitchen-accessories": "🍳",
    laptops: "💻",
    "mens-shirts": "👕",
    "mens-shoes": "👞",
    "mens-watches": "⌚",
    "mobile-accessories": "📱",
    motorcycle: "🏍️",
    "skin-care": "✨",
    smartphones: "📲",
    "sports-accessories": "⚽",
    sunglasses: "🕶️",
    tablets: "📱",
    tops: "👚",
    vehicle: "🚗",
    "womens-bags": "👜",
    "womens-dresses": "👗",
    "womens-jewellery": "💎",
    "womens-shoes": "👠",
    "womens-watches": "⌚",
  };

  container.innerHTML = categories
    .map((category) => {
      const emoji = categoryEmojis[category.name] || "🏷️";
      const formattedName = category.name
        .split("-")
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ");

      return `
                    <div class="category-card" onclick="goToCategory('${category.name}')">
                        <div class="category-badge">${category.count} Items</div>
                        <img 
                            src="${category.image}" 
                            alt="${formattedName}"
                            class="category-image"
                            onerror="this.style.background='linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%)'"
                        >
                        <div class="category-content">
                            <div class="category-title">${emoji} ${formattedName}</div>
                            <div class="category-count">Explore ${category.count} products</div>
                        </div>
                    </div>
                `;
    })
    .join("");
}

function goToCategory(categoryName) {
  window.location.href = `products.html?category=${categoryName}`;
}
window.goToCategory = goToCategory;

fetchCategories();
