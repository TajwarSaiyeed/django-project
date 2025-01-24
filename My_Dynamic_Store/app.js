const productListElement = document.getElementById("product-list");
const productDetailsElement = document.getElementById("product-details");
const categoryListElement = document.getElementById("category-list");

const fetchProducts = (category = "all") => {
  let url = `https://fakestoreapi.com/products`;
  if (category !== "all") {
    url = `https://fakestoreapi.com/products/category/${category}`;
  }

  fetch(url)
    .then((response) => response.json())
    .then((products) => displayProducts(products));
};

const fetchCategories = () => {
  fetch(`https://fakestoreapi.com/products/categories`)
    .then((response) => response.json())
    .then((categories) => displayCategories(categories));
};

const fetchProductDetails = (productId) => {
  fetch(`https://fakestoreapi.com/products/${productId}`)
    .then((response) => response.json())
    .then((product) => displayProductDetails(product));
};

const displayProducts = (products) => {
  productListElement.innerHTML = "";
  products.forEach((product) => {
    const productCard = document.createElement("div");
    productCard.classList.add("product-card");

    productCard.innerHTML = `
            <img src="${product.image}" alt="${product.title}">
            <h3>${product.title}</h3>
            <p>$${product.price}</p>
            <button><a target="_blank" href="product-details.html?id=${product.id}">View Details</a></button
        `;
    productListElement.appendChild(productCard);
  });
};

const displayCategories = (categories) => {
  categories.forEach((category) => {
    const listItem = document.createElement("li");
    const link = document.createElement("a");
    link.href = "#";
    link.style.textTransform = "capitalize";
    link.textContent = category;
    link.addEventListener("click", (event) => {
      event.preventDefault();
      const selectedCategory = event.target.textContent;
      fetchProducts(selectedCategory);
    });
    listItem.appendChild(link);
    categoryListElement.appendChild(listItem);
  });
};

const displayProductDetails = (product) => {
  productDetailsElement.innerHTML = `
    <div class="product-details-container">
        <div class="product-image-container">
            <img src="${product.image}" alt="${product.title}" style="max-width: 100%; max-height: 300px;">
        </div>
        <div class="product-text-container">
            <h2>${product.title}</h2>
            <p><strong>Description:</strong> ${product.description}</p>
            <p><strong>Price:</strong> $${product.price}</p>
            <p><strong>Category:</strong> ${product.category}</p>
        </div>
    </div>
    `;
};


fetchProducts();
fetchCategories();
