// Fetche all movies title from url and append it in html list
$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
        let films = data.results;
        for (let film in films) {
            $('UL#list_movies').append("<li>" + films[film].title + "</li>");
        }  
});
