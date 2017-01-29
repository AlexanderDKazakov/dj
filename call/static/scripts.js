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
