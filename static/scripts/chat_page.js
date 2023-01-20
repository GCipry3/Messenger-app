document.addEventListener('DOMContentLoaded', () => {
    let msg = document.querySelector('#user_message');
    msg.addEventListener('keyup', event => {
        // Number 13 is the "Enter" key on the keyboard
        if (event.keyCode === 13) {
            document.querySelector('#send_message').click();
        }
    });
});
