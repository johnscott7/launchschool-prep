# Exercise 01
name = "Victor"
profession = "programmer"

# How can you print the string Hello, Victor. You are a programmer. using the str.format method?
# You should fill in the name and profession in a string literal that contains the rest of the text. 

str_form = "Hello, {}. You are a {}."
greeting_text = str_form.format(name, profession)
print(greeting_text)

# How can you achieve the same result using an f-string?
fstring_text = f"Hello, {name}. You are a {profession}."
print(fstring_text)


