#!/usr/bin/env python
import tkinter as tk
import requests
import json
import math
from functools import partial


def fill_form(temp_txt, mint_txt, maxt_txt, wther_txt, des_txt, wspd_txt, wdgr_txt, hmd_txt, slvl_txt, name_txt, city_value):
    temp_txt.delete(1.0, tk.END)
    mint_txt.delete(1.0, tk.END)
    maxt_txt.delete(1.0, tk.END)
    wther_txt.delete(1.0, tk.END)
    des_txt.delete(1.0, tk.END)
    wspd_txt.delete(1.0, tk.END)
    wdgr_txt.delete(1.0, tk.END)
    hmd_txt.delete(1.0, tk.END)
    slvl_txt.delete(1.0, tk.END)
    name_txt.delete(1.0, tk.END)

    citynm = city_value.get()
    params = dict(q=citynm, APPID = '26ee310aed6872889843892aa2ff1c1b')
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params)

    if resp.status_code == 200:
        info = resp.json()
        # information from main section
        main_section = info.get('main')
        if main_section != None:
            # get temperature
            temp_avg = main_section.get('temp')
            if temp_avg != None:
                temp_avg = int(round(temp_avg - 273.15))
                temp_txt.insert(tk.END, temp_avg)
                temp_txt.insert(tk.END, '°C')
            else:
                temp_txt.insert(tk.END, 'n/a')
            # get min temperature
            temp_min = main_section.get('temp_min')
            if temp_min != None:
                temp_min = int(math.floor(temp_min - 273.15))
                mint_txt.insert(tk.END, temp_min)
                mint_txt.insert(tk.END, '°C')
            else:
                mint_txt.insert(tk.END, 'n/a')
            # get max temperature
            temp_max = main_section.get('temp_max')
            if temp_max != None:
                temp_max = int(math.ceil(temp_max - 273.15))
                maxt_txt.insert(tk.END, temp_max)
                maxt_txt.insert(tk.END, '°C')
            else:
                maxt_txt.insert(tk.END, 'n/a')
            # get humidity info
            humidity = main_section.get('humidity')
            if humidity != None:
                hmd_txt.insert(tk.END, humidity)
                hmd_txt.insert(tk.END, '%')
            else:
                hmd_txt.insert(tk.END, 'n/a')
            # get sea level info
            sea_level = main_section.get('sea_level')
            if sea_level != None:
                slvl_txt.insert(tk.END, sea_level)
                slvl_txt.insert(tk.END,'m')
            else:
                slvl_txt.insert(tk.END,'n/a')

        else:
            temp_txt.insert(tk.END, 'n/a')
            mint_txt.insert(tk.END, 'n/a')
            maxt_txt.insert(tk.END, 'n/a')
            hmd_txt.insert(tk.END, 'n/a')
            slvl_txt.insert(tk.END,'n/a')

        # information from weather section
        weather_section = info.get('weather')
        if weather_section != None:
            # get the weather info
            short_description = weather_section[0].get('main')
            if short_description != None:
                wther_txt.insert(tk.END, short_description)
            else:
                wther_txt.insert(tk.END, 'n/a')
            # get the longer weather description
            long_description = weather_section[0].get('description')
            if long_description != None:
                des_txt.insert(tk.END, long_description)
            else:
                des_txt.insert(tk.END, 'n/a')
        else:
            wther_txt.insert(tk.END, 'n/a')
            des_txt.insert(tk.END, 'n/a')
        # wind section
        wind_section = info.get('wind')
        if wind_section != None:
            # get the wind speed info
            wind_speed = wind_section.get('speed')
            if wind_speed != None:
                wspd_txt.insert(tk.END, wind_speed)
                wspd_txt.insert(tk.END, 'm/s')
            else:
                wspd_txt.insert(tk.END, 'n/a')
            # get the wind degree info
            wind_degree = wind_section.get('deg')
            if wind_degree != None:
                wdgr_txt.insert(tk.END, wind_degree)
                wdgr_txt.insert(tk.END, '°')
            else:
                wdgr_txt.insert(tk.END, 'n/a')
        else:
            wspd_txt.insert(tk.END, 'n/a')
            wdgr_txt.insert(tk.END, 'n/a')
        # name section
        name_section = info.get('name')
        if name_section != None:
            # get name
            name_txt.insert(tk.END, name_section)
        else:
            name_txt.insert(tk.END, 'n/a')

    else:
        temp_txt.insert(tk.END, '↑Invalid city name↑')


def main():
    window = tk.Tk()

    city_label = tk.Label(window, text='City', justify=tk.LEFT)
    city_label.grid(row=0, column =0)

    city_value = tk.StringVar()
    city_entry = tk.Entry(window, textvariable=city_value)
    city_entry.grid(row=0, column=1)



    temp_label = tk.Label(window, text='Temperature', justify=tk.LEFT)
    temp_label.grid(row=1, column=0)

    temp_txt = tk.Text(window, width=20, height=1)
    temp_txt.grid(row=1, column=1)

    name_label = tk.Label(window, text='Station Name', justify=tk.LEFT)
    name_label.grid(row=1, column=2)

    name_txt = tk.Text(window, width=20, height=1)
    name_txt.grid(row=1, column=3)

    mint_label = tk.Label(window, text='Min Temp', justify=tk.LEFT)
    mint_label.grid(row=2, column=0)

    mint_txt = tk.Text(window, width=20, height=1)
    mint_txt.grid(row=2, column=1)

    maxt_label= tk.Label(window, text='Max Temp', justify=tk.LEFT)
    maxt_label.grid(row=2, column=2)

    maxt_txt = tk.Text(window, width=20, height=1)
    maxt_txt.grid(row=2, column=3)

    wther_label = tk.Label(window, text='Weather', justify=tk.LEFT)
    wther_label.grid(row=3, column=0)

    wther_txt = tk.Text(window, width=20, height=1)
    wther_txt.grid(row=3, column=1)

    des_label = tk.Label(window, text='Description', justify=tk.LEFT)
    des_label.grid(row=3, column=2)

    des_txt = tk.Text(window, width=20, height=1)
    des_txt.grid(row=3, column=3, columnspan=3)



    wspd_label = tk.Label(window, text='Wind speed')
    wspd_label.grid(row=4, column=0)

    wspd_txt = tk.Text(window, width=20, height=1)
    wspd_txt.grid(row=4, column=1)

    wdgr_label = tk.Label(window, text='Wind degree')
    wdgr_label.grid(row=4, column=2)

    wdgr_txt = tk.Text(window, width=20, height=1)
    wdgr_txt.grid(row=4, column=3)

    hmd_label = tk.Label(window, text='Humidity')
    hmd_label.grid(row=5, column=0)

    hmd_txt = tk.Text(window, width=20, height=1)
    hmd_txt.grid(row=5, column=1)

    slvl_label = tk.Label(window, text='Sea level')
    slvl_label.grid(row=5, column=2)

    slvl_txt = tk.Text(window, width=20, height=1)
    slvl_txt.grid(row=5, column=3)

    command = partial(fill_form, temp_txt, mint_txt, maxt_txt, wther_txt, des_txt, wspd_txt, wdgr_txt, hmd_txt, slvl_txt, name_txt, city_value)

    srch = tk.Button(window,  text='Search', command=command)
    srch.grid(row=0, column=2)

    window.mainloop()


if __name__ == '__main__':
    main()
