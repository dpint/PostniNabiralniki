var map, userLocationMarker;

function initMap(){
    L.mapbox.accessToken = 'pk.eyJ1IjoiZHBpbnQiLCJhIjoiY2p0bXl4djVhMHJ6dTQzcGZ2NWEwN2FtaSJ9.hQcVksyHe0ask5gRp9kyFg';

    map = L.mapbox.map('map')
        .setView([46.056946, 14.505751], 9)
        .addLayer(L.mapbox.styleLayer('mapbox://styles/mapbox/streets-v11'));
}

function displayMarkers(){
    var markers = L.markerClusterGroup();

    $.getJSON("data/postni_nabiralniki.json", function(data) {
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
}

function locateUser(){
    map.locate({setView: true, maxZoom: 16}).on("locationfound", e => {
        if(!userLocationMarker){
            userLocationMarker = L.circle(e.latlng, {
                color: 'Crimson',
                fillColor: 'red',
                fillOpacity: 0.5,
                radius: 20
            });
            userLocationMarker.addTo(map);
        }else{
            userLocationMarker.setLatLng(e.latlng);
        }
    }).on("locationerror", error => {
        if(userLocationMarker){
            map.removeLayer(userLocationMarker);
            userLocationMarker = undefined;
        }
    });
}