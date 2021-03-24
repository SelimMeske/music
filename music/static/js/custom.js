let fav_btns = document.querySelectorAll('.fav-btn');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
let img_container = document.querySelectorAll('.cover-img-wrap');

const request = new Request(
    'add-remove-song',
    {headers: {'X-CSRFToken': csrftoken}}
);

for (let i = 0; i < fav_btns.length; i++) {

    fav_btns[i].addEventListener('click', function(event){

    current_fav_btn = event.target;

    fetch(request, {
        method: 'POST',
        mode: 'same-origin',
        body: JSON.stringify({
            "song-id": current_fav_btn.getAttribute('data-id')
        })
    }).then(function(response){
        if (response.status == 200){
            if (current_fav_btn.classList.contains('favourite-song')) {
                    current_fav_btn.classList.remove('favourite-song')
            }else {
                current_fav_btn.classList.add('favourite-song');
            }
            return response.json();
        }
    }).then(function(json){
        notifyControl(json.message);
    });
});
}

for (let o=0; o < img_container.length; o++){

    img_container[o].addEventListener('mouseenter', function(event){
        let current_img_container = event.target;
        let black_overlay = current_img_container.querySelector('.black-overlay');
        let play_button = current_img_container.querySelector('.play-button');
        let fav_button = current_img_container.querySelector('.fav-btn');
        play_button.style.opacity = '1';
        black_overlay.style.opacity = '0.6';
        //fav_button.style.opacity = '1';
    });

    img_container[o].addEventListener('mouseleave', function(event){
        let current_img_container = event.target;
        let black_overlay = current_img_container.querySelector('.black-overlay');
        let play_button = current_img_container.querySelector('.play-button');
        let fav_button = current_img_container.querySelector('.fav-btn');
        play_button.style.opacity = '0.0';
        black_overlay.style.opacity = '0.0';
        //fav_button.style.opacity = '0.0';
    });

}

function on_change(){

}
