// Коли html документ готовий (промальований)
$(document).ready(function () {
    // Беремо з розмітки елемент по id - оповіщення від django
    var notification = $('#notification');
    // И через 7 сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // При натисканні на значок кошика відкриваємо спливаюче(модальне) вікно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Клік по кнопці закрити вікна кошика
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обробник події радіокнопки вибору способу доставки
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Приховуємо або відображаємо input введення адреси доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});