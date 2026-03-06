const hamburguesa = document.querySelector('.hamburguesa');
const navLinks = document.querySelector('.nav-links');
const nav = document.querySelector('nav');

hamburguesa.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
});

const uploadBox = document.getElementById('uploadBox');
const fileInput = document.getElementById('fileInput');

uploadBox.addEventListener('click', () => fileInput.click());

uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = 'var(--naranja-marca)';
    uploadBox.style.background = '#fff9f5';
});

uploadBox.addEventListener('dragleave', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = '#ddd';
    uploadBox.style.background = 'transparent';
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.style.borderColor = 'var(--naranja-marca)';
    uploadBox.style.background = '#fff9f5';
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        uploadBox.querySelector('p').textContent = Archivo seleccionado: ${files[0].name};
    }
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        uploadBox.querySelector('p').textContent = Archivo seleccionado: ${fileInput.files[0].name};
    }
});