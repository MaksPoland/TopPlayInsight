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

// Casino filtering and sorting functionality
document.addEventListener('DOMContentLoaded', function() {
    // Filter badges functionality
    const filterBadges = document.querySelectorAll('.filter-badges .badge');
    if (filterBadges.length > 0) {
        filterBadges.forEach(badge => {
            badge.addEventListener('click', function() {
                // Toggle active class
                if (this.classList.contains('badge-active')) {
                    this.classList.remove('badge-active');
                    this.classList.add('bg-light');
                    this.classList.add('text-dark');
                } else {
                    // Reset all badges first
                    filterBadges.forEach(b => {
                        b.classList.remove('badge-active');
                        b.classList.add('bg-light');
                        b.classList.add('text-dark');
                    });
                    
                    // Set active badge
                    this.classList.add('badge-active');
                    this.classList.remove('bg-light');
                    this.classList.remove('text-dark');
                }
                
                filterCasinos();
            });
        });
    }
    
    // Sort dropdown functionality
    const sortSelect = document.querySelector('.casino-filters .form-select');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            sortCasinos(this.value);
        });
    }
    
    // Function to filter casinos
    function filterCasinos() {
        const activeBadge = document.querySelector('.filter-badges .badge-active');
        const casinoItems = document.querySelectorAll('.casino-list-item');
        
        if (!activeBadge) {
            // Show all casinos if no filter is active
            casinoItems.forEach(item => {
                item.style.display = 'block';
            });
            return;
        }
        
        const filterText = activeBadge.textContent.trim().toLowerCase();
        
        casinoItems.forEach(item => {
            if (filterText === 'new casinos') {
                // Display only new casinos (3rd one for demo purposes)
                if (item.querySelector('.rank-number') && item.querySelector('.rank-number').textContent === '3') {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            } else if (filterText === 'featured casinos' && item.classList.contains('featured-casino')) {
                item.style.display = 'block';
            } else if (filterText === 'best bonus' && item.querySelector('.bonus-amount')) {
                // Check for big bonuses (more than €1000 or with free spins)
                const bonusText = item.querySelector('.bonus-amount').textContent.toLowerCase();
                if (bonusText.includes('€3,000') || bonusText.includes('free spins')) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            } else if (filterText === 'fast payouts' && item.querySelector('.spec-label')) {
                // Check if casino has fast payout (24 hours or less)
                const payoutElements = item.querySelectorAll('.spec-label');
                let hasFastPayout = false;
                
                payoutElements.forEach(el => {
                    if (el.textContent.includes('Payout') && 
                        el.nextElementSibling && 
                        (el.nextElementSibling.textContent.includes('24') || 
                         el.nextElementSibling.textContent.includes('Instant'))) {
                        hasFastPayout = true;
                    }
                });
                
                item.style.display = hasFastPayout ? 'block' : 'none';
            } else if (filterText === 'all casinos') {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }
    
    // Function to sort casinos
    function sortCasinos(sortOption) {
        const casinoContainer = document.querySelector('.casino-listings');
        const casinoItems = Array.from(document.querySelectorAll('.casino-list-item'));
        
        if (!casinoContainer || casinoItems.length === 0) return;
        
        sortOption = sortOption ? sortOption.toLowerCase() : 'recommended';
        
        casinoItems.sort((a, b) => {
            if (sortOption === 'highest rated') {
                const ratingA = parseFloat(a.querySelector('.rating span').textContent) || 0;
                const ratingB = parseFloat(b.querySelector('.rating span').textContent) || 0;
                return ratingB - ratingA;
            } 
            else if (sortOption === 'newest first') {
                const isNewA = a.classList.contains('new-casino') ? 1 : 0;
                const isNewB = b.classList.contains('new-casino') ? 1 : 0;
                return isNewB - isNewA;
            }
            else if (sortOption === 'biggest bonus') {
                // Extract bonus amount if possible or use 0
                function extractBonusValue(el) {
                    const bonusText = el.querySelector('.bonus-amount')?.textContent || '';
                    const match = bonusText.match(/\d+/);
                    return match ? parseInt(match[0]) : 0;
                }
                
                const bonusA = extractBonusValue(a);
                const bonusB = extractBonusValue(b);
                return bonusB - bonusA;
            }
            else {
                // Default sort by rank
                const rankA = parseInt(a.querySelector('.rank-number')?.textContent) || 999;
                const rankB = parseInt(b.querySelector('.rank-number')?.textContent) || 999;
                return rankA - rankB;
            }
        });
        
        // Clear container and append sorted items
        casinoContainer.innerHTML = '';
        casinoItems.forEach(item => {
            casinoContainer.appendChild(item);
        });
    }
});

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
    
    // Review filters functionality
    const reviewFilterBadges = document.querySelectorAll('.review-filters .badge');
    
    if (reviewFilterBadges.length > 0) {
        reviewFilterBadges.forEach(badge => {
            badge.addEventListener('click', function() {
                // Toggle active class
                reviewFilterBadges.forEach(b => {
                    b.classList.remove('bg-primary');
                    b.classList.add('bg-light', 'text-dark');
                });
                
                this.classList.remove('bg-light', 'text-dark');
                this.classList.add('bg-primary');
                
                const filterType = this.getAttribute('data-filter');
                const reviewItems = document.querySelectorAll('.casino-list-item');
                
                // Плавная анимация для фильтрации
                reviewItems.forEach(item => {
                    // Определяем, должен ли элемент отображаться
                    const shouldDisplay = 
                        filterType === 'all' || 
                        (filterType === 'slots' && item.classList.contains('slots-casino')) ||
                        (filterType === 'live' && item.classList.contains('live-dealer')) ||
                        (filterType === 'mobile' && item.classList.contains('mobile-casino')) ||
                        (filterType === 'fast' && item.classList.contains('fast-payout'));
                    
                    if (shouldDisplay) {
                        // Если элемент должен быть показан, делаем это плавно
                        setTimeout(() => {
                            item.style.opacity = '1';
                            item.style.filter = 'blur(0)';
                            item.style.display = 'block';
                        }, 50);
                    } else {
                        // Если элемент должен быть скрыт, сначала анимируем исчезновение
                        item.style.opacity = '0';
                        item.style.filter = 'blur(4px)';
                        setTimeout(() => {
                            item.style.display = 'none';
                        }, 300); // Задержка соответствует времени перехода
                    }
                });
            });
        });
    }
    
    // Review sorting functionality
    const reviewSortSelect = document.querySelector('#sortSelect');
    if (reviewSortSelect) {
        reviewSortSelect.addEventListener('change', function() {
            const sortOption = this.value;
            const reviewContainer = document.querySelector('.container');
            const reviewItems = Array.from(document.querySelectorAll('.casino-list-item'));
            
            if (!reviewContainer || reviewItems.length === 0) return;
            
            reviewItems.sort((a, b) => {
                if (sortOption === 'rating-high' || sortOption === 'rating-low') {
                    const ratingA = parseFloat(a.querySelector('.rating span')?.textContent) || 0;
                    const ratingB = parseFloat(b.querySelector('.rating span')?.textContent) || 0;
                    return sortOption === 'rating-high' ? ratingB - ratingA : ratingA - ratingB;
                } else if (sortOption === 'newest') {
                    return -1; // Предполагаем, что первый элемент новее
                } else if (sortOption === 'a-z') {
                    const nameA = a.querySelector('.casino-name')?.textContent.trim() || '';
                    const nameB = b.querySelector('.casino-name')?.textContent.trim() || '';
                    return nameA.localeCompare(nameB);
                }
                return 0;
            });
            
            // Анимация для сортировки
            const reviewSection = document.querySelector('.container .pt-60.pb-60');
            const filterSection = reviewSection.querySelector('.review-filters');
            const moreReviewsSection = document.querySelector('.text-center.mt-4.mb-4');
            
            // Сначала скрываем все элементы
            reviewItems.forEach(item => {
                item.style.opacity = '0';
                item.style.filter = 'blur(4px)';
            });
            
            // Затем с небольшой задержкой меняем порядок
            setTimeout(() => {
                reviewSection.innerHTML = '';
                reviewSection.appendChild(filterSection);
                
                // Добавляем элементы в новом порядке
                reviewItems.forEach((item, index) => {
                    reviewSection.appendChild(item);
                    
                    // Плавно показываем элементы с cascade-эффектом (поочередно)
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.filter = 'blur(0)';
                    }, 50 * index); // Задержка между появлением каждого элемента
                });
                
                reviewSection.appendChild(moreReviewsSection);
            }, 300);
        });
    }
});