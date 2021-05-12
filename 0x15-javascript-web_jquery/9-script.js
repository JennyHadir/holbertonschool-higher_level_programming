// Fetche the value of hello from url and display it in html tag
$.get("https://fourtonfish.com/hellosalut/?lang=fr", function (data) {
    $('#hello').html(data.hello);
});
