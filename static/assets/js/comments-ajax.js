$(document).ready(function(){
    // Function for adding comments dynamically
    $("#add-comment").submit(function (e){
        e.preventDefault();
        let cookie = document.cookie;
        let csrfToken = cookie.substring(cookie.indexOf('=') + 1);
        let categorySlug = $(this).attr('data-categoryslug');
        let userId = $(this).attr('data-userid');
        let commentBody = $('#comment-body').val();

        $("#add-comment").trigger("reset");

        $.post('/categories/' + categorySlug + '/',
            {'user-id' : userId,
            'body': commentBody,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()},
            function (data) {
                $('#comments').html(data);
            })

    });
    // Function for removing comments dynamically
    $("body").on("click", ".remove-comment",function() {
        let commentId = $(this).attr('data-commentid');
        let categorySlug = $(this).attr('data-categoryslug')

        $.get('/categories/' + categorySlug + '/remove-comment/' + commentId + '/',
            function (data) {
                $('#comments').html(data);
        })
    });
    // Function for liking/disliking comments dynamically
    $("body").on("click", ".like-button", function() {
        let commentId = $(this).attr('data-commentid');
        let categorySlug = $(this).attr('data-categoryslug');
        let userId = $(this).attr('data-userid');

        $.get('/categories/' + categorySlug + '/toggle-like/' + commentId + '/',
            {'user-id': userId},
            function (data) {
                $('#comments').html(data);
        })
    })
});
