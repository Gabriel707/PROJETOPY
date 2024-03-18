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

num_to_be_checked = int(input('Insert number to be checked: '))
if num_to_be_checked in huge_nums_pt1:
    print(f"{num_to_be_checked} is present on huge_nums_part1.\n")
elif num_to_be_checked in huge_nums_pt2:
    print(f"{num_to_be_checked} is present on huge_nums_part2.\n")
elif num_to_be_checked in huge_nums_pt3:
    print(f"{num_to_be_checked} is present on huge_nums_part3")

# print(f"PART I: \n{(min(huge_nums_pt1), (max(huge_nums_pt1)))}\n")
# print(f"PART II: \n{(min(huge_nums_pt2), (max(huge_nums_pt2)))}\n")
# print(f"PART II: \n{(min(huge_nums_pt3), (max(huge_nums_pt3)))}\n")
