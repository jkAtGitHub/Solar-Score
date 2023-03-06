def add_marker(icon):
    lat, lng = fig.center
    marker = gmaps.Marker(location=(lat, lng), icon=icon)
    marker_layer.markers = marker_layer.markers + (marker,)

icons = [
    "http://maps.google.com/mapfiles/kml/pal2/icon4.png",
    "http://maps.google.com/mapfiles/kml/pal2/icon19.png",
    "http://maps.google.com/mapfiles/kml/pal2/icon22.png",
    "http://maps.google.com/mapfiles/kml/pal2/icon26.png"
]

dropdown = widgets.Dropdown(options=icons, description="Marker icon:")
button = widgets.Button(description="Add marker")

def on_button_clicked(b):
    add_marker(dropdown.value)

button.on_click(on_button_clicked)

display(widgets.VBox([dropdown, button]))
