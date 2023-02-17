// animate only on the homepage
if (page == "homepage") {
  animateSidebar(2);
  animateHero(0.5, 3);
}

// animation for the sidebar
function animateSidebar(duration) {
  gsap.from("body", {
    opacity: 0,
    duration: duration - 1,
  });

  gsap.from(".sidebar", {
    width: "100vw",
    duration: duration,
    ease: "circ.out",
  });

  gsap.from(".logo", {
    scale: 4,
    duration: duration - 1,
    yPercent: 50,
    xPercent: 50,
  });

  gsap.from(".nav", {
    opacity: 0,
    delay: duration,
    duration: 0.2,
  });

  gsap.from(".nav-link", {
    x: -200,
    opacity: 0,
    delay: duration + 0.2,
    stagger: 0.2,
  });
}

// animation for the hero section (homepage)
function animateHero(duration, delay) {
  gsap.from(".branding", {
    opacity: 0,
    scale: 0,
    duration: duration,
    delay: delay - 2,
  });

  gsap.from(".hero-image", {
    rotation: 360,
    duration: duration,
    delay: delay - 1,
    scale: 0,
  });

  gsap.from(".button-container", {
    scale: 0,
    opacity: 0,
    duration: duration,
    delay: delay - 1,
  });

  gsap.from(".bio", {
    xPercent: 20,
    scale: 0,
    opacity: 0,
    duration: duration,
    delay: delay - 1,
  });
}

const p2 = document.querySelector(".p2");
const words = [
  "DESIGNER",
  "DEVELOPER",
  "CREATIVE",
  "ARCHITECH",
  "ENGINEER",
  "ARTISAN",
  "WIZARD",
];
let wordIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < words[wordIndex].length) {
    p2.textContent += words[wordIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, 50);
  } else {
    setTimeout(erase, 2000);
  }
}

function erase() {
  if (charIndex > 0) {
    p2.textContent = words[wordIndex].substring(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 10);
  } else {
    wordIndex++;
    if (wordIndex >= words.length) {
      wordIndex = 0;
    }
    setTimeout(type, 50);
  }
}

type();
