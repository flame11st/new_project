mapboxgl.accessToken = 'pk.eyJ1IjoiZmxhbWUxMXN0IiwiYSI6ImNqN3VibmJtaDRydjIyd21qZDloeDU3MzQifQ.ktuL8tPfBYLGQ3YiJGtHTQ';
var map = new mapboxgl.Map({
	container: 'map',
	style: 'mapbox://styles/mapbox/light-v9',
});

map.on('load', function () {
	map.addLayer({
		"id": "route",
		"type": "line",
		"source": {"type": "geojson", "data": geojson},
		"layout": {
            "line-join": "round",
            "line-cap": "round"
        },
        "paint": {
            "line-color": "#888",
            "line-width": 8
        }
	});
});
