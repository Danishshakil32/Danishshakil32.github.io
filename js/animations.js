// js/animations.js

document.addEventListener('DOMContentLoaded', () => {
    
    // Intersection Observer for reveal elements
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Unobserve after animating once
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(el => observer.observe(el));

    // Stats counter animation
    const statsObserverOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };

    const animateValue = (obj, start, end, duration, decimals) => {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            
            // Ease out cubic
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            
            let currentVal = (easeProgress * (end - start) + start);
            if (decimals > 0) {
                obj.innerHTML = currentVal.toFixed(decimals);
            } else {
                obj.innerHTML = Math.floor(currentVal);
            }
            
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                obj.innerHTML = decimals > 0 ? end.toFixed(decimals) : end;
            }
        };
        window.requestAnimationFrame(step);
    };

    const statsObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const targetVal = parseFloat(entry.target.getAttribute('data-target'));
                const decimals = parseInt(entry.target.getAttribute('data-decimal')) || 0;
                animateValue(entry.target, 0, targetVal, 2000, decimals);
                observer.unobserve(entry.target);
            }
        });
    }, statsObserverOptions);

    const statNumbers = document.querySelectorAll('.stat-number[data-target]');
    statNumbers.forEach(el => statsObserver.observe(el));
    
    // Timeline node pulse effect when in view
    const timelineNodes = document.querySelectorAll('.timeline-node');
    timelineNodes.forEach(el => observer.observe(el)); // Will add 'visible' class
});
