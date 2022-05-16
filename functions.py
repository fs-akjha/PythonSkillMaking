#Problem:- You are given two lists of numbers and you need to find total of each of these list

a_exp_list=[2100,3400,3500]
b_exp_list=[200,500,700]

def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

a_total_exp=calculate_total(a_exp_list)
b_total_exp=calculate_total(b_exp_list)

print("A's Total Expenses: ",a_total_exp)
print("B's Total Expenses: ",b_total_exp)