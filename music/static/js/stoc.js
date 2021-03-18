let notify_container = document.querySelector('.custom-messages-container');

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