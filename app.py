from bottle import *
import requests 

application=Bottle()

@application.route("/",method=["POST","GET"])
def home():
	if request.method=="POST":
		try:
			num=int(request.forms.get("num"))
			url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"
			res=requests.get(url)
			if res.status_code==200:
				data=res.json()
				RATE=data["bitcoin"]["inr"]
				amt=RATE*num
				msg="₹"+str(round(amt,2))
				return template("home.tpl",msg=msg)
			else:
				msg="status code "+str(res.status_code)
				return template("home.tpl",msg=msg)
		except ValueError:
			msg="please enter integers only"
			return template("home.tpl",msg=msg)
	else:
		return template("home.tpl",msg="")
run(application,host="localhost",port=4050,debug=True,reloader =True)
