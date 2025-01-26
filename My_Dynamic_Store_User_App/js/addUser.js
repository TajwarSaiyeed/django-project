const addUserResult = document.getElementById("addUserResult");

const handleAddUser = (event) => {
  event.preventDefault();

  const form = event.target;
  const username = form.username.value;
  const email = form.email.value;
  const password = form.password.value;
  const city = form.city.value;
  const street = form.street.value;
  const phone = form.phone.value;
  const firstname = form.firstname.value;
  const lastname = form.lastname.value;

  const user = {
    username,
    email,
    password,
    address: {
      city,
      street,
    },
    phone,
    name: {
      firstname,
      lastname,
    },
  };

  fetch("https://fakestoreapi.com/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  })
    .then((res) => res.json())
    .then((json) => {
      addUserResult.innerHTML = `
        ${JSON.stringify(json, null, 2)}
      `;
    });
};
