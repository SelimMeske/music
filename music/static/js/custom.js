let fav_btns = document.querySelectorAll('.fav-btn');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

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


