const getUserId = document.getElementById("getUserId");
const getUserBtn = document.getElementById("getUserBtn");
const singleUserResult = document.getElementById("singleUserResult");

const fetchUserById = () => {
  fetch(`https://fakestoreapi.com/users/${parseInt(getUserId.value)}`)
    .then((res) => res.json())
    .then((json) => {
      singleUserResult.innerHTML = "";

      const div = document.createElement("div");
      div.classList.add("bg-white", "p-4", "rounded-lg", "shadow-md");

      div.innerHTML = `
        <h2 class="text-xl font-semibold">${json.name.firstname} ${json.name.lastname}</h2>
        <p><strong>Email:</strong> ${json.email}</p>
        <p><strong>Username:</strong> ${json.username}</p>
        <p><strong>Phone:</strong> ${json.phone}</p>
        <p><strong>Address:</strong> ${json.address.street}, ${json.address.city}, ${json.address.zipcode}</p>
        <p><strong>Geolocation:</strong> Lat: ${json.address.geolocation.lat}, Long: ${json.address.geolocation.long}</p>
      `;

      singleUserResult.appendChild(div);
    });
};

getUserBtn.addEventListener("click", fetchUserById);
