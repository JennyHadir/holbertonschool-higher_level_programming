// Fetche the character name from url and display it in html tag
$.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function (data) {
    $('#character').html(data.name);
});
