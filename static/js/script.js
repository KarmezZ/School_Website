const collapsibles = document.querySelectorAll(".collapsible");
collapsibles.forEach((item) =>
  item.addEventListener("click", function () {
    this.classList.toggle("collapsible--expanded");
  })
);

// slider
const slides = document.querySelectorAll(".slides img");
const nextButton = document.getElementById("slider-next-button");
const previousButton = document.getElementById("slider-previous-button");
let slideIndex = 0;
let intervalId = null;
initSlider();
function initSlider() {
  if (slides.length > 0) {
    slides[slideIndex].classList.add("display-slide");
    intervalId = setInterval(nextSlide, 4000);
  }
}
function showSlide(index) {
  if (index >= slides.length) {
    slideIndex = 0;
  } else if (index < 0) {
    slideIndex = slides.length - 1;
  }

  slides.forEach((slide) => {
    slide.classList.remove("display-slide");
  });
  slides[slideIndex].classList.add("display-slide");
}

function prevSlide() {
  clearInterval(intervalId);
  slideIndex--;
  showSlide(slideIndex);
}
function nextSlide() {
  clearInterval(intervalId);
  slideIndex++;
  showSlide(slideIndex);
}

nextButton.addEventListener("click", function () {
  nextSlide();
});
previousButton.addEventListener("click", function () {
  prevSlide();
});
