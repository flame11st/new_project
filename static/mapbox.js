mapboxgl.accessToken = 'pk.eyJ1IjoiZmxhbWUxMXN0IiwiYSI6ImNqN3VibmJtaDRydjIyd21qZDloeDU3MzQifQ.ktuL8tPfBYLGQ3YiJGtHTQ';
var map = new mapboxgl.Map({
	container: 'map',
	style: 'mapbox://styles/mapbox/streets-v9',
	center: [30.516253709793087,50.45835782737586],
	zoom: 10
});

map.on('load', function () {
	map.addLayer({
		"id": "points",
		"type": "symbol",
		"source": {"type": "geojson", "data": geojson},
		"layout": {
		"icon-image": "triangle-15",
		"text-field": title,
		"text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
		"text-offset": [0, 0.6],
		"text-anchor": "top"
		}
	});
});