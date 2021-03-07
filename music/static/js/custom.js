let fav_btns = document.querySelectorAll('.fav-btn');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// Toast
let toast = document.querySelector('.main-toast');
console.log(toast)
const request = new Request(
    'add-remove-song',
    {headers: {'X-CSRFToken': csrftoken}}
);

for (let i = 0; i < fav_btns.length; i++) {

    fav_btns[i].addEventListener('click', function(event){

    current_fav_btn = event.target;

    if (current_fav_btn.classList.contains('favourite-song')) {
        current_fav_btn.classList.remove('favourite-song')
        toast.toast('show');
    }else {
        current_fav_btn.classList.add('favourite-song');
        toast.toast('show');
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



