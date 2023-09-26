#!usr/bin/env/ python3
# Created By: Marli Peters
# Date: Sep. 25, 2023
# This program calculates area and perimeter of a rectangle with user input.


def main():
    # Collecting length and width.

    length = int(input("Enter length (cm): "))
    width = int(input("Enter width (cm): "))

    # Printing solution.

    print("")
    print("Area is {}cm^2".format(length * width))
    print("Perimeter is {}cm".format(2 * (length + width)))
if __name__ == "__main__":
    main()
