let player = document.querySelector('.main-audio-player');
let all_buttons = document.querySelectorAll('.audio-play');

for (i = 0; i < all_buttons.length; i++) {
    all_buttons[i].addEventListener('click', function(event){

        current_song = event.target;
        current_song_parent = current_song.parentElement.parentElement.parentElement;

        let current_playing = document.querySelector('.playing');

        if (current_song.classList.contains('playing')) {
            current_song.innerHTML = 'Play';
            player.pause();
            current_song.classList.remove('playing');
            current_song_parent.classList.remove('width-100-custom');
        }else {
            if (current_playing){
                current_playing.innerHTML = 'Play';
                current_playing.classList.remove('playing');
                current_playing.parentElement.parentElement.parentElement.remove('width-100-custom');
            }
            player.src = current_song.parentElement.parentElement.id;
            player.play();
            current_song.innerHTML = 'Stop';
            current_song.classList.add('playing');
            current_song_parent.classList.add('width-100-custom');
        }

    })
}

