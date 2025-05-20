document.getElementById("password-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  console.log("🔐 Form submitted");

  const password = document.getElementById("password").value;
  const spinner = document.getElementById("loading");
  const results = document.getElementById("results");

  spinner.classList.remove("hidden");
  results.classList.add("hidden");

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password }),
    });

    const data = await response.json();
    console.log("📦 Data from backend:", data);

    document.getElementById("strength").textContent = data.strength;
    document.getElementById("entropy").textContent = data.entropy;
    document.getElementById("crack-time").textContent = data.crack_time;
    document.getElementById("suggestions").textContent = data.suggestions.join(", ");

    const crackedResult = document.getElementById("cracked-result");
    const crackedPassword = document.getElementById("cracked-password");

    if (crackedResult && crackedPassword) {
      crackedResult.textContent = data.cracked_by_jtr ? "Yes" : "No";
      crackedPassword.textContent = data.cracked_password || "-";
      console.log("✅ Cracked password inserted into DOM");
    } else {
      console.warn("⚠️ Could not find cracked-result or cracked-password in DOM");
    }

    const strengthBar = document.getElementById("strength-bar-fill");
    strengthBar.className = "";

    if (data.strength.toLowerCase() === "weak") {
      strengthBar.classList.add("weak");
      strengthBar.style.width = "33%";
    } else if (data.strength.toLowerCase() === "medium") {
      strengthBar.classList.add("medium");
      strengthBar.style.width = "66%";
    } else if (data.strength.toLowerCase() === "strong") {
      strengthBar.classList.add("strong");
      strengthBar.style.width = "100%";
    } else {
      strengthBar.style.width = "0%";
    }

    spinner.classList.add("hidden");
    results.classList.remove("hidden");
    results.style.display = "block";

  } catch (err) {
    console.error("❌ Error during analysis:", err);
    spinner.classList.add("hidden");
    alert("An error occurred during analysis.");
  }
});

document.getElementById("toggle-password").addEventListener("click", function () {
  const input = document.getElementById("password");
  const icon = this.querySelector("i");
  const isPassword = input.type === "password";
  input.type = isPassword ? "text" : "password";
  icon.className = isPassword ? "fas fa-eye-slash" : "fas fa-eye";
});

