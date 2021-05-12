// Transalte Hello in giving code lang and display it in tag
$(function () {
    $('INPUT#btn_translate').click(function () {
        const code = $('#language_code').val();
        $.get("https://fourtonfish.com/hellosalut/?lang=" + code, function (data) {
            $('#hello').html(data.hello);
        });
    });
});
