

function openModal() {
    document.getElementById('my-modal').style.display = "inline-flex"; //changes display property

    // hide scrollbnar when image viewer is opened
    document.body.style.overflow = "hidden";

}

function closeModal() {
    document.getElementById('my-modal').style.display = "none"; //changes display property

    // hide scrollbnar when image viewer is opened
    document.body.style.overflow = "auto";

}

//declare our slide index variable
var slideIndexJS = 1;

// Calling the showSlides by passing the variable slide index, hiding all images initially
showSlides(slideIndexJS)

function changeSlides(n) {
    showSlides(slideIndexJS += n); // incremented by what our function calls
}

// Displays inmage whose thumbnail was clicked
function currentSlide(n) {
    showSlides(slideIndexJS = n);
}

//Main function for image viewer
function showSlides(n) {
    var i;

    // get all elemnets with class .my-slides
    var slidesJS = document.getElementsByClassName("my-slides");

    // If the slideIndexJS is greater than total no of images open first image
    if (n > slidesJS.length) { slideIndexJS = 1; }

    if (n < 1) { slideIndexJS = slideIndexJS.length; }

    // hide all images
    for (i = 0; i < slidesJS.length; i++) {
        slidesJS[i].style.display = "none";
    }

    // Show the images whose thumbnail is clicked
    slidesJS[slideIndexJS - 1].style.display = "block";

    // show index numbers 
    document.getElementByID('index-number').innerHTML = slidesJS[slideIndexJS - 1].getAttribute('data-index-number');
    var imagesJS = document.getElementsByClassName("image");
    document.getElementById('caption').innerHTML = imagesJS[slideIndexJS - 1].alt;
}

function messageSent() {
    alert("Your message has been sent!");
}


