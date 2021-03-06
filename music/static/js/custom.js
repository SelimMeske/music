let fav_btns = document.querySelectorAll('.fav-btn');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const request = new Request(
    'add-remove-song',
    {headers: {'X-CSRFToken': csrftoken}}
);

for (let i = 0; i < fav_btns.length; i++) {

    fav_btns[i].addEventListener('click', function(event){

    current_fav_btn = event.target;

    if (current_fav_btn.classList.contains('favorite') && (current_fav_btn.src.includes('lover_red'))) {
        current_fav_btn.src = '/static/images/lover_black.png';
    }else {
        current_fav_btn.src = '/static/images/lover_red.png';
        current_fav_btn.classList.add('favorite');
    }

    fetch(request, {
        method: 'POST',
        mode: 'same-origin',
        body: JSON.stringify({
            "song-id": current_fav_btn.getAttribute('data-id')
        })
    }).then(function(response){
        console.log(response)
    });
});
}