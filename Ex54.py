print("Program to tell the visible spectrum  of a wave from its wavelength")

wavelength = int(input("Enter the wavelength "))

if (wavelength>380 and wavelength<450):
    print("The visible spectrum of this wave is Violet")
elif (wavelength>=450 and wavelength<495):
    print("The visible spectrum of this wave is Blue")
elif (wavelength>=495 and wavelength<570):
    print("The visible spectrum of this wave is Green")
elif (wavelength>=570 and wavelength<590):
    print("The visible spectrum of this wave is Yellow")
elif (wavelength>=590 and wavelength<620):
    print("The visible spectrum of this wave is Orange")
elif (wavelength>=620 and wavelength<750):
    print("The visible spectrum of this wave is Red")
else:
    print("Invalid Entry")