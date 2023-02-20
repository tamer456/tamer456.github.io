// Fetch posts from API and create post elements
fetch('https://jsonplaceholder.typicode.com/posts')
.then(response => response.json())
.then(posts => {
    const main = document.querySelector('main');
    posts.forEach(post => {
        // Create post element
        const postElement = document.createElement('div');
        postElement.classList.add('post');
        postElement.innerHTML = `
            <h2>${post.title}</h2>
            <p>${post.body}</p>
        `;

        // Fetch comments for the post
        fetch(`https://jsonplaceholder.typicode.com/comments?postId=${post.id}`)
            .then(response => response.json())
            .then(comments => {
                // Create comments element for this post
                const commentsElement = document.createElement('div');
                comments.forEach(comment => {
                    const commentElement = document.createElement('div');
                    commentElement.classList.add('comment');
                    commentElement.innerHTML = `
                        <p>${comment.body}</p>
                        <p><em>- ${comment.email}</em></p>
                    `;
                    commentsElement.appendChild(commentElement);
                });

                // Add comments to post element
                postElement.appendChild(commentsElement);
            });

        // Add post to main element
        main.appendChild(postElement);
    });
});