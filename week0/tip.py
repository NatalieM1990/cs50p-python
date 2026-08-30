def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Remove the dollar sign and convert the remaining amount to a decimal number
def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)

# Remove the percent sign, convert to a decimal number, then divide by 100
def percent_to_float(p):
     p = p.replace("%", "")
     return float(p) / 100


main()