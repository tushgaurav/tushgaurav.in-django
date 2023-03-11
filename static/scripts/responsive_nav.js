// Responsive Menu
const menuIcon = document.getElementById("menu-icon");
const nav = document.querySelector(".nav");

if (window.innerWidth < 700) {
  nav.style.display == "none";
}

menuIcon.addEventListener("click", () => {
  if (nav.style.display === "block") {
    nav.style.display = "none";
  } else {
    nav.style.display = "block";
  }
});
