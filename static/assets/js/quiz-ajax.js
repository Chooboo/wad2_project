$(document).ready(function(){
    // Function for rendering the first question of the quiz
    $("body").on("click", "#start-quiz", function(){
        $.get('/quiz/question/1/',
            {'points': 0},
            function (data) {
                $('#quiz-content').html(data);
            })
    });
    // Function for moving on to the next question of the quiz without refreshing
    $("body").on("click", "#next-question",function() {
        let questionId = parseInt($(this).attr('data-questionid'));
        let points = parseInt($("#point-counter").text());
        let newPoints = parseInt($("input[type='radio']:checked").val());
        if (!isNaN(newPoints)){
            if (questionId !== 10) {
                $.get('/quiz/question/' + (questionId + 1) + '/',
                    {'points': points + newPoints},
                    function (data) {
                        $('#quiz-content').html(data);
                    })
            } else {
                document.location.href = '/quiz/quizresults/' + (points + newPoints) + '/';
            }
        }
    });
})