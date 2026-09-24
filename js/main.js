// js/main.js

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Header scroll effect
    const header = document.getElementById('site-header');
    const backToTop = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
            if(backToTop) backToTop.style.opacity = '1';
        } else {
            header.classList.remove('scrolled');
            if(backToTop) backToTop.style.opacity = '0';
        }
    });

    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.getElementById('main-nav');

    if (mobileMenuBtn && mainNav) {
        mobileMenuBtn.addEventListener('click', () => {
            const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
            mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
            mainNav.classList.toggle('open');
            
            // Toggle icon
            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                icon.setAttribute('data-lucide', isExpanded ? 'menu' : 'x');
                lucide.createIcons();
            }
        });
    }

    // Close mobile menu on link click
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (mainNav.classList.contains('open')) {
                mainNav.classList.remove('open');
                mobileMenuBtn.setAttribute('aria-expanded', 'false');
                const icon = mobileMenuBtn.querySelector('i');
                if (icon) {
                    icon.setAttribute('data-lucide', 'menu');
                    lucide.createIcons();
                }
            }
        });
    });

    // Back to Top
    if(backToTop) {
        backToTop.style.opacity = '0';
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
