var prevScrollPos = window.pageYOffset || document.documentElement.scrollTop;
var navbar = document.querySelector('.header-section');
var isScrolling = false;
var timeout;

function toggleNavbar() {
  var currentScrollPos = window.pageYOffset || document.documentElement.scrollTop;
  if (currentScrollPos === 0) {
    navbar.classList.remove('hidden');
  } else if (prevScrollPos > currentScrollPos) {
    navbar.classList.remove('hidden');
  } else {
    navbar.classList.add('hidden');
  }
  prevScrollPos = currentScrollPos;
  isScrolling = false;
}

function handleScroll() {
  if (!isScrolling) {
    isScrolling = true;
    navbar.classList.remove('hidden');
  }

  clearTimeout(timeout);
  timeout = setTimeout(function() {
    isScrolling = false;
    toggleNavbar();
  }, 500); // Adjust the delay (in milliseconds) as desired
}

window.addEventListener('scroll', handleScroll);

