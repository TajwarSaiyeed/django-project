const loginResult = document.getElementById("loginResult");

const handleLogin = (event) => {
  event.preventDefault();
  const form = event.target;
  const username = form.username.value;
  const password = form.password.value;

  console.log({
    username,
    password,
  });


  fetch("https://fakestoreapi.com/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      password,
    }),
  })
    .then((res) => res.json())
    .then((json) => {
      loginResult.innerHTML = `
        ${JSON.stringify(json, null, 2)}
      `;
    })
};
