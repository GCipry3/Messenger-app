document.addEventListener('DOMContentLoaded', () => {
    // Send message when 'enter' is pressed
    let msg = document.querySelector('#user_message');
    msg.addEventListener('keyup', event => {
        event.preventDefault();
        // Number 13 is the "Enter" key on the keyboard
        if (event.keyCode === 13) {
            document.querySelector('#send_message').click();
        }
    });
});