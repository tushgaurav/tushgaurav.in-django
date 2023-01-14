// Responsive Menu
const menuIcon = document.getElementById("menu-icon");
const nav = document.querySelector(".nav");

menuIcon.addEventListener("click", () => {
  if (nav.style.display === "block") {
    nav.style.display = "none";
  } else {
    nav.style.display = "block";
  }
});
