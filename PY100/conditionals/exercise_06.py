# Exercise 06
# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. 
# Feel free to add more cases besides 'sunny' and 'rainy'.

weather = 'snowy'
match weather:
    case 'rainy':
        print('Grab your umbrella!')
    case 'sunny':
        print("It's a beautiful day!")
    case 'cloudy':
        print("It's so gloomy out")
    case _:
        print("Let's stay inside")