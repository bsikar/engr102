# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   5.3 LAB: Diabetes risk
# Date:         9 26 2022
from math import e


# background:
# The score was created from a notional population that was formed by random selection and pooling of 
# two separate data sets. One data set came from a population-based sample of 1077 people, aged 40 to 
# 64 years, without known diabetes, from a single Cambridgeshire general practice who underwent 
# clinical assessment including an oral glucose tolerance test. The other data set came from a 12-month 
# study in which 41 practices in southern England reported clinical details of patients aged 40 to 64 years 
# with newly diagnosed Type 2 diabetes. Data were entered into a regression model to produce a formula 
# predicting the risk of diabetes. 
# The performance of this risk score in detecting diabetes was tested in an independent, randomly 
# selected, population-based sample. In the test population at 72% specificity, the sensitivity of the score 
# was 77% and likelihood ratio 2.76. The area under the receiver-operating characteristic curve was 80%. 

# user input
sex = input("Enter your sex (M/F): ").lower()
if sex == "m":
    sex = 0
else: 
    sex = 0.879


age = float(input("Enter your age (years): "))

bmi = float(input("Enter your BMI: "))
if bmi < 25: 
    bmi = 0
elif bmi <= 27.49: 
    bmi = 0.699
elif bmi <= 29.99: 
    bmi = 1.97
else: 
    bmi = 2.518

hypertension = input("Are you on medication for hypertension (Y/N)? ").lower()
if hypertension == "y": 
    hypertension = 1.222
else: 
    hypertension = 0

steroids = input("Are you on steroids (Y/N)? ").lower()

if steroids == "y": 
    steroids = 2.191
else: 
    steroids = 0

cigarettes = input("Do you smoke cigarettes (Y/N)? ").lower()
if cigarettes == "y": 
    cigarettes = True
else: 
    cigarettes = False


# if they didnt smoke maybe they did in the past
if cigarettes: 
    smoke = 0.855
else:
    smoke = input("Did you used to smoke (Y/N)? ").lower()
    if smoke == "y": 
        smoke = -0.218
    else: 
        smoke = 0

# if the history was yes maybe their sibling and parent both had it
history = input("Do you have a family history of diabetes (Y/N) ? ").lower()
if history == "y":
    both = input("Both parent and sibling (Y/N)? ").lower()
    if both == "y": 
        history = 0.753
    else: 
        history = 0.728
else: 
    history = 0

# calculations
n = 6.322 + sex - (0.063 * age) - bmi - hypertension - steroids - smoke - history
risk = 100 / (1 + e ** n)

print(f"Your risk of developing type-2 diabetes is {risk:.1f}%")