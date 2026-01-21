# Exercise 10
# Similar to the previous exercise, write a function that extracts the region code from a locale. For example:

def extract_region(locale):
    locale2 = locale.split('_')[1]
    return locale2.split('.')[0] 

print(extract_region('en_US.UTF-8'))
print(extract_region('en_GB.UTF-8'))
print(extract_region('ko_KR.UTF-16'))
