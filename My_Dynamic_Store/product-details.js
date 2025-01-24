const getProductDetails = () => {
  const productId = new URLSearchParams(window.location.search).get("id");

  fetch(`https://fakestoreapi.com/products/${productId}`)
    .then((response) => response.json())
    .then((product) => displayProductDetails(product))
};

const displayProductDetails = (product) => {
  const productDetailsElement = document.getElementById("product-details");
  productDetailsElement.innerHTML = `
        <img src="${product.image}" alt="${product.title}">
        <h2>${product.title}</h2>
        <p><strong>Price:</strong> $${product.price}</p>
        <p><strong>Description:</strong> ${product.description}</p>
        <p><strong>Category:</strong> ${product.category}</p>
    `;
};


document.addEventListener("DOMContentLoaded", getProductDetails);
