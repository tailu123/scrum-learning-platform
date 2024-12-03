// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', () => {
    // 初始化动画
    initializeAnimations();
    // 初始化滚动监听
    initializeScrollObserver();
    // 初始化平滑滚动
    initializeSmoothScroll();
});

// 初始化动画
function initializeAnimations() {
    // 标题动画
    anime({
        targets: '.hero h1',
        opacity: [0, 1],
        translateY: [50, 0],
        duration: 1000,
        easing: 'easeOutExpo'
    });

    // 描述文字动画
    anime({
        targets: '.hero p',
        opacity: [0, 1],
        translateY: [30, 0],
        duration: 1000,
        delay: 300,
        easing: 'easeOutExpo'
    });

    // 按钮动画
    anime({
        targets: '.hero button',
        opacity: [0, 1],
        translateY: [20, 0],
        duration: 800,
        delay: anime.stagger(100, {start: 500}),
        easing: 'easeOutExpo'
    });
}

// 初始化滚动监听
function initializeScrollObserver() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // 添加动画类
                entry.target.classList.add('visible');
                // 如果是卡片，添加特殊动画
                if (entry.target.classList.contains('card')) {
                    anime({
                        targets: entry.target,
                        opacity: [0, 1],
                        translateY: [30, 0],
                        duration: 600,
                        easing: 'easeOutExpo'
                    });
                }
            }
        });
    }, {
        threshold: 0.1
    });

    // 监听所有需要动画的元素
    document.querySelectorAll('.fade-in, .card').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
}

// 初始化平滑滚动
function initializeSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// 添加导航栏滚动效果
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('nav');
    if (window.scrollY > 50) {
        navbar.classList.add('shadow-md');
        navbar.classList.remove('shadow-sm');
    } else {
        navbar.classList.remove('shadow-md');
        navbar.classList.add('shadow-sm');
    }
}); 