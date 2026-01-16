let allProducts = [];
let filteredProducts = [];
let selectedCategory = "all";

// Get category from URL if present
const urlParams = new URLSearchParams(window.location.search);
const urlCategory = urlParams.get("category");
if (urlCategory) {
  selectedCategory = urlCategory;
}

// Mobile menu toggle
const mobileMenu = document.getElementById("mobileMenu");
const navLinks = document.getElementById("navLinks");

mobileMenu.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

// Category emojis
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

// Fetch ALL products from API
async function fetchProducts() {
  try {
    const response = await fetch("https://dummyjson.com/products?limit=0");
    const data = await response.json();
    allProducts = data.products;
    filteredProducts = allProducts;

    // Create category pills
    createCategoryPills();

    // Filter and render
    filterAndSortProducts();
  } catch (error) {
    console.error("Error fetching products:", error);
    document.getElementById("productsContainer").innerHTML = `
                    <div class="no-results">
                        <p>⚠️ Failed to load products. Please try again later.</p>
                    </div>
                `;
  }
}

// Create category filter pills
function createCategoryPills() {
  const categories = [...new Set(allProducts.map((p) => p.category))].sort();
  const pillsContainer = document.getElementById("categoryPills");

  let pillsHTML = `<div class="category-pill ${
    selectedCategory === "all" ? "active" : ""
  }" onclick="filterByCategory('all', this)">

                🌟 All Products
            </div>`;

  categories.forEach((category) => {
    const emoji = categoryEmojis[category] || "🏷️";
    const formattedName = category
      .split("-")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ");

    pillsHTML += `<div class="category-pill ${
      selectedCategory === category ? "active" : ""
    }" onclick="filterByCategory('${category}', this)">

                    ${emoji} ${formattedName}
                </div>`;
  });

  pillsContainer.innerHTML = pillsHTML;
}

// Filter by category
function filterByCategory(category, el) {
  selectedCategory = category;

  // Update active pill
  document.querySelectorAll(".category-pill").forEach((pill) => {
    pill.classList.remove("active");
  });
  el.classList.add("active");

  // Update URL
  if (category !== "all") {
    window.history.pushState({}, "", `?category=${category}`);
  } else {
    window.history.pushState({}, "", "products.html");
  }

  filterAndSortProducts();
}

// Render products by category
function renderProducts(products) {
  const container = document.getElementById("productsContainer");

  if (products.length === 0) {
    container.innerHTML = `
                    <div class="no-results">
                        <p>😕 No products found matching your criteria.</p>
                    </div>
                `;
    return;
  }

  // Group products by category
  const groupedProducts = {};
  products.forEach((product) => {
    if (!groupedProducts[product.category]) {
      groupedProducts[product.category] = [];
    }
    groupedProducts[product.category].push(product);
  });

  // Sort categories alphabetically
  const sortedCategories = Object.keys(groupedProducts).sort();

  // Render each category section
  let html = "";
  sortedCategories.forEach((category) => {
    const categoryProducts = groupedProducts[category];
    const emoji = categoryEmojis[category] || "🏷️";
    const formattedName = category
      .split("-")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ");

    html += `
                    <div class="category-section">
                        <div class="category-header">
                            <div class="category-title">
                                <span class="category-title-emoji">${emoji}</span>
                                <div>
                                    <div>${formattedName}</div>
                                    <div class="category-count">${
                                      categoryProducts.length
                                    } products</div>
                                </div>
                            </div>
                        </div>
                        <div class="products-grid">
                            ${categoryProducts
                              .map(
                                (product) => `
                                <div class="product-card">
                                    <img 
                                        src="${product.thumbnail}" 
                                        alt="${product.title}"
                                        class="product-image"
                                        onerror="this.src='https://via.placeholder.com/300x250?text=No+Image'"
                                    >
                                    <div class="product-info">
                                        <span class="product-category">${
                                          categoryEmojis[product.category] ||
                                          "🏷️"
                                        } ${product.category.replace(
                                  /-/g,
                                  " "
                                )}</span>
                                        <h3 class="product-title">${
                                          product.title
                                        }</h3>
                                        <p class="product-description">${
                                          product.description
                                        }</p>
                                        <div class="product-footer">
                                            <span class="product-price">$${
                                              product.price
                                            }</span>
                                            <span class="product-rating">
                                                ⭐ ${product.rating.toFixed(1)}
                                            </span>
                                        </div>
                                        <button class="add-to-cart" onclick="addToCart(${
                                          product.id
                                        })">
                                            Add to Cart
                                        </button>
                                    </div>
                                </div>
                            `
                              )
                              .join("")}
                        </div>
                    </div>
                `;
  });

  container.innerHTML = html;
}

// Update product count
function updateProductCount(count) {
  const countElement = document.getElementById("productCount");
  countElement.textContent = `Showing ${count} product${
    count !== 1 ? "s" : ""
  }`;
}

// Filter and sort products
function filterAndSortProducts() {
  let result = [...allProducts];

  // Apply category filter
  if (selectedCategory !== "all") {
    result = result.filter((p) => p.category === selectedCategory);
  }

  // Apply search filter
  const searchTerm = document.getElementById("searchInput").value.toLowerCase();
  if (searchTerm) {
    result = result.filter(
      (product) =>
        product.title.toLowerCase().includes(searchTerm) ||
        product.description.toLowerCase().includes(searchTerm) ||
        product.category.toLowerCase().includes(searchTerm)
    );
  }

  // Apply sorting
  const sortValue = document.getElementById("sortSelect").value;
  applySorting(result, sortValue);

  filteredProducts = result;
  renderProducts(filteredProducts);
  updateProductCount(filteredProducts.length);
}

// Search functionality
const searchInput = document.getElementById("searchInput");
searchInput.addEventListener("input", () => {
  filterAndSortProducts();
});

// Sort functionality
const sortSelect = document.getElementById("sortSelect");
sortSelect.addEventListener("change", () => {
  filterAndSortProducts();
});

function applySorting(products, sortValue) {
  switch (sortValue) {
    case "high-to-low":
      products.sort((a, b) => b.price - a.price);
      break;
    case "low-to-high":
      products.sort((a, b) => a.price - b.price);
      break;
    case "rating-high":
      products.sort((a, b) => b.rating - a.rating);
      break;
    case "name-asc":
      products.sort((a, b) => a.title.localeCompare(b.title));
      break;
    case "name-desc":
      products.sort((a, b) => b.title.localeCompare(a.title));
      break;
  }
}

// Add to cart function
function addToCart(productId) {
  const product = allProducts.find((p) => p.id === productId);
  if (product) {
    alert(`"${product.title}" has been added to your cart! 🛒`);
  }
}
window.filterByCategory = filterByCategory;
window.addToCart = addToCart;

// Initialize
fetchProducts();
