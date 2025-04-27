// Validate email format
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Show error message
function showError(input, message) {
    const formGroup = input.parentElement;
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message text-danger mt-1';
    errorDiv.textContent = message;
    
    // Remove any existing error message
    removeError(input);
    
    // Add the new error message
    formGroup.appendChild(errorDiv);
    input.classList.add('is-invalid');
}

// Remove error message
function removeError(input) {
    const formGroup = input.parentElement;
    const errorDiv = formGroup.querySelector('.error-message');
    
    if (errorDiv) {
        formGroup.removeChild(errorDiv);
    }
    
    input.classList.remove('is-invalid');
}

// Contact form validation
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            let isValid = true;
            
            // Get form elements
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const subjectInput = document.getElementById('subject');
            const messageInput = document.getElementById('message');
            
            // Validate name
            if (nameInput.value.trim() === '') {
                showError(nameInput, 'Please enter your name');
                isValid = false;
            } else {
                removeError(nameInput);
            }
            
            // Validate email
            if (emailInput.value.trim() === '') {
                showError(emailInput, 'Please enter your email');
                isValid = false;
            } else if (!isValidEmail(emailInput.value)) {
                showError(emailInput, 'Please enter a valid email address');
                isValid = false;
            } else {
                removeError(emailInput);
            }
            
            // Validate subject
            if (subjectInput.value.trim() === '') {
                showError(subjectInput, 'Please enter a subject');
                isValid = false;
            } else {
                removeError(subjectInput);
            }
            
            // Validate message
            if (messageInput.value.trim() === '') {
                showError(messageInput, 'Please enter your message');
                isValid = false;
            } else {
                removeError(messageInput);
            }
            
            // If valid, show success message
            if (isValid) {
                const alertDiv = document.createElement('div');
                alertDiv.className = 'alert alert-success mt-3';
                alertDiv.textContent = 'Your message has been sent successfully! We will get back to you soon.';
                
                const formContainer = document.querySelector('.contact-form');
                formContainer.insertBefore(alertDiv, contactForm);
                
                // Reset form
                contactForm.reset();
                
                // Remove success message after 5 seconds
                setTimeout(function() {
                    formContainer.removeChild(alertDiv);
                }, 5000);
            }
        });
    }
    
    // Casino filters functionality
    const filterBadges = document.querySelectorAll('.filter-badges .badge');
    
    if (filterBadges.length > 0) {
        filterBadges.forEach(badge => {
            badge.addEventListener('click', function() {
                // Remove active class from all badges
                filterBadges.forEach(b => b.classList.remove('bg-primary'));
                filterBadges.forEach(b => b.classList.add('bg-light', 'text-dark'));
                
                // Add active class to clicked badge
                this.classList.remove('bg-light', 'text-dark');
                this.classList.add('bg-primary');
                
                // Filter casinos based on category
                const category = this.textContent.trim().toLowerCase();
                const casinoItems = document.querySelectorAll('.casino-list-item');
                
                casinoItems.forEach(item => {
                    if (category === 'all casinos') {
                        item.style.display = 'block';
                    } else if (category === 'new casinos' && item.classList.contains('new-casino')) {
                        item.style.display = 'block';
                    } else if (category === 'featured casinos' && item.classList.contains('featured-casino')) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
    }
});