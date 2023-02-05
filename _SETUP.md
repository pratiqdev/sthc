# SETUP

Installed / updated python 
`^3 (3.10.6)`

Created python virtual environment from the current dir
`python3 -m venv .`

Activated the venv
`source ./bin/activate`

Install `pipreqs` to generate a requirement file (after each new `import` added to script)
`pip install pipreqs`

Run pipreqs in the current dir (after each new `import` added to script)
`pipreqs .`

Install all packages in `requirements.txt`
`pip install -r requirements.txt`

Install PyGObject on ubuntu (already installed and up to date)
`sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0`