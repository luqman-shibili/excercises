document.querySelectorAll('.image').forEach((image, index) => {
    image.addEventListener('click', () => {
        image.style.zIndex = 4;
        setTimeout(() => {
            image.style.zIndex = index + 1;
        }, 300);
    });
});
