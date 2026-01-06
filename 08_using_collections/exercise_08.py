# Exercise 08
# Explain why the code below prints different values.
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# The first one slices the text into 'for the fjords!'
# f is the 8-indexed character in that string
# The second one searches for f in that same character range, but the indexes are not reset from zero, so f in that range is 29.