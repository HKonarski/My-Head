document.addEventListener('DOMContentLoaded', () => {
    const animateElement = (selector) => {
        const element = document.querySelector(selector);
        if (!element) return;

        if (window.TweenMax) {
            TweenMax.to(element, 10, {
                rotation: 360,
                ease: Linear.easeNone,
                repeat: -1
            });
            return;
        }

        element.style.animation = 'rotacao 8s linear infinite';
        element.style.transformOrigin = 'center';
    };

    animateElement('#img');
    animateElement('.pokemon-img');
});