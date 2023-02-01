import { Application } from "@splinetool/runtime";

const canvas = document.getElementById("canvas3d");
canvas.style.maxHeight = "50%";

const app = new Application(canvas);
app.load("https://prod.spline.design/sPNFXvkM5t-R8qn5/scene.splinecode");
