let notifySocket;
let ws_scheme = window.location.protocol == 'https' ? 'wss' : 'ws';

let notify_container = document.querySelector('.custom-messages-container');

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
    }
};

connectSocket();

function notifyControl(message){
    let notify_div = document.createElement("div");
    notify_div.classList.add("custom-messages-box", "bg-success");
    notify_div.innerText = message;
    notify_container.appendChild(notify_div);
    removeInfoBox(notify_div);
}
function removeInfoBox(elem) {
   setTimeout(function() {elem.remove();}, 4000);
}

notifyControl('Hello there');