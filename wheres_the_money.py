
def annualPercentages(ammount: str, salaryAnnually: str):
    percentage = ammount % salaryAnnually
    return percentage

def taxAmmount(salaryAnnually: str):
    if salaryAnnually <= "14999":
        taxAnnually = salaryAnnually * (10 % 100)
        return taxAnnually
    elif salaryAnnually >= "15000" and salaryAnnually <= "74999":
        taxAnnually = salaryAnnually * (20 % 100)
        return taxAnnually
    elif salaryAnnually >= "75000" and salaryAnnually <= "200000":
        taxAnnually = salaryAnnually * (25 % 100)
        return taxAnnually
    else:
        taxAnnually = "50000"
        return taxAnnually
        print(">>> TAX LIMIT REACHED <<<")

def main():
    print("-----------------------------")
    print("----- WHERE'S THE MONEY -----")
    print("-----------------------------")
    salaryAnnually = input("What is your annual salary?\n")
    rentMonthly = input("How much is your monthly mortgage or rent?\n")
    billsMonthly = input("What do you spend on bills monthly?\n")
    foodWeekly = input("What are your weekly grocery/food expenses?\n")
    travelAnnually = input("What do you spend on travel annually?\n")
    rentAnnually = rentMonthly * 12
    billsAnnually = billsMonthly * 12
    foodAnnually = foodWeekly * 52
    taxAnnually = taxAmmount(salaryAnnually)
    rentPercentage = annualPercentages(rentAnnually, salaryAnnually)
    billsPercentage = annualPercentages(billsAnnually, salaryAnnually)
    foodPercentage = annualPercentages(foodAnnually, salaryAnnually)
    travelPercentage = annualPercentages(travelAnnually, salaryAnnually)
    taxPercentage = annualPercentages(taxAnnually, salaryAnnually)

    print()
    print("------------------------------------------------------------------------------------------------------")
    print("See the financial breakdown below, based on a salary of $" , salaryAnnually)
    print("------------------------------------------------------------------------------------------------------")
    print("| mortgage/rent | $  " , rentAnnually , " |  " , rentPercentage  , "% | ")
    print("| bills | $  " , billsAnnually , " |  " , billsPercentage , "% | "  )
    print("| food | $  " , foodAnnually , " |  " , foodPercentage , "% | "   )
    print("| travel | $  " , travelAnnually , " |  " , foodPercentage , "% | "  )
    print("| tax | $  " , taxPercentage() , " |  " , taxAnnually , "% | "   )
    print("| extra | $  " , salaryAnnually - rentAnnually - billsAnnually - foodAnnually - travelAnnually - taxAnnually  , " |  " , (billsAnnually / salaryAnnually) , "% | "  )

main()
