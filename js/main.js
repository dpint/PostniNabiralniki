var mymap = L.map('mapid').setView([46.554649, 15.645881], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors"
}).addTo(mymap);

const fs = require('fs');
const pdf = require('../node_modules/pdf-parse');
