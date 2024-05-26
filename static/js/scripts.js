
/// for navigation ///// Execute scrollFunction when the window is scrolled
window.onscroll = function() {
  scrollFunction();
};

// Function to handle scrolling behavior
function scrollFunction() {
  const scrollPosition = window.scrollY || document.documentElement.scrollTop;

  // Select the navigation element with class 'fixed-nav'
  const navElement = document.querySelector('.fixed-nav');

  // Add or remove the 'scroll' class based on scroll position
  if (scrollPosition > 50) {
    navElement.classList.add('scroll');
  } else {
    navElement.classList.remove('scroll');
  }
}

// Smooth scrolling when clicking on navigation links
document.querySelectorAll('.fixed-nav a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();

    const targetId = this.getAttribute('href').substring(1);
    const targetSection = document.getElementById(targetId);

    if (targetSection) {
      // Calculate the offset relative to the top of the document
      const offsetTop = targetSection.getBoundingClientRect().top + window.scrollY;

      // Scroll to the target section with smooth behavior
      window.scrollTo({
        top: offsetTop,
        behavior: 'smooth'
      });
    }
  });
});

// Linking about
window.onload = function() {
  const aboutSection = document.getElementById('about-section');
  if (aboutSection) {
    aboutSection.scrollIntoView({ behavior: 'smooth' });
  }
};


