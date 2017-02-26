#!/usr/bin/env python
import tkinter as tk
import requests
import json
import math
from functools import partial
import http.client

class Form:
    def __init__(self, temp_txt, mint_txt, maxt_txt, wther_txt, des_txt, wspd_txt,
                 wdgr_txt, hmd_txt, slvl_txt, name_txt):
        self.temp_txt = temp_txt
        self.mint_txt = mint_txt
        self.maxt_txt = maxt_txt
        self.wther_txt = wther_txt
        self.des_txt = des_txt
        self.wspd_txt = wspd_txt
        self.wdgr_txt = wdgr_txt
        self.hmd_txt = hmd_txt
        self.slvl_txt = slvl_txt
        self.name_txt = name_txt

def clear_form(form):
    form.temp_txt.delete(1.0, tk.END)
    form.mint_txt.delete(1.0, tk.END)
    form.maxt_txt.delete(1.0, tk.END)
    form.wther_txt.delete(1.0, tk.END)
    form.des_txt.delete(1.0, tk.END)
    form.wspd_txt.delete(1.0, tk.END)
    form.wdgr_txt.delete(1.0, tk.END)
    form.hmd_txt.delete(1.0, tk.END)
    form.slvl_txt.delete(1.0, tk.END)
    form.name_txt.delete(1.0, tk.END)

def web_request(form, city_value):
    citynm = city_value.get()
    params = dict(q=citynm, APPID='26ee310aed6872889843892aa2ff1c1b')
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params)
    if resp.status_code == http.client.OK:
        return resp.json()
    else:
        form.temp_txt.insert(tk.END, '↑Invalid city name↑')

def kelvin_to_celsius(value):
    return value - 273.15


def fill_form_main_section(form, info, na):
    # information from main section
    main_section = info.get('main')
    if main_section != None:
        # get temperature
        temp_avg = main_section.get('temp', na)
        if temp_avg != na:
            temp_avg = '%s °C' % int(round(kelvin_to_celsius(temp_avg)))
        form.temp_txt.insert(tk.END, temp_avg)

        # get min temperature
        temp_min = main_section.get('temp_min', na)
        if temp_min != na:
            temp_min = '%s °C' % int(math.floor(kelvin_to_celsius(temp_min)))
        form.mint_txt.insert(tk.END, temp_min)

        # get max temperature
        temp_max = main_section.get('temp_max', na)
        if temp_max != na:
            temp_max = '%s °C' % int(math.ceil(kelvin_to_celsius(temp_max)))
        form.maxt_txt.insert(tk.END, temp_max)

        # get humidity info
        humidity = main_section.get('humidity', na)
        if humidity != na:
            humidity = '%s %%' % humidity
        form.hmd_txt.insert(tk.END, humidity)

                    # get sea level info
        sea_level = main_section.get('sea_level', na)
        if sea_level != na:
            sea_level = '%s m' % sea_level
        form.slvl_txt.insert(tk.END, sea_level)

    else:
        form.temp_txt.insert(tk.END, na)
        form.mint_txt.insert(tk.END, na)
        form.maxt_txt.insert(tk.END, na)
        form.hmd_txt.insert(tk.END, na)
        form.slvl_txt.insert(tk.END,na)

def fill_form_weather_section(form, info, na):
    # information from weather section
    weather_section = info.get('weather')
    if weather_section != None:
        # get the weather info
        short_description = weather_section[0].get('main', na)
        form.wther_txt.insert(tk.END, short_description)

        # get the longer weather description
        long_description = weather_section[0].get('description', na)
        form.des_txt.insert(tk.END, long_description)
    else:
        form.wther_txt.insert(tk.END, na)
        form.des_txt.insert(tk.END, na)

def fill_form_wind_section(form, info, na):
    # wind section
    wind_section = info.get('wind')
    if wind_section != None:
        # get the wind speed info
        wind_speed = wind_section.get('speed', na)
        if wind_speed != na:
            wind_speed = '%s m/s' % wind_speed
        form.wspd_txt.insert(tk.END, wind_speed)

        # get the wind degree info
        wind_degree = wind_section.get('deg', na)
        if wind_degree != na:
            wind_degree = '%s °' % wind_degree
        form.wdgr_txt.insert(tk.END, wind_degree)

    else:
        form.wspd_txt.insert(tk.END, na)
        form.wdgr_txt.insert(tk.END, na)

def fill_form_name_section(form, info, na):
    # name section
    name_section = info.get('name', na)
    form.name_txt.insert(tk.END, name_section)

def fill_form(form, city_value):
    clear_form(form)
    info = web_request(form, city_value)
    na = 'n/a'

    if info != None:
        fill_form_main_section(form, info, na)
        fill_form_weather_section(form, info, na)
        fill_form_wind_section(form, info, na)
        fill_form_name_section(form, info, na)

def make_label(window, text, row, column):
    label = tk.Label(window, text=text, justify=tk.LEFT)
    label.grid(row=row, column=column)
    return label

def make_text(window, row, column, columnspan=None):
    txt = tk.Text(window, width=20, height=1)
    txt.grid(row=row, column=column, columnspan=columnspan)
    return txt


def main():
    window = tk.Tk()

    city_label = make_label(window, 'City', 0, 0)

    city_value = tk.StringVar()
    city_entry = tk.Entry(window, textvariable=city_value)
    city_entry.grid(row=0, column=1)

    make_label(window, 'Temperature', 1, 0)
    temp_txt = make_text(window, 1, 1)

    make_label(window, 'Station Name', 1, 2)
    name_txt = make_text(window, 1, 3)

    make_label(window, 'Min Temp', 2, 0)
    mint_txt = make_text(window, 2, 1)

    make_label(window, 'Max Temp', 2, 2)
    maxt_txt = make_text(window, 2, 3)

    make_label(window, 'Weather', 3, 0)
    wther_txt = make_text(window, 3, 1)

    make_label(window, 'Description', 3, 2)
    des_txt = make_text(window, 3, 3, 3)

    make_label(window, 'Wind speed', 4, 0)
    wspd_txt = make_text(window, 4, 1)

    make_label(window, 'Wind degree', 4, 2)
    wdgr_txt = make_text(window, 4, 3)

    make_label(window, 'Humidity', 5, 0)
    hmd_txt = make_text(window, 5, 1)

    make_label(window, 'Sea level', 5, 2)
    slvl_txt = make_text(window, 5, 3)

    form = Form(temp_txt, mint_txt, maxt_txt, wther_txt, des_txt, wspd_txt, wdgr_txt, hmd_txt, slvl_txt, name_txt)
    command = partial(fill_form, form, city_value)

    srch = tk.Button(window,  text='Search', command=command)
    srch.grid(row=0, column=2)

    window.mainloop()


if __name__ == '__main__':
    main()
