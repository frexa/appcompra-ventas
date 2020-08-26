$(document).ready(function() {

    $('#boton-modal').on('click', function() {

        //El metodo .modal(), se utiliza para abrir la ventana modal de bootstrap 4
        $('#modal-date').modal();

    })

    $('#checkin').datepicker({
        language: "es",
        todayBtn: "linked",
        clearBtn: true,
        format: "dd/mm/yyyy",
        multidate: false,
        todayHighlight: true

    });

    $('#checkout').datepicker({
        language: "es",
        todayBtn: "linked",
        clearBtn: true,
        format: "dd/mm/yyyy",
        multidate: false,
        todayHighlight: true

    });

})