from tkinter import *
import requests
from tkinter.messagebox import *
import json
window=Tk()
window.title("Weather App")
window.geometry("300x200")

def getweatherinfo():
    api_key="28586fbd5099986e339951d7dbd1fb18"
    city=entry1.get()
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res=requests.get(url)
    json_data=json.loads(res.text)
    print(json_data)
    print(json_data["main"]["temp"])
    
    weather = json_data["weather"][0]["description"]
    temperature=json_data["main"]["temp"]
    humidity=json_data["main"]["humidity"]
    wind_speed=json_data["wind"]["speed"]
    city_name=json_data["name"]
    country_name=json_data["sys"]["country"]
    showinfo(f'{city.title()} Weather',f'city_name:{city_name}\n Country:{country_name}\n Weather:{weather} \n Temperature:{temperature} \n Humidity:{humidity} : 'f'{humidity} \n Wind Speed:{wind_speed}')
    
entryvar=StringVar()

citylabel=Label(window,text="Enter City",font=("Arial",10))
citylabel.grid(row=0,column=2,columnspan=2)

entry1=Entry(window,textvariable=entryvar)
entry1.grid(row=1,column=3,columnspan=1,padx=50,pady=10,ipady=5,ipadx=20)

searchbutton=Button(window,text="Weather Info",command=getweatherinfo)
searchbutton.grid(row=2,column=2,columnspan=2,pady=10)

window.mainloop()
