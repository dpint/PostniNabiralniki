var mymap = L.map('mapid').setView([46.056946, 14.505751], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors"
}).addTo(mymap);

$.getJSON("py/nabiralniki.json", function(data) {
    $.each(data, function(i, item) {
        L.marker([data[i].lat, data[i].lon]).addTo(mymap);
    });   
});