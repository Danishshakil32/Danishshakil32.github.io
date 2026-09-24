// js/form.js

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const formResult = document.getElementById('form-result');
    const submitBtn = document.getElementById('submit-btn');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Basic validation
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (!name || !email || !message) {
                showResult('Please fill in all required fields.', 'var(--copper)');
                return;
            }

            // Submit text
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = 'Sending... <i data-lucide="loader" class="spinner"></i>';
            if (typeof lucide !== 'undefined') lucide.createIcons();
            submitBtn.disabled = true;

            const formData = new FormData(contactForm);

            // Fetch to Web3Forms API
            fetch('https://api.web3forms.com/submit', {
                method: 'POST',
                body: formData
            })
            .then(async (response) => {
                let json = await response.json();
                if (response.status == 200) {
                    showResult('Message sent successfully! I will get back to you soon.', 'var(--cyan)');
                    contactForm.reset();
                } else {
                    console.log(response);
                    showResult(json.message || 'Something went wrong. Please try again.', 'var(--copper)');
                }
            })
            .catch(error => {
                console.log(error);
                showResult('Something went wrong. Please try again.', 'var(--copper)');
            })
            .finally(() => {
                submitBtn.innerHTML = originalBtnText;
                if (typeof lucide !== 'undefined') lucide.createIcons();
                submitBtn.disabled = false;
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    formResult.style.display = 'none';
                }, 5000);
            });
        });
    }

    function showResult(text, color) {
        formResult.style.display = 'block';
        formResult.style.color = color;
        formResult.innerHTML = text;
    }
});
