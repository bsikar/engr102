# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   11.9 LAB: Passport checker Part A
# Date:         11 11 2022

required_fields = ["byr", "iyr", "eyr", "hgt", "ecl", "pid", "cid"]

file = input("Enter the name of the file: ")

valid_count = 0
output_file = open("valid_passports.txt", "w")
with open(file, "r") as f:
    passports = f.read().split("\n\n")
    for passport in passports:
        fields = passport.replace("\n", " ").split(" ")
        field_names = [field.split(":")[0] for field in fields]
        if all(field in field_names for field in required_fields):
            # write to file
            output_file.write(passport + "\n\n")
            valid_count += 1
# close file
output_file.close()
print(f"There are {valid_count} valid passports")
