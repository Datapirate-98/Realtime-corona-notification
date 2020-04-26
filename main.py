



from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message):
	notification.notify(title = title, message = message, app_icon = "C:/Users/satya/realtime_corona/corona_icon.ico", timeout = 5)


def getdata(url):
	r = requests.get(url)
	return r.text

def corona():
	while True:
		#notifyme("satyam ", "here you are")
		data = getdata("https://www.mohfw.gov.in/")


		
		soup = BeautifulSoup(data, "html.parser")
		#print(soup.prettify())
		mydatastr = ""
		for trow in soup.find_all('tr'):
			mydatastr += trow.get_text()
		mydatastr = mydatastr[1:]

		itemlist = mydatastr.split("\n\n")

		states = ["Odisha", "Tamil Nadu"]

		for item in itemlist[0:34]:
			datalist = (item.split("\n"))
			if datalist[1] in states:
				print(datalist)
				noti_title = "Cases of Covid-19"
				noti_text = f"{datalist[1]}\n Cases : {datalist[2]}\n Cured: {datalist[3]}\n Death: {datalist[4]} "
				notifyme(noti_title, noti_text)
		time.sleep(3600)

if __name__ == "__main__":
	corona()

	


