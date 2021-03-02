let player = document.querySelector('.main-audio-player');
let all_buttons = document.querySelectorAll('.audio-play');

for (i = 0; i < all_buttons.length; i++) {
    all_buttons[i].addEventListener('click', function(event){
        current_song = event.target;
        player.src = current_song.parentElement.id;
        player.play();
    })
}

