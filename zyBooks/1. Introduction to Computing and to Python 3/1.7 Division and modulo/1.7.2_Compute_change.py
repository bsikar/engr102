amount_to_change = int(input())

num_fives = amount_to_change // 5

num_ones = amount_to_change % 5

print("Change for $", amount_to_change)
print(num_fives, "$5 bill(s) and", num_ones, "$1 bill(s)")
