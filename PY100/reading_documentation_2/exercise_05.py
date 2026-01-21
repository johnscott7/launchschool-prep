# Exercise 05
# The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.
from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

# What is the difference between the year attribute and the isocalendar method?
# year returns the year of the date
# isolendar returns the year, week number, and weekday as a tuple.