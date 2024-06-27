$(function(){
    function updateScroll() {
        var chat_messages = document.getElementById("chat-messages");
        chat_messages.scrollTop = chat_messages.scrollHeight;
        console.log(chat_messages.scrollTop)
    }

    $('.formsd').keypress((e) => { 
        // Enter key corresponds to number 13
        if (e.which === 13) {
            e.preventDefault(); 
            input = $('input[name^="promptvalue"]');
            question = input.val();
            input.val("");

            divQuestion = $('<div class="text-end question">'+  question + '</div>');
            divQuestion.appendTo('.chat');

            waiting = $('<div class="waiting"><p>Wait for the answer ... </p></div>');
            waiting.appendTo('.chat');
            updateScroll();

            $.post('/chatbot/prompt', {prompt:question, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value} , function(data){
                waiting.remove();
                divResponse =  $(data.response);
                divResponse.appendTo('.chat');
                updateScroll();
            });
        } 
    });

    $('.form-rag').keypress((e) => { 
        // Enter key corresponds to number 13
        if (e.which === 13) {
            e.preventDefault(); 
            input = $('input[name^="promptrag"]');
            question = input.val();
            input.val("");

            waiting = $('<div class="waiting"><p>Wait for the answer ... </p></div>');
            waiting.appendTo('.response-rag');

            $.post('/chatbot/rag', {prompt:question, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value} , function(data){
                waiting.remove();
                divResponse =  $(data.response);
                divResponse.appendTo('.response-rag');
            });
        } 
    }) 
});