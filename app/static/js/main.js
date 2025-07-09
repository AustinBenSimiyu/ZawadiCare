// Mobile menu toggle
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

menuBtn.addEventListener('click', () => {
  const expanded = menuBtn.getAttribute('aria-expanded') === 'true';
  menuBtn.setAttribute('aria-expanded', !expanded);
  mobileMenu.classList.toggle('hidden');
  if (!expanded) {
    // Focus first link in mobile menu
    const firstLink = mobileMenu.querySelector('a');
    if (firstLink) firstLink.focus();
  }
});

document.addEventListener('keydown', (e) => {
  if (!mobileMenu.classList.contains('hidden')) {
    if (e.key === 'Escape') {
      mobileMenu.classList.add('hidden');
      menuBtn.setAttribute('aria-expanded', 'false');
      menuBtn.focus();
    }
    // Focus trap
    const focusableEls = mobileMenu.querySelectorAll('a');
    if (focusableEls.length > 0) {
      const firstEl = focusableEls[0];
      const lastEl = focusableEls[focusableEls.length - 1];
      if (e.key === 'Tab') {
        if (e.shiftKey && document.activeElement === firstEl) {
          e.preventDefault();
          lastEl.focus();
        } else if (!e.shiftKey && document.activeElement === lastEl) {
          e.preventDefault();
          firstEl.focus();
        }
      }
    }
  }
});

// About Section Image Slider

document.addEventListener('DOMContentLoaded', function() {
  const sliderImgs = document.querySelectorAll('#about-slider .slider-img');
  const sliderDots = document.querySelectorAll('#about-slider .slider-dot');
  const sliderPrev = document.getElementById('slider-prev');
  const sliderNext = document.getElementById('slider-next');
  let sliderIndex = 0;
  let autoPlayInterval = null;

  function showSliderImage(idx) {
    sliderImgs.forEach((img, i) => {
      img.style.opacity = i === idx ? '1' : '0';
      img.style.zIndex = i === idx ? '1' : '0';
      img.setAttribute('aria-hidden', i === idx ? 'false' : 'true');
    });
    sliderDots.forEach((dot, i) => {
      dot.classList.toggle('bg-pink-400', i === idx);
      dot.classList.toggle('bg-pink-200', i !== idx);
    });
  }

  function nextSliderImage() {
    sliderIndex = (sliderIndex + 1) % sliderImgs.length;
    showSliderImage(sliderIndex);
  }

  function prevSliderImage() {
    sliderIndex = (sliderIndex - 1 + sliderImgs.length) % sliderImgs.length;
    showSliderImage(sliderIndex);
  }

  function startAutoPlay() {
    if (autoPlayInterval) clearInterval(autoPlayInterval);
    autoPlayInterval = setInterval(() => {
      nextSliderImage();
    }, 4000);
  }

  function resetAutoPlay() {
    startAutoPlay();
  }

  if (sliderPrev && sliderNext && sliderImgs.length > 0) {
    sliderPrev.addEventListener('click', () => {
      prevSliderImage();
      resetAutoPlay();
    });
    sliderNext.addEventListener('click', () => {
      nextSliderImage();
      resetAutoPlay();
    });
    sliderDots.forEach((dot, i) => {
      dot.addEventListener('click', () => {
        sliderIndex = i;
        showSliderImage(sliderIndex);
        resetAutoPlay();
      });
    });
    showSliderImage(sliderIndex);
    startAutoPlay();
  }
}); 