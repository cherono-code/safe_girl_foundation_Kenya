document.addEventListener("DOMContentLoaded", function () {
    const slides = document.getElementById("slides");
    let counter = 1;

    setInterval(() => {
        slides.style.transition = "transform 0.5s ease-in-out";
        slides.style.transform = `translateX(${-counter * 100}%)`;

        counter++;

        if (counter === 6) {
            counter = 1;
            setTimeout(() => {
                slides.style.transition = "none";
                slides.style.transform = "translateX(0)";
            }, 500);
        }
    }, 3000);
});

//for event.html, our_books.html comiing soon updatte
document.addEventListener('DOMContentLoaded', function () {
    // Example: Change text color on button click
    const changeColorButton = document.getElementById('changeColorButton');
    
    if (changeColorButton) {
        changeColorButton.addEventListener('click', function () {
            document.body.style.color = getRandomColor();
        });
    }
});

// Function to generate a random color
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
//One time and Monthly donation butttons
document.addEventListener('DOMContentLoaded', function () {
    // Function to show or hide donation options based on the donation type
    function showDonationOptions(type) {
        var donationOptions = document.getElementById('donationOptions');

        // Reset to hide all options
        donationOptions.style.display = 'none';

        if (type === 'oneTime' || type === 'monthly') {
            // Show donation options for one-time or monthly
            donationOptions.style.display = 'block';
        }
    }

    // Attach click event listeners to the buttons
    document.getElementById('oneTimeDonation').addEventListener('click', function () {
        console.log('One Time Donation button clicked.');
        showDonationOptions('oneTime');
    });

    document.getElementById('monthlyDonation').addEventListener('click', function () {
        showDonationOptions('monthly');
    });
});