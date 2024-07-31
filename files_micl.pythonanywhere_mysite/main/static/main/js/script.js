function createStar() {
    const star = document.createElement('div');
    star.classList.add('star');
    const size = Math.random() * 4; // Размер звезды
    star.style.width = size + 'px';
    star.style.height = size + 'px';
    star.style.left = Math.random() * window.innerWidth + 'px';
    star.style.top = Math.random() * window.innerHeight + 'px';
    document.body.appendChild(star);

    const duration = Math.random() * 2 + 1; // Скорость анимации
    star.style.animationDuration = duration + 's';

    setTimeout(() => {
        star.remove(); // Удаление звезды после завершения анимации
        createStar(); // Создание новой звезды
    }, duration * 1000);
}

// Создаем начальные звезды
for (let i = 0; i < 100; i++) {
    createStar();
}
