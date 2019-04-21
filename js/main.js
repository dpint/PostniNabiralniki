L.mapbox.accessToken = 'pk.eyJ1IjoiZHBpbnQiLCJhIjoiY2p0bXl4djVhMHJ6dTQzcGZ2NWEwN2FtaSJ9.hQcVksyHe0ask5gRp9kyFg';
var map = L.mapbox.map('map')
    .setView([46.056946, 14.505751], 9)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/mapbox/streets-v11'));

var markers = L.markerClusterGroup();

$.getJSON("postni_nabiralniki.json", function(data) {
    $.each(data["addresses"], function(i, item) {
        var marker = L.marker([item.lat, item.lng])
        marker.bindPopup("<b>Ulica:</b> " + item.street + " " + item.house_number 
                            + "<br><b>Kraj:</b> " + item.post_code + " " + item.city 
                            + "<br><b>Naziv pošte:</b> " + item.post_office 
                            + "<br><b>ID:</b> " + item.id)
        markers.addLayer(marker);
    });   
});

map.addLayer(markers);