$(document).ready(function () {
            // Fetch movie data from the API
            $.ajax({
                url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
                method: 'GET',
                dataType: 'json',
                success: function (data) {
                    // Get the list of movies from the API response
                    var movies = data.results;

                    // Loop through each movie and append the title to the list
                    for (var i = 0; i < movies.length; i++) {
                        var title = movies[i].title;
                        $('#list_movies').append('<li>' + title + '</li>');
                    }
                },
                error: function (error) {
                    console.log('Error fetching movie data:', error);
                }
            });
        });
