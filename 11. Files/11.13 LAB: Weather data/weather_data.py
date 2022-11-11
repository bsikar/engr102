#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 11.13 LAB: Weather data
# Date: 11 11 2022

# open file
with open("WeatherDataCLL.csv") as f:
    lines = list(f)
    header = lines.pop(0).split(",")
    # convert header into a dict with index as value
    header = {header[i].strip(): i for i in range(len(header))}
    max_temp = float(lines[0].split(",")[header["Maximum Temperature (F)"]])
    min_temp = float(lines[0].split(",")[header["Minimum Temperature (F)"]])
    average_precipitation = 0

    for line in lines:
        # check if max_temp is less than current line's max_temp
        curr_max_temp = float(line.split(",")[header["Maximum Temperature (F)"]])
        if curr_max_temp > max_temp:
            max_temp = curr_max_temp
        # check if min_temp is greater than current line's min_temp
        curr_min_temp = float(line.split(",")[header["Minimum Temperature (F)"]])
        if curr_min_temp < min_temp:
            min_temp = curr_min_temp
        # add current line's precipitation to average_precipitation
        curr_precipitation = line.split(",")[header["Precipitation (in)"]]
        average_precipitation += float(curr_precipitation)
    # divide average_precipitation by number of lines
    average_precipitation /= len(lines)

    print(f"3-year maximum temperature: {max_temp:.0f} F")
    print(f"3-year minimum temperature: {min_temp:.0f} F")
    print(f"3-year average precipitation: {average_precipitation:.3f} inches\n")

    # get user input for month and year
    month = input("Please enter a month: ")
    year = int(input("Please enter a year: "))
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    month = months[month]

    mean_max_temp = 0
    mean_wind_speed = 0
    percentage_precipitation = 0
    count = 0
    for line in lines:
        # get month and year from line
        curr_date = line.split(",")[header["Date"]]
        curr_month = int(curr_date.split("/")[0])
        curr_year = int(curr_date.split("/")[2])
        # check if month and year match user input
        if curr_month == month and curr_year == year:
            # add max temp, wind speed, and precipitation to their respective variables
            mean_max_temp += float(line.split(",")[header["Maximum Temperature (F)"]])
            mean_wind_speed += float(line.split(",")[header["Average Daily Wind Speed (mph)"]])
            precipitation = float(line.split(",")[header["Precipitation (in)"]])
            if precipitation > 0:
                percentage_precipitation += 1
            count += 1
    # divide by count
    mean_max_temp /= count
    mean_wind_speed /= count
    percentage_precipitation /= count
    percentage_precipitation *= 100

    month = list(months.keys())[list(months.values()).index(month)]
    print(f"\nFor {month} {year}:")
    print(f"Mean maximum daily temperature: {mean_max_temp:.1f} F")
    print(f"Mean daily wind speed: {mean_wind_speed:.2f} mph")
    print(f"Percentage of days with precipitation: {percentage_precipitation:.1f}%")
