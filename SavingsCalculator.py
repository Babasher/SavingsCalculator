import logging
logging.basicConfig(level = logging.DEBUG)


def calculateSavings():
    print('Please enter how much income you expect to make every week' )
    weeklyIncome = int(input())
    print('Please enter number of weeks you expect to work')
    weeks = int(input())

    def taxBracket(weeklyIncome):
        annualIncome = weeklyIncome*weeks
        if (annualIncome > 418400):
            return 0.396
        elif (annualIncome >= 416700):
            return 0.35
        elif (annualIncome >= 191650):
            return 0.33
        elif (annualIncome >= 91900):
            return  0.28
        elif (annualIncome >= 37950):
            return 0.25
        elif (annualIncome >= 9325):
            return 0.15
        elif (annualIncome >= 0):
            return 0.10

    taxPercentage = taxBracket(weeklyIncome) #What percentage you will be taxed at
    taxedAmount = weeklyIncome*taxPercentage #How much money will be taken out based on the percentage
    netIncome = weeklyIncome-taxedAmount #Your netIncome


    print("Please enter the preferred savings % ")
    preferredSavings = int(input())

    savings = 0
    for x in range(1, weeks+1):
        savings += float(netIncome)*(preferredSavings/100)
    netIncome *= weeks

    print("In {} weeks, you have saved ${} from ${}. Your tax bracket value is "
          "{}%.".format(str(x),str(int(savings)),str(int(netIncome)),str(float(taxPercentage*100))))
    #We want to write something like, how much you made from x amount of money.
calculateSavings()

