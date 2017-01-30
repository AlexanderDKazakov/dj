//INITIAL CONDITIONS
PopUpHide();
//
// HIDE/SHOW FIELD FOR CONTACT INFORMATION
var $input = $("#id_call_otvet");
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
    }
})
// END H/S
// SORTING&FILTERS
var options = {
    valueNames: [ 'name', 'date', 'aim' ]
};
var userList = new List('users', options);
// END S&F
// PUPOP WINDOW
function PopUpShow(){
    $("#popup1").show();
}
function PopUpHide(){
    $("#popup1").hide();
}