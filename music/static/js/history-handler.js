let home_button = document.querySelector('.navbar-brand');
let my_profile = document.querySelector('.circle-profile-image');

home_button.addEventListener('click', function(){
      history.pushState(null, null, '')
});

my_profile.addEventListener('click', function(){
      history.pushState(null, null, 'profile');
      console.log('hi');
});

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