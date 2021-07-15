const menuBtn = document.querySelector('.menu-btn');
// ..hamburger to "x" animation
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('open');
});

// ..hamburger Function
function openMenu() {
    let nav = document.querySelector('.mobile-nav');
    if (nav.style.display === "block") {
        nav.style.display = "none";
    } else {
        nav.style.display = "block";
    }
}

// display review reply form
$('.reply').click(function(){
    let review_id = $(this).attr('review_id');
    $(".comment_" + review_id).css("display", "block");
})

// display status reply form
$('.reply').click(function(){
    let status_id = $(this).attr('status_id');
    $(".comment_" + status_id).css("display", "block");
})

//display "edit Profile" modal
$('#edit-profile').click(function(){
    $('.edit-profile-modal').css("display", "block");
})

//close "Edit Profile" modal
$('#close').click(function(){
    $('.edit-profile-modal').css("display", "none");
})

// select profile image
$('.img-container img').click(function(){
    $('.img-container img').css("outline", "none");
    $(this).css("outline", "5px solid #86b7fe");
    let image = $(this).attr('id');
    $('#img').val(image);
})

//select profile color
$('.img-container span').click(function(){
    $('.img-container span').css("outline", "none");
    $(this).css("outline", "5px solid #86b7fe");
    let color = $(this).attr('color');
    $('#color').val(color);
})