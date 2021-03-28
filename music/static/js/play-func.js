let player = document.querySelector('.main-audio-player');
let all_buttons = document.querySelectorAll('.audio-play');
let audio_play_single = document.querySelector('.audio-play-single');
let audio_pause_single = document.querySelector('.audio-pause-single');
let audio_play_pause_single = document.querySelector('.audio-play-pause-single');
let single_button_img_source = audio_play_pause_single.querySelector('img');
let current_playing = document.querySelector('.playing');
let current_paused = document.querySelector('.paused');
let wavesurfer;
let blocked = false;

wavesurfer = WaveSurfer.create({
                container: '.visual-audio',
                scrollParent: false,
                barWidth: 3,
                barHeight: 1,
                barGap: null,
                height: 50,
                fillParent: true,
                responsive: false,
                pixelRatio: 1,
                partialRender: true,
                waveColor: '#0d6efd',
                progressColor: '#4B0082',
                interact: true,
                backend: 'MediaElement'
            });


audio_play_pause_single.addEventListener('click', function(){
       wavesurfer.playPause();
});

for (i = 0; i < all_buttons.length; i++) {
    all_buttons[i].addEventListener('click', function(event){

        // Show player on first play
        let init_call = document.querySelector('.init-call');

        if (init_call){
            init_call.classList.remove('init-call');
        }

        if (blocked){
            return;
        }

        let current_song = event.target;
        let current_song_parent = current_song.parentElement.parentElement.parentElement;
        let audio_data = current_song.parentElement.parentElement.querySelector('textarea').value;

        audio_data = audio_data.replace('[', '').replace(']', '').split(",");
        let intlist = audio_data.map(x=>+x);

        if (current_song.classList.contains('playing') || current_song.classList.contains('paused')) {
            wavesurfer.playPause();
            current_song.classList.remove('playing');
            current_song.classList.add('paused');
        }else {
            if (current_playing){
                current_playing.classList.remove('playing');
                wavesurfer.playPause();
            }
            else if(current_paused){
                current_paused.classList.remove('paused');
                wavesurfer.playPause();
            }

            wavesurfer.destroy();

            wavesurfer = WaveSurfer.create({
                container: '.visual-audio',
                scrollParent: false,
                barWidth: 3,
                barHeight: 1,
                barGap: null,
                height: 50,
                fillParent: true,
                responsive: false,
                pixelRatio: 1,
                partialRender: true,
                interact: true,
                waveColor: '#0d6efd',
                progressColor: '#4B0082',
                backend: 'MediaElement'
            });

            current_url = window.location.protocol + "//" + window.location.host;

            wavesurfer.load(current_url + current_song.parentElement.parentElement.id, intlist);

            wavesurfer.playPause();
            wavesurfer.on('play', function(){
                single_button_img_source.src = '/static/images/pause-button-ico.png';
                console.log('bye')
            });
            wavesurfer.on('pause', function(){
                single_button_img_source.src = '/static/images/play-button-ico.png';
                console.log('hi');
            });
            current_song.classList.add('playing');
        }

        blocked = true;

        setTimeout(function(){
            blocked = false;
        }, 600);
    })
}

