# Exercise 02
# Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead. 
# However, the output is the same every time the function is invoked. Why? 
# Fix the code so that it behaves as expected.

import random

def predict_weather():
#    sunshine = random.choice(['True', 'False'])
# Will error because the above are strings. True and False must be boolean values for this to work. Replacing with boolean values in below line.
    sunshine = random.choice([True, False])
    sunshine = False
    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()
