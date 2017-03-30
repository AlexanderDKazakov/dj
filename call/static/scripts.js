//INITIAL CONDITIONS
PopUpHide();
//
// $(document).on('submit','#myform_requst1',function (e) {
//            e.preventDefault();
//
//            $.ajax({
//                type:"POST",
//                url:"xhr_test/",
//                data:{
//                    date_from:$('#date_from').val(),
//                    date_to:$('#date_to').val(),
//                    inp_otdel:$('#inp_otdel').val(),
//                    // cache:false,
//                    // dataType: "json",
//                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
//                },
//                success:function(){
//
//                }
//            });
//         });
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
    valueNames: [ 'name', 'date', 'aim', 'user' ]
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
// $("#but1").click(function(){
//       $("#par1").load("data_out/");
//    })
   // //######################################## TEST
   // $(function() {
   //    $("#test").click(function() {
   //       $.get("xhr_test/", function(data) {
   //          alert(data);
   //       });
   //    });
   //  });
//##########################
// DATAPICKER EXPORT FUNCTION
    $( function() {
    var dateFormat = "dd/mm/yy",
      from = $( "#from" )
        .datepicker({
          defaultDate: "+1w",
          changeMonth: true,
          numberOfMonths: 1,
          dateFormat: "dd/mm/yy"
        })
        .on( "change", function() {
          to.datepicker( "option", "minDate", getDate( this ) );
        }),
      to = $( "#to" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: "dd/mm/yy"
      })
      .on( "change", function() {
        from.datepicker( "option", "maxDate", getDate( this ) );
      });
      to = $( "#id_call_date_end" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: "dd.mm.yy"
      })
      .on( "change", function() {
        from.datepicker( "option", "maxDate", getDate( this ) );
      });

    function getDate( element ) {
      var date;
      try {
        date = $.datepicker.parseDate( dateFormat, element.value );
      } catch( error ) {
        date = null;
      }

      return date;
    }
  } );
// END DATAPICKER
// START DATATIMEPICKER
// $( function() {
//     to = $('#id_call_date_end').datetimepicker({
// 	timeFormat: "hh:mm tt"
// });
// }
// END DATATIMEPICKER
// COLOR THE TABLE DEPENDING ON DATE
//     $(function () {
//     var currentdate = new Date();
//     var d = new Date();
//     var datetime = "Last Sync: " + currentdate.getDate() + "/" + (currentdate.getMonth()+1) + "/" + currentdate.getFullYear() + " @ " + currentdate.getHours() + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();
//     // document.getElementById("callDate123").innerHTML = d.toUTCString();
//     document.write(datetime);
//     // document.write("<br>");
//     // document.write(d);
//     });
