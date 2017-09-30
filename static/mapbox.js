mapboxgl.accessToken = 'pk.eyJ1IjoiZmxhbWUxMXN0IiwiYSI6ImNqN3VibmJtaDRydjIyd21qZDloeDU3MzQifQ.ktuL8tPfBYLGQ3YiJGtHTQ';
var map = new mapboxgl.Map({
	container: 'map',
	style: 'mapbox://styles/mapbox/light-v9',
	center: coord,
	zoom: 15
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
