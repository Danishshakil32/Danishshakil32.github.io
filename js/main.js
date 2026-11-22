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

// Image Modal Slider functionality
window.currentModalImages = [];
window.currentModalIndex = 0;
window.currentModalCaption = "";

window.openModal = function(imageSrcArray, caption) {
    const modal = document.getElementById('image-modal');
    if(!modal) return;
    
    // Convert single string to array if needed
    window.currentModalImages = Array.isArray(imageSrcArray) ? imageSrcArray : [imageSrcArray];
    window.currentModalIndex = 0;
    window.currentModalCaption = caption;
    
    updateModalView();
    modal.style.display = 'block';
    
    // Show/hide arrows based on array length
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    if (window.currentModalImages.length > 1) {
        if(prevBtn) prevBtn.style.display = 'block';
        if(nextBtn) nextBtn.style.display = 'block';
    } else {
        if(prevBtn) prevBtn.style.display = 'none';
        if(nextBtn) nextBtn.style.display = 'none';
    }
};

window.updateModalView = function() {
    const imgElement = document.getElementById('modal-img');
    const captionElement = document.getElementById('modal-caption');
    const counterElement = document.getElementById('modal-counter');
    
    if (imgElement && window.currentModalImages.length > 0) {
        imgElement.src = window.currentModalImages[window.currentModalIndex];
    }
    if (captionElement) {
        captionElement.innerText = Array.isArray(window.currentModalCaption) ? (window.currentModalCaption[window.currentModalIndex] || "") : window.currentModalCaption;
    }
    if (counterElement && window.currentModalImages.length > 1) {
        counterElement.innerText = "Image " + (window.currentModalIndex + 1) + " of " + window.currentModalImages.length;
    } else if (counterElement) {
        counterElement.innerText = "";
    }
}

window.changeSlide = function(direction) {
    window.currentModalIndex += direction;
    if (window.currentModalIndex >= window.currentModalImages.length) {
        window.currentModalIndex = 0; // wrap to first
    } else if (window.currentModalIndex < 0) {
        window.currentModalIndex = window.currentModalImages.length - 1; // wrap to last
    }
    updateModalView();
}

window.closeModal = function() {
    const modal = document.getElementById('image-modal');
    if(modal) {
        modal.style.display = 'none';
    }
};

// Close modal when clicking outside of image
document.addEventListener('click', function(event) {
    const modal = document.getElementById('image-modal');
    if(modal && modal.style.display === 'block') {
        if(event.target === modal || event.target.classList.contains('modal-slider-container')) {
            closeModal();
        }
    }
});
// FYP gallery: opens the shared modal at a given image with per-image captions
window.openFypGallery = function(startIndex) {
    const dir = 'data/Projects/fyp-refrigerator-insulation/';
    const items = [
        ['project-approach.png', 'Two-stage approach: A4 foam samples, then PEL refrigerator cabinets'],
        ['emat-daq-chain.png', 'EMAT data-acquisition chain'],
        ['a4-scanner-cad.png', 'A4 sample scanner, CAD model (one motorized axis + one manual axis)'],
        ['cabinet-scanner-top.png', 'U-shaped cabinet scanner, top view with EMAT probes'],
        ['cabinet-scanner-iso.png', 'U-shaped cabinet scanner around a refrigerator cabinet']
    ];
    window.openModal(items.map(i => dir + i[0]), items.map(i => i[1]));
    window.currentModalIndex = startIndex || 0;
    window.updateModalView();
};
