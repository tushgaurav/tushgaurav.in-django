import { Application } from "@splinetool/runtime";

const canvas = document.getElementById("canvas3d");
canvas.style.maxHeight = "50%";

canvas.style.width = "100%";
canvas.style.maxWidth = "1000px";

const app = new Application(canvas);
app.load("https://prod.spline.design/sPNFXvkM5t-R8qn5/scene.splinecode");
