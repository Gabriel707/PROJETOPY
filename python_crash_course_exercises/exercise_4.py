huge_nums = list(range(1, 1000001))

list_lenght = print(f'huge_nums list lenght = {len(huge_nums)}')

huge_nums_pt1 = []
huge_nums_pt2 = []
huge_nums_pt3 = []

for num in huge_nums:
    if num <= 300000:
        huge_nums_pt1.append(num)
    elif num > 300000 and num <= 600000:
        huge_nums_pt2.append(num)
    elif num > 600000:
        huge_nums_pt3.append(num)
    else:
        print("Please check your code...")

print(f"PART I: \n{huge_nums_pt1}\n")
print(f"PART II: \n{huge_nums_pt2}\n")
print(f"PART III: \n{huge_nums_pt3}\n")
