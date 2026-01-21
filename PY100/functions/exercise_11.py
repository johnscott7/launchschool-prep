# Exercise 11
# Building on your solutions from the previous exercises, write a function local_greet that takes a locale as input, and returns a greeting. 
# The locale lets us greet people from different countries appropriately, even when they share a common language, for example:

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hello'
        case 'fr':
            return 'Salut!'
        case 'ca':
            return 'Oh hey there'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Wagwan'
        case ('en', 'AU'):
            return 'Oy mate'
        case _:
            return greet(language)
