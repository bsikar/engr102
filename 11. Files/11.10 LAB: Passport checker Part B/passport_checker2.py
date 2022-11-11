# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   11.10 LAB: Passport checker Part B
# Date:         11 11 2022

required_fields = ["byr", "iyr", "eyr", "hgt", "ecl", "pid", "cid"]

file = input("Enter the name of the file: ")

valid_count = 0
output_file = open("valid_passports2.txt", "w")
with open(file, "r") as f:
    passports = f.read().split("\n\n")
    for passport in passports:
        fields = passport.replace("\n", " ").split(" ")
        field_names = [field.split(":")[0] for field in fields]
        if all(field in field_names for field in required_fields):
            # check byr is btw [1920, 2005]
            byr = [field for field in fields if field.startswith("byr")][0].split(":")[1]
            if not (1920 <= int(byr) <= 2005):
                continue
            # check iyr is btw [2012, 2022]
            iyr = [field for field in fields if field.startswith("iyr")][0].split(":")[1]
            if not (2012 <= int(iyr) <= 2022):
                continue
            # check eyr is btw [2022, 2032]
            eyr = [field for field in fields if field.startswith("eyr")][0].split(":")[1]
            if not (2022 <= int(eyr) <= 2032):
                continue
            # check hgt is btw [150, 193]cm or [59, 76]in
            hgt = [field for field in fields if field.startswith("hgt")][0].split(":")[1]
            if hgt.endswith("cm"):
                if not (150 <= int(hgt[:-2]) <= 193):
                    continue
            elif hgt.endswith("in"):
                if not (59 <= int(hgt[:-2]) <= 76):
                    continue
            else:
                continue
            # check ecl is one of amb blu brn gry grn hzl oth
            ecl = [field for field in fields if field.startswith("ecl")][0].split(":")[1]
            if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue
            # check pid is 9 digits
            pid = [field for field in fields if field.startswith("pid")][0].split(":")[1]
            if not (len(pid) == 9 and all(c in "0123456789" for c in pid)):
                continue
            # check cid is a 3 digit number with leading 0s
            cid = [field for field in fields if field.startswith("cid")][0].split(":")[1]
            if len(str(int(cid))) != 3:
                continue
            # write to file
            valid_count += 1
            output_file.write(passport + "\n\n")
# close file
output_file.close()
print(f"There are {valid_count} valid passports")
