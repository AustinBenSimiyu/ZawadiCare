document.addEventListener('DOMContentLoaded', function() {
    // Flash message auto-dismiss
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 3000);
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            requiredFields.forEach(field => {
                if (!field.value) {
                    e.preventDefault();
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });
        });
    });

    // Date input enhancement for due date
    const dueDateInput = document.querySelector('input[type="date"]');
    if (dueDateInput) {
        // Set min date to today
        const today = new Date();
        const maxDate = new Date();
        maxDate.setMonth(maxDate.getMonth() + 9); // 9 months from now
        
        dueDateInput.min = today.toISOString().split('T')[0];
        dueDateInput.max = maxDate.toISOString().split('T')[0];
    }

    // Mobile menu toggle (if we decide to add a hamburger menu later)
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }
});

// Utility functions
function formatDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

function calculateWeeks(dueDate) {
    const due = new Date(dueDate);
    const today = new Date();
    const diffTime = Math.abs(due - today);
    const diffWeeks = Math.ceil(diffTime / (1000 * 60 * 60 * 24 * 7));
    return 40 - diffWeeks; // Assuming 40 weeks total pregnancy
}


const additionalCSS = `
.error {
    border-color: red !important;
}

.flash-message {
    transition: opacity 0.3s ease;
}

.nav-links {
    transition: all 0.3s ease;
}

@media (max-width: 768px) {
    .nav-links {
        display: none;
    }
    
    .nav-links.active {
        display: flex;
    }
}
`;


document.addEventListener('DOMContentLoaded', function() {
    // Set default date and time for appointment
    const dateInput = document.querySelector('input[type="datetime-local"]');
    if (dateInput) {
        const now = new Date();
        now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
        dateInput.min = now.toISOString().slice(0, 16);
        
        if (!dateInput.value) {
            dateInput.value = now.toISOString().slice(0, 16);
        }
    }
});


document.addEventListener('DOMContentLoaded', function() {
    // Handle appointment deletion
    const appointmentList = document.querySelector('.appointment-list');
    if (appointmentList) {
        appointmentList.addEventListener('submit', function(e) {
            if (e.target.matches('form')) {
                e.preventDefault();
                
                if (confirm('Are you sure you want to delete this appointment?')) {
                    const appointmentItem = e.target.closest('.appointment-item');
                    appointmentItem.classList.add('deleting');
                    
                    setTimeout(() => {
                        // Submit the form after animation
                        e.target.submit();
                    }, 300);
                }
            }
        });
    }
});