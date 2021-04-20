let all_blog_posts_holder = document.querySelector('.blog-all-posts-container');
let one_blog_post_container = document.createElement('div');
one_blog_post_container.classList.add('blog-post-container');

blog_request = new Request(
    'get-all-posts'
);

get_all_posts();

function get_all_posts(){

    fetch(blog_request, {
        method: 'GET',
        mode: 'same-origin'
    }).then(function (response) {
        let posts = response.json();
        return posts;
    }).then(function(result){
        let posts = JSON.parse(result);
        
        /** Clear posts holder */
        all_blog_posts_holder.innerHTML = '';

        for(let i=0; i<posts.length; i++){
            let post_id = posts[i].pk;
            let post = posts[i].fields;
            let post_image_url = window.location.protocol + "//" + window.location.host + '/media/' + post.image;
            let html_post = `
            <div class="inner-blog-post d-flex justify-content-start align-items-end">
                <div class="blog-post-image-holder">
                    <img src="${post_image_url}"/>
                </div>
                <div class="blog-post-info-holder">
                    <h3>${post.title}</h3>
                    <p>short paginated text for this post this is</p>
                    <a id="${post_id}" class="btn btn-primary read-post">Read Post</a>
                </div>
            </div>`;
            
            let new_elem = document.createElement('div');
            new_elem.innerHTML = html_post;
            all_blog_posts_holder.appendChild(new_elem);
        }
    }).then(function(res){
        let all_posts_buttons = document.querySelectorAll('.read-post');
        for(let i=0; i<all_posts_buttons.length; i++){
        
            all_posts_buttons[i].addEventListener('click', function(){
                get_post(all_posts_buttons[i].id);
                pushHistory('post');
            });
        }
    });
} 

function get_post(pk){
    fetch(new Request('post/'+pk), {
        method: 'GET',
        mode: 'same-origin'
    }).then(function(response){
        let html_response = response.text();
        return html_response;
    }).then(function(html_response){

        /** Clear posts holder */
        all_blog_posts_holder.innerHTML = '';
        all_blog_posts_holder.innerHTML = html_response;
    });
};

window.addEventListener('popstate', e => {
    let current_location = e.state.location;

    if(current_location == 'blog'){
        get_all_posts();
        return;
    }
    blog_post_page.classList.toggle('open-close-blog');
});

