import subprocess
import requests
path = "C:\\Program Files\\Inkscape\\bin\\inkscape.exe"
svgfile = "drawing.svg"
gcode = "drawing.gcode"
api = ""
thingid = ""
variableid = "e249fdb1-1a18-4279-91ef-f219260da419"
url = f"https://api2.arduino.cc/iot/v2/things/{thingid}/properties/"
# creates the command to run inkscape and create a gcode file
# "path to executable, name of svg file, name of export file, what is going to be exported"
command = [path, svgfile, "--export-filename=" + gcode, "--export-type=gcode"]
# Runs code in terminal returns error if it doesn't work
subprocess.run(command, check=True)
#Reads the gcode file and sends the command to the arduino cloud.
#reads the gcode file made by the function above
with open(gcode_file, "r") as file:
gcode_lines = file.readlines()
for line in gcode_lines:
        #dictionary with authorization api and content type.
    	headers = {"Authorization": f"Bearer {api}", "Content-Type": "application/json"}
#creates a url to send to cloud and the specific variable id of the thing
    	url = url + variableid
	#Sends request to url and sends the gcode with it, ues api key
    	returnresponse = requests.put(url, json={"value": line.strip()}, headers=headers) 
generategcode()

