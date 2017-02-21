from tkinter import *
import requests
import json
import math

window = Tk()

def getinfo():
    temp_txt.delete(1.0, END)
    mint_txt.delete(1.0, END)
    maxt_txt.delete(1.0, END)
    wther_txt.delete(1.0, END)
    dis_txt.delete(1.0, END)
    wspd_txt.delete(1.0, END)
    wdgr_txt.delete(1.0, END)
    hmd_txt.delete(1.0, END)
    slvl_txt.delete(1.0, END)
    name_txt.delete(1.0, END)

    citynm = city_value.get()
    params = dict(q=citynm, APPID = '26ee310aed6872889843892aa2ff1c1b')
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params)

    if resp.status_code == 200:
        info = resp.json()

        temp_avg = int(round(info['main']['temp']- 273.15))
        temp_min = int(math.floor(info['main']['temp_min'] - 273.15))
        temp_max = int(math.ceil(info['main']['temp_max'] - 273.15))
        temp_txt.insert(END, temp_avg)
        temp_txt.insert(END, '°C')
        name_txt.insert(END, info['name'])
        mint_txt.insert(END, temp_min)
        mint_txt.insert(END, '°C')
        maxt_txt.insert(END, temp_max)
        maxt_txt.insert(END, '°C')
        wther_txt.insert(END, info['weather'][0]['main'])
        dis_txt.insert(END, info['weather'][0]['description'])
        wspd_txt.insert(END, info['wind']['speed'])
        wspd_txt.insert(END, 'm/s')
        wdgr_txt.insert(END, info['wind']['deg'])
        wdgr_txt.insert(END, '°')
        hmd_txt.insert(END, info['main']['humidity'])
        hmd_txt.insert(END, '%')
        slvl_txt.insert(END, info['main']['sea_level'])
        slvl_txt.insert(END,'m')

    else:
        temp_txt.insert(END, '↑Invalid city name↑')





city_label = Label(window, text='City', justify=LEFT)
city_label.grid(row=0, column =0)

city_value = StringVar()
city_entry = Entry(window, textvariable=city_value)
city_entry.grid(row=0, column=1)

srch = Button(window,  text='Search', command=getinfo)
srch.grid(row=0, column=2)

temp_label = Label(window, text='Temperature', justify=LEFT)
temp_label.grid(row=1, column=0)

temp_txt = Text(window, width=20, height=1)
temp_txt.grid(row=1, column=1)

name_label = Label(window, text='Station Name', justify=LEFT)
name_label.grid(row=1, column=2)

name_txt = Text(window, width=20, height=1)
name_txt.grid(row=1, column=3)

mint_label = Label(window, text='Min Temp', justify=LEFT)
mint_label.grid(row=2, column=0)

mint_txt = Text(window, width=20, height=1)
mint_txt.grid(row=2, column=1)

maxt_label= Label(window, text='Max Temp', justify=LEFT)
maxt_label.grid(row=2, column=2)

maxt_txt = Text(window, width=20, height=1)
maxt_txt.grid(row=2, column=3)

wther_label = Label(window, text='Weather', justify=LEFT)
wther_label.grid(row=3, column=0)

wther_txt = Text(window, width=20, height=1)
wther_txt.grid(row=3, column=1)

dis_label = Label(window, text='Description', justify=LEFT)
dis_label.grid(row=3, column=2)

dis_txt = Text(window, width=20, height=1)
dis_txt.grid(row=3, column=3, columnspan=3)



wspd_label = Label(window, text='Wind speed')
wspd_label.grid(row=4, column=0)

wspd_txt = Text(window, width=20, height=1)
wspd_txt.grid(row=4, column=1)

wdgr_label = Label(window, text='Wind degree')
wdgr_label.grid(row=4, column=2)

wdgr_txt = Text(window, width=20, height=1)
wdgr_txt.grid(row=4, column=3)

hmd_label = Label(window, text='Humidity')
hmd_label.grid(row=5, column=0)

hmd_txt = Text(window, width=20, height=1)
hmd_txt.grid(row=5, column=1)

slvl_label = Label(window, text='Sea level')
slvl_label.grid(row=5, column=2)

slvl_txt = Text(window, width=20, height=1)
slvl_txt.grid(row=5, column=3)

window.mainloop()
