var fb;


$('#ready_btn').click(function(event){
    event.preventDefault();

    var button = $(this);

    var url = "/myapp/ready/"; // the script where you handle the form input.

    $.ajax({
           type: "GET",
           url: url,
           data: button.attr('data-user-id'), // serializes the form's elements.
           success: function(data)
           {    
                button.removeClass('btn-warning');
                button.addClass('btn-success disabled');
                button.html('Waiting for more users...(' + int(data) +')' )
           }
     });

    setInterval(checkAgain, 1000);
});

function checkAgain(){
    $.ajax({
      type: "GET",
      data: '',
      url: '/myapp/ready',
      success: function (data) {
        if (data <= 0){
            window.location.href = "/myapp/";
        } else {
            setInterval(checkAgain, 1000);
        }
      },
    })
}

function isLogged(){
  if (FB == null && fb == null){
    return false;
  }
  return true;
}

// Verifies on every 
function authenticationStep(){
  if (!isLogged()){
    window.location.href = "/myapp/login";
  }
  else {
    
  }
}

$(window).load(function() {
  authenticationStep();
  FB.api('/me', function(response) {
    console.log(response);
  });

});
