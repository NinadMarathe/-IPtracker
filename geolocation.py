from flask import Flask, redirect , url_for, render_template, request, session
from geolite2 import geolite2

import requests

import gmplot

app = Flask(__name__)
app.secret_key="hello"

print("hello")

@app.route("/navi",methods=["POST", "GET"])
def navi():
	if request.method == "POST":
		print("------------ INSIDE NAVI")
		user=request.form["nm"]
		session["user"]=user
		my_ip = requests.get('https://api.ipify.org').text
		my_ip_location(func(user))
		return redirect(url_for("user"))
	else:
		return render_template("plzwork.html")



def func(str):
	c=-1
	for x in str:
		c+=1
		print(str[c:(c+14)])
		if ((x=="R") and (str[c:(c+14)]=="Received: from")):
			print("ok")
			str=str[c:]
			break
	for x in str:
		if(str.find('[')):
				pe=str.find('[')
				print(pe)
				str=str[pe:]
	for x in str:
		pe=str.find(']')
		str=str[1:pe]
		print(str)
		break
	return str




def my_ip_location(my_ip):

    reader = geolite2.reader()

    location = reader.get(my_ip)

    c=(location['country']['names']['en'])

    d=(location['location'])



    print('''country: %s\nlocation: %s\n'''

     % (c,d))

    x = list(d.values())



    lat = x[1]

    lon = x[2]

    print(lat, lon)



    gmap = gmplot.GoogleMapPlotter(lat, lon, 13)

    latitude_list = [lat, lat+0.5, lat +1.0]

    longitude_list = [lon, lon +0.5, lon+1.0]



    gmap.apikey = "AIzaSyCrSQ4s0h54Go7RIV3oDr-wsN5lOd7jot4"

    # scatter method of map object

    # scatter points on the google map
    gmap.scatter( latitude_list, longitude_list, 'red',size = 40, marker = False )
    # Plot method Draw a line in between given coordinates
    gmap.plot(latitude_list, longitude_list,'#ff8759', edge_width = 2.5)
    gmap.draw("C:\\Users\Acer\Desktop\Python\Flasktut\\templates\\map.html")
    return render_template("map.html")




x = "global"
global p
p=[]
@app.route("/user")
def user():
	if "user" in session:
		user=session["user"]
		print("------------ INSIDE USER")
		x=user
		p.append(x)
		print(p)
		print("value entered : "+x)
		# my_ip = requests.get('https://api.ipify.org').text
		# my_ip_location(x)
		return render_template("map.html")

if __name__== "__main__" :
	app.run(debug=True)
