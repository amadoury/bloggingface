$(function(){
    $('.formsd').keypress((e) => { 
        // Enter key corresponds to number 13
        if (e.which === 13) {
            e.preventDefault(); 

            question = $('input[name^="promptvalue"]').val();
            divQuestion = $('<div class="text-end question">'+  question + '</div>');
            divQuestion.appendTo('.chat');
            $.post('/chatbot/prompt', {prompt:question, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value} , function(data){
                divResponse =  $('<div class="text-end response">'+  data.response + '</div>');
                divResponse.appendTo('.chat');
                $('input[name^="promptvalue"]').val("");
            });
        } 
    }) 
});