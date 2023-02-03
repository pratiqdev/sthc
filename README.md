# lightbulb-applet-py

Python script that makes use of HomeAssistants API to control lights with statusbar icons on the Linux desktop

Written with [PyGObject](https://pygobject.readthedocs.io/en/latest/) and [XApp](https://lazka.github.io/pgi-docs/XApp-1.0/index.html) 

Current features:

  - Multiple lights/entities (currently hardcoded)
  - Mouse scroll over applet to dim/brighten light
  - Left click an applet to toggle the light entity
  - Right click an applet to set RGB color on light

Future roadmap:

  - More object-oriented (cleaner)
  - Faster (somehow)
  - Move configuration to YAML/TOML file
  - Move API calls to a plugin based system for expandability


okthx
