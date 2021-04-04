$(document).ready(function(){
    $("#add-comment").submit(function (e){
        e.preventDefault();
        let categorySlug = $(this).attr('data-categoryslug');

        $.get('/category/' + categorySlug + '/',
            function(data) {
                $('#comments').html(data);
        })
    })

})
