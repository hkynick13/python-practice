
def annualPercentages(ammount, salaryAnnually):
    percentage = (ammount / salaryAnnually) * 100
    return percentage

def taxAmmount(salaryAnnually):
    if salaryAnnually <= 14999:
        taxAnnually = salaryAnnually * (10 / 100)
        return taxAnnually
    elif salaryAnnually >= 15000 and salaryAnnually <= 74999:
        taxAnnually = salaryAnnually * (20 / 100)
        return taxAnnually
    elif salaryAnnually >= 75000 and salaryAnnually <= 200000:
        taxAnnually = salaryAnnually * (25 / 100)
        return taxAnnually
    else:
        taxAnnually = 50000
        return taxAnnually

def main():
    print("-----------------------------")
    print("----- WHERE'S THE MONEY -----")
    print("-----------------------------")
    salaryAnnually = int(input("What is your annual salary?\n"))
    rentMonthly = int(input("How much is your monthly mortgage or rent?\n"))
    billsMonthly = int(input("What do you spend on bills monthly?\n"))
    foodWeekly = int(input("What are your weekly grocery/food expenses?\n"))
    travelAnnually = int(input("What do you spend on travel annually?\n"))
    rentAnnually = rentMonthly * 12
    billsAnnually = billsMonthly * 12
    foodAnnually = foodWeekly * 52
    taxAnnually = taxAmmount(salaryAnnually)
    rentPercentage = annualPercentages(rentAnnually, salaryAnnually)
    billsPercentage = annualPercentages(billsAnnually, salaryAnnually)
    foodPercentage = annualPercentages(foodAnnually, salaryAnnually)
    travelPercentage = annualPercentages(travelAnnually, salaryAnnually)
    taxPercentage = annualPercentages(taxAnnually, salaryAnnually)
    extraAnually = salaryAnnually - rentAnnually - billsAnnually - foodAnnually - travelAnnually - taxAnnually

    print()
    print("-----------------------------------------" + "-" * int(max(rentPercentage, billsPercentage, foodPercentage, travelPercentage, taxPercentage, (extraAnually / salaryAnnually * 100))))
    print("See the financial breakdown below, based on a salary of $" , salaryAnnually)
    print("-----------------------------------------" +  "-" * int(max(rentPercentage, billsPercentage, foodPercentage, travelPercentage, taxPercentage, (extraAnually / salaryAnnually * 100))))
    print("| mortgage/rent | $" + (" " * (10 - len(str(rentAnnually)))) + str(rentAnnually) + " |" + (" " * (6 - len(str(rentPercentage)))) + str(rentPercentage)  + "% | " + "#" * int(rentPercentage))
    print("| bills         | $" + (" " * (10 - len(str(billsAnnually)))) + str(billsAnnually) + " |" + (" " * (6 - len(str(billsPercentage)))) + str(billsPercentage) + "% | " + "#" * int(billsPercentage))
    print("| food          | $" + (" " * (10 - len(str(foodAnnually)))) + str(foodAnnually) + " |" + (" " * (6 - len(str(foodPercentage)))) + str(foodPercentage) + "% | " + "#" * int(foodPercentage))
    print("| travel        | $" + (" " * (10 - len(str(travelAnnually)))) + str(travelAnnually) + " |" + (" " * (6 - len(str(travelPercentage)))) + str(travelPercentage) + "% | " + "#" * int(travelPercentage))
    print("| tax           | $" + (" " * (10 - len(str(taxAnnually)))) + str(taxAnnually) + " |" + (" " * (6 - len(str(taxPercentage))))  + str(taxPercentage) + "% | " + "#" * int(taxPercentage))
    print("| extra         | $" + (" " * (10 - len(str(extraAnually))))  + str(extraAnually)  + " |" + (" " * (6 - len(str(extraAnually / salaryAnnually * 100)))) + (str(extraAnually / salaryAnnually * 100)) + "% | " + "#" * int(extraAnually / salaryAnnually * 100))

main()
