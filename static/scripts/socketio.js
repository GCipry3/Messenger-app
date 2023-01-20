document.addEventListener('DOMContentLoaded', () => {
    var socket = io();
    let room = 'Lounge';
    joinRoom('Lounge');

    socket.on('message', data => {
        const p = document.createElement('p');
        const br = document.createElement('br');
        if (data.username) {
            // Create a container 
            const container = document.createElement('div');
            container.className = 'container';

            const span_timestamp = document.createElement('span');
            span_timestamp.innerHTML = "(" + data.time_stamp + ")";
            container.append(span_timestamp);

            const span_username = document.createElement('span');
            span_username.style.color = '#16573c';
            span_username.innerHTML = data.username;
            container.append(span_username);

            const span_message = document.createElement('span');
            span_message.style.fontSize = '20px';
            span_message.innerHTML = ": "+data.msg;
            container.append(span_message);

            document.querySelector('#display-message-section').append(container);
        } else {
            printSysMsg(data.msg);
        }
    });

    // Send message
    document.querySelector('#send_message').onclick = () => {
        socket.send({
            'msg': document.querySelector('#user_message').value,
            'username': username,
            'room': room
        });
        document.querySelector('#user_message').value = '';
    };

    // Room selection
    document.querySelectorAll('.select-room').forEach(p => {
        p.onclick = () => {
            let newRoom = p.innerHTML;
            if (newRoom == room) {
                msg = `You are already in ${room} room.`;
                printSysMsg(msg);
            } else {
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }
        }
    });

    // Leave room
    function leaveRoom(room) {
        socket.emit('leave', {'username': username, 'room': room});
    }

    // Join room
    function joinRoom(room) {
        socket.emit('join', {'username': username, 'room': room});
        document.querySelector('#display-message-section').innerHTML = '';
        document.querySelector('#user_message').focus();
    }

    // Print system message
    function printSysMsg(msg) {
        const container = document.createElement('div');
        container.className = 'container';

        const span_message = document.createElement('span');
        span_message.style.color = 'red';
        span_message.innerHTML = msg;
        container.append(span_message);

        document.querySelector('#display-message-section').append(container);
    }

})