$(document).ready(function(){
    $("#add-comment").submit(function (e){
        e.preventDefault();
        let categorySlug = $(this).attr('data-categoryslug');
        let userId = $(this).attr('data-userid');
        let commentBody = $('#comment-body').val();

        $("#add-comment").trigger("reset");

        $.post('/category/' + categorySlug + '/',
            {'user-id' : userId,
            'body': commentBody},
            function (data) {
                $('#comments').html(data);
            })

    });
    $("body").on("click", ".remove-comment",function() {
        let commentId = $(this).attr('data-commentid');
        let categorySlug = $(this).attr('data-categoryslug')

        $.get('/category/' + categorySlug + '/remove-comment/' + commentId + '/',
            function (data) {
                $('#comments').html(data);
        })
    });
});
