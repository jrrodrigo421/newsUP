document.addEventListener('DOMContentLoaded', function () {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', function () {
            mainNav.style.display = mainNav.style.display === 'flex' ? 'none' : 'flex';
        });
    }

    // Handle article card hover effects
    const articleCards = document.querySelectorAll('.article-card');

    articleCards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = 'var(--shadow-lg)';
        });

        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = 'var(--shadow-md)';
        });
    });

    // Add current date to footer
    const footerYear = document.querySelector('.footer-content p');
    if (footerYear) {
        const currentYear = new Date().getFullYear();
        footerYear.innerHTML = footerYear.innerHTML.replace('{% now year %}', currentYear);
    }

    // Simulate loading state for buttons
    const buttons = document.querySelectorAll('.btn');

    buttons.forEach(button => {
        button.addEventListener('click', function (e) {
            // Don't apply to links or form submissions
            if (this.tagName === 'A' || this.type === 'submit') return;

            const originalText = this.innerHTML;
            this.innerHTML = '<span class="material-icons">hourglass_top</span> Loading...';
            this.disabled = true;

            // Simulate loading
            setTimeout(() => {
                this.innerHTML = originalText;
                this.disabled = false;
            }, 1500);
        });
    });

    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add tech animation to the hero section
    const techIllustration = document.querySelector('.tech-illustration');

    if (techIllustration) {
        // Add rotating animation to tech circles
        const techCircle = document.querySelector('.tech-circle');
        const techLines = document.querySelector('.tech-lines');

        if (techCircle && techLines) {
            techCircle.style.animation = 'rotate 20s linear infinite';
            techLines.style.animation = 'rotate 30s linear infinite reverse';

            // Add keyframes for rotation
            const style = document.createElement('style');
            style.textContent = `
                @keyframes rotate {
                    from { transform: translate(-50%, -50%) rotate(0deg); }
                    to { transform: translate(-50%, -50%) rotate(360deg); }
                }
            `;
            document.head.appendChild(style);
        }
    }
});