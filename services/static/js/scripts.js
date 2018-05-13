let navbar = document.getElementById("insta-navbar");

let height = navbar.offsetHeight;
let difference = height;

document.body.style.paddingTop = difference + "px";

window.onscroll = function() {
    let distance = window.scrollY;
    console.log(distance , " ", height);
    if(distance > difference - height) {
        navbar.classList.add("insta-navbar_scroll");
    } else {
        navbar.classList.remove("insta-navbar_scroll");
    }
};