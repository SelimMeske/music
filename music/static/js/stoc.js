let notifySocket;
let ws_scheme = window.location.protocol == 'https' ? 'wss' : 'ws';

function connectSocket() {

    notifySocket = new WebSocket(
        ws_scheme + '://' + window.location.host + '/notify'
    );

    notifySocket.onmessage = function(e) {
        console.log('Here is the message')
        console.log(e.data);
    };

    notifySocket.onclose = function(e) {
        console.error("error");
        setTimeout(connectSocket, 1000);
    };

    notifySocket.onopen = function(e) {
        console.log("Socket connected");
        notifySocket.send("Whatsapp");
    }
};

connectSocket();