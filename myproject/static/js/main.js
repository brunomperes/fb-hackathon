var fb;

$('#settings_form').submit(function(event){
    event.preventDefault();

    var id;

    FB.api('/me', {fields: 'id'}, function(response) {
      if (response.error !== undefined){
        id = response.id; 
      }
    });

    $(this).find('input[name="facebook-id"]').val(id);

    return true;
});

$('#ready_btn').click(function(event){
    event.preventDefault();

    var button = $(this);
    button.removeClass('btn-warning');
    button.addClass('btn-success disabled');
    button.html('Waiting for more users...(' + int(3) +')' )

    return;

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
  if (FB == null && fb == null && FB.getAccessToken === undefined){
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
