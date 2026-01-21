# Exercise 02
# In the following code snippet, find all violations of the PEP8 style guide. Rewrite it so that it conforms with the guide.

iceCreamDensity=10 # Should have spaces around =. Should use snake_case for variable name

while iceCreamDensity>0 : # spaces around >, none before :
    print('Drip...')
    iceCreamDensity-=1 # spaces around -= 

print('The ice cream melted.')

# Fixed:

ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')