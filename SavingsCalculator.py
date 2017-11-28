import logging
logging.basicConfig(level = logging.DEBUG)


def calculateSavings():
    print('Please enter how much income you expect to make every week' )
    weeklyIncome = int(input())
    print('Please enter number of weeks you expect to work')
    weeks = int(input())

    taxPercentage = taxBracket(weeklyIncome) #What percentage you will be taxed at
    taxedAmount = weeklyIncome*taxPercentage #How much money will be taken out based on the percentage
    netIncome = weeklyIncome-taxedAmount #Your netIncome

    savings = 0
    for x in range(1, weeks+1):
        savings += float(netIncome)*.15
    netIncome *= weeks

    print('In ' + str(x) + ' weeks, you have saved $' + str(int(savings)) + ' from $' + str(int(netIncome)) + ' Your tax bracket value is '
          + str(float(taxPercentage)))
    #We want to write something like, how much you made from x amount of money.


def taxBracket(weeklyIncome):
    annualIncome = weeklyIncome*weeks #50 because of number of working weeks || Artekka: Changed to weeks to reflect accurate tax bracket
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

calculateSavings()


