document.addEventListener('click', function(e) {
    id = e.target.id
    id = id.split('tt').join('')
    console.log(id)

    const proxyurl = "https://whispering-wave-91848.herokuapp.com/"
    const url = "https://themovieclips.p.rapidapi.com/trailers?imdb="+id+"&limit=3"

    fetch(proxyurl+url, {
        "method": "GET",
        "headers": {
            "x-rapidapi-host": "themovieclips.p.rapidapi.com",
            "x-rapidapi-key": "80d1b10cb0mshe34b0eb53cf0a02p1fed07jsn893bd88913f3"
        }
    })
    // .then(response => response.document())
    .then(contents => console.log(id))
    .catch(err => {
        console.log(err);
    });
});