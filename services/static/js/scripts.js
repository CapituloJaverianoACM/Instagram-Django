let navbar = document.getElementById("insta-navbar");

let height = navbar.offsetHeight;
let difference = height;

document.body.style.paddingTop = difference + "px";

window.onscroll = function() {
    let distance = window.scrollY;
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


let doLikes = $(".insta-do-like");

doLikes.on('click', function() {
    let item = $(this);
    let data = {};
    data["post_id"] = item.attr("postid");
    let url = "/dislike/"
    let like = item.hasClass("fa-heart-o");
    let target = $(item.attr("target"));
    console.log(item.attr("target"));

    if(like) {
        url = "/like/";
    }

    $.ajax({
        type: "POST",
        data: data,
        url: url,
        success: function(e) {
            console.log(e);
            item.toggleClass("fa-heart-o");
            item.toggleClass("fa-heart");
            target.html(e.likes_count);
        }
    });
});











