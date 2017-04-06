// HIDE/SHOW FIELD FOR CONTACT INFORMATION
var $input = $("#div_id_call_otvet");
    if ($input.prop('checked')){
        $("#id_call_kontact").css({'display': 'inline-block'});
    }
    else {
        $("#id_call_kontact").css({'display': 'none'});
    }

$("#id_call_otvet").click(function(){
    var $input = $(this);
    if ($input.prop('checked')){
        $("#id_call_kontact").css({'display': 'inline-block'});
    }
    else {
        $("#id_call_kontact").css({'display': 'none'});
        // $("#id_call_otvet").css(unchecked)
    }
});
// REDIRECT CALL
var $input = $("#div_id_call_otvet_redirect");
    if ($input.prop('checked')){
        $("#id_call_kontact_redirect").css({'display': 'inline-block'});
    }
    else {
        $("#id_call_kontact_redirect").css({'display': 'none'});
    }

$("#id_call_otvet_redirect").click(function(){
    var $input = $(this);
    if ($input.prop('checked')){
        $("#id_call_kontact_redirect").css({'display': 'inline-block'});
    }
    else {
        $("#id_call_kontact_redirect").css({'display': 'none'});
        // $("#id_call_otvet").css(unchecked)
    }
});
// END H/S
// SORTING&FILTERS
var options = {
    valueNames: [ 'name', 'date', 'aim', 'user' ]
};
var userList = new List('users', options);
// END S&F