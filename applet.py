import gi
gi.require_version('Gtk', '3.0')
gi.require_version('XApp', '1.0')
from gi.repository import Gtk, XApp
import requests

direction = ""
headers = {
	"Content-Type": "application/json",
	"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxNzVmZDJlYWZmODA0OGJmOTk4ZDE5MTJhMGQ3ZDkwZCIsImlhdCI6MTY3NTMzMjkwOSwiZXhwIjoxOTkwNjkyOTA5fQ.NfPsebbQl28eEKSSOHciA9ThJ_UlJXt45s6H-ZNrwrE"
}

def on_scroll_event(status_icon, event, x, y):
	print(status_icon.props.name)
	icon_number = status_icon.props.name
	if event == 1:
		direction = "down"
	elif event == -1:
		direction = "up"
	print(direction)
	bright_dim(direction, icon_number)

def bright_dim(direction, icon_number):
	url = "http://192.168.1.121:8123/api/services/light/turn_on"
	if direction == "up":
		data = {
			"brightness_step": "20"
		}
	elif direction == "down":
			data = {
			"brightness_step": "-20"
		}
	if icon_number == "icon1":
		data.update({"entity_id": "light.office_lights"})
	elif icon_number == "icon2":
		data.update({"entity_id": "light.living_room_lights"})
	elif icon_number == "icon3":
		data.update({"entity_id": "light.front_room_lights"})
	response = requests.post(url, headers=headers, json=data)
	print(response)

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
		print("Selected color: RGBA({}, {}, {}, {})".format(
			red, green, blue, alpha
		))
	color_chooser.destroy()
	url = "http://192.168.1.121:8123/api/services/light/turn_on"
	data = {
	"rgb_color": [red,green,blue]
	}
	if icon_number == "icon1":
		data.update({"entity_id": "light.office_lights"})
	elif icon_number == "icon2":
		data.update({"entity_id": "light.living_room_lights"})
	elif icon_number == "icon3":
		data.update({"entity_id": "light.front_room_lights"})
	response = requests.post(url, headers=headers, json=data)
	print(response)

def toggle(icon_number):
	url = "http://192.168.1.121:8123/api/services/light/toggle"
	if icon_number == "icon1":
		data = {"entity_id": "light.office_lights"}
	elif icon_number == "icon2":
		data = {"entity_id": "light.living_room_lights"}
	elif icon_number == "icon3":
		data = {"entity_id": "light.front_room_lights"}
	response = requests.post(url, headers=headers, json=data)
	print(response)

def on_button_event(status_icon, button, time):
	print(status_icon.props.name)
	print(button)
	icon_number = status_icon.props.name
	if button == 1:
		toggle(icon_number)
	elif button == 3:
		change_color(icon_number)

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
