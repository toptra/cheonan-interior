/* ============================================
   대우나이 인테리어 - Main JavaScript
   Vanilla JS (no jQuery dependency)
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {

  // ============================================
  // Header scroll effect
  // ============================================
  const header = document.getElementById('header');
  let lastScroll = 0;

  window.addEventListener('scroll', function() {
    const currentScroll = window.scrollY;
    if (currentScroll > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    lastScroll = currentScroll;
  });

  // ============================================
  // Mobile menu toggle
  // ============================================
  const menuToggle = document.getElementById('menuToggle');
  const navLinks = document.getElementById('navLinks');

  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', function() {
      menuToggle.classList.toggle('active');
      navLinks.classList.toggle('open');
    });

    // Close menu on link click
    navLinks.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        menuToggle.classList.remove('active');
        navLinks.classList.remove('open');
      });
    });
  }

  // ============================================
  // Hero Slider
  // ============================================
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');
  let currentSlide = 0;
  let slideInterval;

  function goToSlide(index) {
    slides.forEach(function(s) { s.classList.remove('active'); });
    dots.forEach(function(d) { d.classList.remove('active'); });
    slides[index].classList.add('active');
    dots[index].classList.add('active');
    currentSlide = index;
  }

  function nextSlide() {
    var next = (currentSlide + 1) % slides.length;
    goToSlide(next);
  }

  function startSlider() {
    slideInterval = setInterval(nextSlide, 2000);
  }

  function resetSlider() {
    clearInterval(slideInterval);
    startSlider();
  }

  if (slides.length > 0) {
    dots.forEach(function(dot) {
      dot.addEventListener('click', function() {
        goToSlide(parseInt(this.dataset.slide));
        resetSlider();
      });
    });
    startSlider();
  }

  // ============================================
  // Scroll animations (Intersection Observer)
  // ============================================
  var animatedElements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -40px 0px'
    });

    animatedElements.forEach(function(el) {
      observer.observe(el);
    });
  } else {
    // Fallback for older browsers
    animatedElements.forEach(function(el) {
      el.classList.add('visible');
    });
  }

  // ============================================
  // Portfolio filter
  // ============================================
  var filterBtns = document.querySelectorAll('.filter-btn');
  var portfolioItems = document.querySelectorAll('.portfolio-item');

  filterBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var filter = this.dataset.filter;

      filterBtns.forEach(function(b) { b.classList.remove('active'); });
      this.classList.add('active');

      portfolioItems.forEach(function(item) {
        if (filter === 'all' || item.dataset.category === filter) {
          item.style.display = '';
          item.style.opacity = '0';
          setTimeout(function() { item.style.opacity = '1'; }, 50);
        } else {
          item.style.opacity = '0';
          setTimeout(function() { item.style.display = 'none'; }, 300);
        }
      });
    });
  });

  // ============================================
  // Smooth scroll for anchor links
  // ============================================
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var headerHeight = header ? header.offsetHeight : 0;
        var targetPos = target.getBoundingClientRect().top + window.scrollY - headerHeight;
        window.scrollTo({ top: targetPos, behavior: 'smooth' });
      }
    });
  });

  // ============================================
  // Back to top button
  // ============================================
  var btnTop = document.getElementById('btnTop');

  if (btnTop) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 600) {
        btnTop.classList.add('visible');
      } else {
        btnTop.classList.remove('visible');
      }
    });
  }

  // ============================================
  // Active nav link on scroll
  // ============================================
  var sections = document.querySelectorAll('section[id]');
  var navLinksAll = document.querySelectorAll('.nav-links a:not(.nav-cta)');

  function updateActiveNav() {
    var scrollPos = window.scrollY + 150;

    sections.forEach(function(section) {
      var top = section.offsetTop;
      var height = section.offsetHeight;
      var id = section.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        navLinksAll.forEach(function(link) {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', updateActiveNav);

});

// ============================================
// Contact form handler
// ============================================
function handleSubmit(e) {
  e.preventDefault();

  var form = e.target;
  var formData = {
    name: form.querySelector('#name').value,
    phone: form.querySelector('#phone').value,
    type: form.querySelector('#type').value,
    budget: form.querySelector('#budget').value,
    message: form.querySelector('#message').value
  };

  // 무료버전: 간단한 알림 후 메일 전송 또는 외부 폼 연동
  // 유료버전에서는 API 호출로 DB 저장
  var subject = encodeURIComponent('[상담신청] ' + formData.name + ' 님 상담 요청');
  var body = encodeURIComponent(
    '이름: ' + formData.name + '\n' +
    '연락처: ' + formData.phone + '\n' +
    '인테리어 종류: ' + formData.type + '\n' +
    '예상 예산: ' + formData.budget + '\n' +
    '상담 내용: ' + formData.message
  );

  // mailto 방식 (무료버전 기본)
  window.location.href = 'mailto:info@daewoonai.com?subject=' + subject + '&body=' + body;

  alert('상담 신청이 접수되었습니다. 빠른 시일 내에 연락드리겠습니다.');
  form.reset();
}

// ============================================
// Ad inquiry form handler (Google Sheets 연동)
// ============================================
function handleAdSubmit(e) {
  e.preventDefault();
  var form = e.target;
  var submitBtn = form.querySelector('button[type="submit"]');
  var name = form.querySelector('#ad-name').value;
  var phone = form.querySelector('#ad-phone').value;
  var company = form.querySelector('#ad-company').value;
  var message = form.querySelector('#ad-message').value;

  submitBtn.disabled = true;
  submitBtn.textContent = '전송 중...';

  var SHEET_URL = 'https://script.google.com/macros/s/AKfycbwMxMNgP2iyiXUeLLbuxZey_5lGgWgiwqFPtfNQomUqvBKtTQ3M3Ao3oLnrz7ip3A8R/exec';
  var params = '?name=' + encodeURIComponent(name) +
    '&phone=' + encodeURIComponent(phone) +
    '&company=' + encodeURIComponent(company) +
    '&message=' + encodeURIComponent(message);

  fetch(SHEET_URL + params, { method: 'GET', mode: 'no-cors' })
    .then(function() {
      alert('입점 신청이 완료되었습니다!\n빠른 시일 내에 연락드리겠습니다.');
      form.reset();
      submitBtn.disabled = false;
      submitBtn.textContent = '입점 신청하기';
    })
    .catch(function() {
      alert('전송 중 오류가 발생했습니다.\n전화로 문의해 주세요: 010-8672-3426');
      submitBtn.disabled = false;
      submitBtn.textContent = '입점 신청하기';
    });
}
