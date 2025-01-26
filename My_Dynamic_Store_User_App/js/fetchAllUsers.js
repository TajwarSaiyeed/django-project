const getAllUsersBtn = document.getElementById("getAllUsersBtn");
const allUsersResult = document.getElementById("allUsersResult");

const fetchAllUsers = () => {
  fetch("https://fakestoreapi.com/users")
    .then((res) => res.json())
    .then((json) => {
      allUsersResult.innerHTML = "";

      json.forEach((user) => {
        const div = document.createElement("div");
        div.classList.add(
          "bg-white",
          "p-4",
          "mb-4",
          "rounded-lg",
          "shadow-md"
        );

        div.innerHTML = `
          <h2 class="text-xl font-semibold">${user.name.firstname} ${user.name.lastname}</h2>
          <p><strong>Email:</strong> ${user.email}</p>
          <p><strong>Phone:</strong> ${user.phone}</p>
          <p><strong>Address:</strong> ${user.address.street}, ${user.address.city}</p>
          <p><strong>Username:</strong> ${user.username}</p>
        `;

        allUsersResult.appendChild(div);
      });
    });
};

getAllUsersBtn.addEventListener("click", fetchAllUsers);
