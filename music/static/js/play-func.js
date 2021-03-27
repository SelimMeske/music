let player = document.querySelector('.main-audio-player');
let all_buttons = document.querySelectorAll('.audio-play');
let wavesurfer;
let blocked = false;

for (i = 0; i < all_buttons.length; i++) {
    all_buttons[i].addEventListener('click', function(event){

        if (blocked){
            return;
        }

        let current_song = event.target;
        let current_song_parent = current_song.parentElement.parentElement.parentElement;
        let audio_data = current_song.parentElement.parentElement.querySelector('textarea').value;
        let audio_waves_cont = document.createElement('div');
        audio_waves_cont.classList.add('flex-fill', 'visual-audio');

        let current_playing = document.querySelector('.playing');

        audio_data = audio_data.replace('[', '').replace(']', '').split(",");
        let intlist = audio_data.map(x=>+x);

        if (current_song.classList.contains('playing')) {
            current_song.innerHTML = 'Play';
            current_song.classList.remove('playing');
            wavesurfer.playPause();
            current_song_parent.classList.remove('width-100-custom');
            current_song_parent.querySelector('.visual-audio').remove();
        }else {
            if (current_playing){
                current_playing.innerHTML = 'Play';
                current_playing.classList.remove('playing');
                wavesurfer.playPause();
                wavesurfer.destroy();
                current_playing.parentElement.parentElement.parentElement.classList.remove('width-100-custom');
                current_song_parent.querySelector('.visual-audio').remove();
            }

            if(wavesurfer){
                wavesurfer.destroy();
            }

            current_song_parent.classList.add('width-100-custom');
            current_song_parent.append(audio_waves_cont);

            wavesurfer = WaveSurfer.create({
                container: '.visual-audio',
                scrollParent: false,
                barWidth: 3,
                barHeight: 1, // the height of the wave
                barGap: null,
                height: 50,
                fillParent: true,
                responsive: false,
                pixelRatio: 1,
                partialRender: true,
                backend: 'MediaElement'
            });

            current_url = window.location.protocol + "//" + window.location.host;

            wavesurfer.load(current_url + current_song.parentElement.parentElement.id, intlist);

            // player.src = current_song.parentElement.parentElement.id;
            // player.play();
            wavesurfer.playPause();
            current_song.innerHTML = 'Stop';
            current_song.classList.add('playing');
        }

        blocked = true;

        setTimeout(function(){
            blocked = false;
        }, 1000);
    })
}

