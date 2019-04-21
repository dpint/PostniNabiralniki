L.mapbox.accessToken = 'pk.eyJ1IjoiZHBpbnQiLCJhIjoiY2p0bXl4djVhMHJ6dTQzcGZ2NWEwN2FtaSJ9.hQcVksyHe0ask5gRp9kyFg';
var map = L.mapbox.map('map')
    .setView([46.056946, 14.505751], 9)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/mapbox/streets-v11'));

var markers = L.markerClusterGroup();

$.getJSON("postni_nabiralniki.json", function(data) {
    $.each(data["addresses"], function(i, item) {
        markers.addLayer(L.marker([item.lat, item.lng]));
    });   
});

map.addLayer(markers);