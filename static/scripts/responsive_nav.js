// Responsive Menu
const menuIcon = document.getElementById("menu-icon");
const nav = document.querySelector(".nav");
const logo = document.querySelector(".logo");

// resize logo

if (window.innerWidth < 700) {
  logo.style.width = "40%";
}

if (nav.style.display === "block") {
  nav.style.display = "none";
} else {
  nav.style.display = "block";
}
if (nav.style.display === "block") {
  nav.style.display = "none";
} else {
  nav.style.display = "block";
}

menuIcon.addEventListener("click", () => {
  if (nav.style.display === "block") {
    nav.style.display = "none";
  } else {
    nav.style.display = "block";
  }
});
