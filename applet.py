import gi
gi.require_version('Gtk', '3.0')
gi.require_version('XApp', '1.0')
from gi.repository import Gtk, XApp
import requests

host = "192.168.1.121"
port = "8123"
endpoint = lambda a: "http://" + host + ":" + port + a
rgb_luminence = "/api/services/light/turn_on"
light_toggle = "/api/services/light/toggle"

ha_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxNzVmZDJlYWZmODA0OGJmOTk4ZDE5MTJhMGQ3ZDkwZCIsImlhdCI6MTY3NTMzMjkwOSwiZXhwIjoxOTkwNjkyOTA5fQ.NfPsebbQl28eEKSSOHciA9ThJ_UlJXt45s6H-ZNrwrE"

print(endpoint(rgb_luminence))
print(endpoint(light_toggle))

headers = {
	"Content-Type": "application/json",
	"Authorization": "Bearer " + ha_token
}

def api_send(endpoint, post_data):
	response = requests.post(endpoint, headers=headers, json=post_data)
	print(response)


def data_select(icon_number, direction="", rgb_color=[]):
	data = {}
	if icon_number == "icon1":
		data.update({"entity_id": "light.office_lights"})
	elif icon_number == "icon2":
		data.update({"entity_id": "light.living_room_lights"})
	elif icon_number == "icon3":
		data.update({"entity_id": "light.front_room_lights"})

	if direction != "":
		if direction == "up":
			data.update({"brightness_step": "20"})
		elif direction == "down":
			data.update({"brightness_step": "-20"})

	if rgb_color != []:
		data.update({"rgb_color": rgb_color})
		
	print(data)
	return data
	del data


def on_button_event(status_icon, button, time):
	icon_number = status_icon.props.name
	if button == 1: #left click
		change_toggle(icon_number)
	elif button == 3: #right click
		change_color(icon_number)


def on_scroll_event(status_icon, event, x, y):
	icon_number = status_icon.props.name
	if event == 1:
		direction = "down"
	elif event == -1:
		direction = "up"
	change_luminence(icon_number, direction)
	del direction


def change_toggle(icon_number):
	api_send(endpoint(light_toggle), data_select(icon_number))


def change_luminence(icon_number, direction):
	api_send(endpoint(rgb_luminence), data_select(icon_number, direction))


def change_color(icon_number):
	color_chooser = Gtk.ColorChooserDialog("Choose a color")
	color_chooser.set_transient_for(None)
	color_chooser.set_modal(True)
	response = color_chooser.run()
	if response == Gtk.ResponseType.OK:
		color = color_chooser.get_rgba()
		red = int(color.red * 255)
		green = int(color.green * 255)
		blue = int(color.blue * 255)
		alpha = int(color.alpha * 255)
	color_chooser.destroy()
	api_send(endpoint(rgb_luminence), data_select(icon_number, None, [red,green,blue]))



icon1 = XApp.StatusIcon()
icon1.connect("scroll-event", on_scroll_event)
icon1.connect("activate", on_button_event)
icon1.set_icon_name("/home/albo/lightbulb-applet-py/bulb1.png")
icon1.set_name("icon1")
icon1.set_tooltip_text("Office")
icon1.set_label("Office")
icon1.set_visible(True)

icon2 = XApp.StatusIcon()
icon2.connect("scroll-event", on_scroll_event)
icon2.connect("activate", on_button_event)
icon2.set_icon_name("/home/albo/lightbulb-applet-py/bulb2.png")
icon2.set_visible(True)
icon2.set_name("icon2")
icon2.set_tooltip_text("Living Room")

icon3 = XApp.StatusIcon()
icon3.connect("scroll-event", on_scroll_event)
icon3.connect("activate", on_button_event)
icon3.set_icon_name("/home/albo/lightbulb-applet-py/bulb3.png")
icon3.set_visible(True)
icon3.set_name("icon3")
icon3.set_tooltip_text("Front Room")

Gtk.main()
