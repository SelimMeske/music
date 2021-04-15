let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
let all_blog_posts_holder = document.querySelector('.blog-all-posts-container');
let one_blog_post_container = document.createElement('div');
one_blog_post_container.classList.add('blog-post-container');


blog_request = new Request(
    'get-all-posts',
    { headers: { 'X-CSRFToken': csrftoken } }
);

fetch(blog_request, {
    method: 'GET',
    mode: 'same-origin'
}).then(function (response) {
    let posts = response.json();
    return posts;
}).then(function(result){
    let posts = JSON.parse(result);
    for(let i=0; i<posts.length; i++){
        let post = posts[i].fields;
        console.log(post)
        let html_post = `
        <div class="inner-blog-post d-flex justify-content-start align-items-end">
            <div class="blog-post-image-holder">
                <img src="${post.image}"/>
            </div>
            <div class="blog-post-info-holder">
                <h3>${post.title}</h3>
                <p>short paginated text for this post this is</p>
                <a href="" class="btn btn-primary">Read Post</a>
            </div>
        </div>`;
        
        let new_elem = document.createElement('div');
        new_elem.innerHTML = html_post;
        all_blog_posts_holder.appendChild(new_elem);
        
        //all_blog_posts_html_content.push(html_post);
    }
    /*for(let p=0; p<all_blog_posts_html_content.length; p++){
        all_blog_posts_holder.appendChild(all_blog_posts_html_content[p])
        console.log('iter')
    }*/
})

