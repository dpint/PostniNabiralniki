L.mapbox.accessToken = 'pk.eyJ1IjoiZHBpbnQiLCJhIjoiY2p0bXl4djVhMHJ6dTQzcGZ2NWEwN2FtaSJ9.hQcVksyHe0ask5gRp9kyFg';
var map = L.mapbox.map('map')
    .setView([46.056946, 14.505751], 9)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/mapbox/streets-v11'));

$.getJSON("postni_nabiralniki.json", function(data) {
    $.each(data, function(i, item) {
        L.marker([item.lat, item.lng]).addTo(map);
    });   
});