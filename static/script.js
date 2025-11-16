let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

window.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
} 

const typed = new Typed('.multiple-text', {
    strings: ['Web Developer', 'Backend Developer', 'Web Developer'],
    typeSpeed: 80,
    backSpeed: 80,
    backDelay: 1200,
    loop: true,
});

// --- New Functionality for "Read More" in About Section ---
// --- AND Refactored Logic for Service Read More Buttons ---

// Generic function to toggle content visibility
function toggleReadMore(button) {
    // Get the ID of the content element from the button's data-target attribute
    const targetId = button.getAttribute('data-target');
    const content = document.getElementById(targetId);

    if (!content) return; // Exit if the content element doesn't exist

    // Toggle the display property
    if (content.style.display === 'none' || content.style.display === '') {
        // Show content
        content.style.display = 'inline'; // Use 'inline' or 'block' depending on desired flow
        // Change button text
        button.textContent = 'Show Less';
    } else {
        // Hide content
        content.style.display = 'none';
        // Change button text back
        button.textContent = 'Read More';
    }
}


// Wait until the entire document is loaded before adding event listeners
document.addEventListener('DOMContentLoaded', () => {
    const aboutReadMoreBtn = document.getElementById('about-read-more-btn');
    const moreAboutContent = document.getElementById('more-about-content');

    // 1. Logic for About Me Section (Block display)
    if (aboutReadMoreBtn && moreAboutContent) {
        aboutReadMoreBtn.addEventListener('click', (e) => {
            e.preventDefault(); 
            
            // Toggle the display property (using 'block' for the paragraph in About Me)
            if (moreAboutContent.style.display === 'none' || moreAboutContent.style.display === '') {
                moreAboutContent.style.display = 'block';
                aboutReadMoreBtn.textContent = 'Show Less';
            } else {
                moreAboutContent.style.display = 'none';
                aboutReadMoreBtn.textContent = 'Read More';
            }
        });
    }

    // 2. Logic for Services Section (Inline display)
    const serviceReadMoreBtns = document.querySelectorAll('.read-more-service-btn');
    
    serviceReadMoreBtns.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault(); 
            toggleReadMore(button);
        });
    });

});