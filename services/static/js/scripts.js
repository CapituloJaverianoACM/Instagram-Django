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

let image_container = $("#upload-image");

if(image_container) {
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                image_container.attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#image_input").change(function(){
        readURL(this);
    });

}