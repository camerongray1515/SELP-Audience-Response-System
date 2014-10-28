function RunningSesson(sessionCode) {
    this.sessionCode = sessionCode;

    this.checkForQuestions = function() {
        $.get('/student/check_question_availability/', {
            'session_code': this.sessionCode
        }, function(response) {
            if (response.question_available) {
                console.log("Question Available");
                setTimeout(showQuestion, response.time_to_start);
            } else {
                // If there were no questions, check again in 2 seconds
                setTimeout(runningSession.checkForQuestions, 2000);
            }
        });
    };

    showQuestion = function() {
        console.log("Question Started!");
    };
}

var runningSession = new RunningSesson(sessionCode);