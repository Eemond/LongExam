const form = document.querySelector('form');
const email = document.getElementById("email");
const phone = document.getElementById("phone");
const subject = document.getElementById("subject");
const mess = document.getElementById("message");
const fullName = document.getElementById("fullName"); // Assuming you have an input field with id="fullName"

function sendEmail() {
    const bodyMessage = `Full Name: ${fullName.value}<br> Email: ${email.value}<br> Phone Number: ${phone.value}<br> Message: ${mess.value}`;

    Email.send({
        Host : "smtp.elasticemail.com",
        Username : "reymondramos424@gmail.com",
        Password : "929B8861F0C77D0E1A04F7B6AAF627F0402A",
        To : 'reymondramos424@gmail.com',
        From : "reymondramos424@gmail.com", // Corrected email address
        Subject : subject.value,
        Body : bodyMessage
    }).then(
      message => {
        if (message === "OK") {
            Swal.fire({
                title: "Good job!",
                text: "Email sent successfully!",
                icon: "success"
              });
        } else {
            Swal.fire({
                title: "Oops...",
                text: "Something went wrong. Please try again later.",
                icon: "error"
              });
        }
      }
    );
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    sendEmail();
});
