# Ask the user for mass, and convert it from text to a whole number
mass = int(input("Mass: "))
# Calculate the speed of light squared (part of E = mc^2)
c = 300000000**2
# Multiply mass by c-squared to get the energy, then display it
print(mass * c)
