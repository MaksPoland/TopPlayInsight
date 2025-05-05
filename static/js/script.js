document.addEventListener('DOMContentLoaded', function() {
    // Table of Contents Functionality
    const tocTabs = document.querySelectorAll('.toc-tab');
    const progressBar = document.querySelector('.toc-progress-bar');
    
    if (tocTabs.length > 0 && progressBar) {
        // Set initial active tab
        const firstTab = tocTabs[0];
        firstTab.classList.add('active');
        
        // Tab click handling
        tocTabs.forEach((tab, index) => {
            tab.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Remove active class from all tabs
                tocTabs.forEach(t => t.classList.remove('active'));
                
                // Add active class to clicked tab
                tab.classList.add('active');
                
                // Update progress bar based on tab index
                const progressWidth = ((index + 1) / tocTabs.length) * 100;
                progressBar.style.width = `${progressWidth}%`;
                
                // Optional: Scroll to section
                const targetId = tab.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 100,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // Add ID anchors to the relevant sections if they don't exist
        const sections = ['best-casinos', 'casino-categories', 'new-casinos', 'bonuses'];
        sections.forEach(sectionId => {
            if (!document.getElementById(sectionId)) {
                const sectionContainer = document.createElement('div');
                sectionContainer.id = sectionId;
                document.querySelector('.casino-listings').prepend(sectionContainer);
            }
        });
    }
    
    // Mobile navigation toggle
    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarToggler) {
        navbarToggler.addEventListener('click', function() {
            const navbarCollapse = document.querySelector('.navbar-collapse');
            navbarCollapse.classList.toggle('show');
        });
    }

    // Form validation for contact form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            let isValid = true;
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const messageInput = document.getElementById('message');
            
            // Simple validation
            if (!nameInput.value.trim()) {
                showError(nameInput, 'Please enter your name');
                isValid = false;
            } else {
                removeError(nameInput);
            }
            
            if (!emailInput.value.trim()) {
                showError(emailInput, 'Please enter your email');
                isValid = false;
            } else if (!isValidEmail(emailInput.value.trim())) {
                showError(emailInput, 'Please enter a valid email address');
                isValid = false;
            } else {
                removeError(emailInput);
            }
            
            if (!messageInput.value.trim()) {
                showError(messageInput, 'Please enter your message');
                isValid = false;
            } else {
                removeError(messageInput);
            }
            
            if (isValid) {
                // Show success message (in a real app, this would submit the form)
                const successMessage = document.createElement('div');
                successMessage.className = 'alert alert-success mt-3';
                successMessage.role = 'alert';
                successMessage.textContent = 'Your message has been sent. We\'ll get back to you soon!';
                
                contactForm.reset();
                contactForm.parentNode.insertBefore(successMessage, contactForm.nextSibling);
                
                // Remove success message after 5 seconds
                setTimeout(() => {
                    successMessage.remove();
                }, 5000);
            }
        });
    }
    
    // Validate email format
    function isValidEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }
    
    // Show error message
    function showError(input, message) {
        const formGroup = input.closest('.form-group');
        const errorMessage = formGroup.querySelector('.invalid-feedback') || document.createElement('div');
        
        errorMessage.className = 'invalid-feedback d-block';
        errorMessage.textContent = message;
        
        if (!formGroup.querySelector('.invalid-feedback')) {
            formGroup.appendChild(errorMessage);
        }
        
        input.classList.add('is-invalid');
    }
    
    // Remove error message
    function removeError(input) {
        const formGroup = input.closest('.form-group');
        const errorMessage = formGroup.querySelector('.invalid-feedback');
        
        if (errorMessage) {
            errorMessage.remove();
        }
        
        input.classList.remove('is-invalid');
    }

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
