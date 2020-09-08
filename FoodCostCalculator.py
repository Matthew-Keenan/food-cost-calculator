# Calculate how much everyones owes for an order
# Percent of total food order (including tip) determines percent of delivery fee (including tip) each person owes
def howManyPeople():
    numPeople = eval(input("How many people are included? "))

    return numPeople
# Test Edit
def costs(numPeople):
    peopleOwe = []
    totalCost = 0
    for i in range(1, numPeople + 1):
        items = eval(input(f"How many items does person {i} have? "))
        indCost = 0
        for a in range(items):
            cost = eval(input(f"How much is item {a + 1}? "))
            indCost += cost
            totalCost += cost
        peopleOwe.append(indCost)
        print()

    return peopleOwe, totalCost

def personOwe(totalCost, peopleOwe):
    percents = []
    for num in peopleOwe:
        percent = num / totalCost
        percents.append(percent)

    delivery = eval(input("How much is delivery? "))
    tax = eval(input("How much is the sales tax? "))
    delTip = eval(input("How much is the delivery tip? "))
    totDelivery = delivery + tax + delTip

    delOwe = []
    for p in percents:
        personDelivery = p * totDelivery
        delOwe.append(personDelivery)
    print()

    print("Total Cost:" + " $"+ str(totalCost + totDelivery))
    for i in range(len(delOwe)):
        personTotal = peopleOwe[i] + delOwe[i]
        print("Person {0} owes ${1:.2f} for food, ${2:.2f} for delivery, ${3:.2f} in total.".format(i + 1, peopleOwe[i], delOwe[i], personTotal))

def main():
    numPeople = howManyPeople()
    print()
    peopleOwe, totalCost = costs(numPeople)
    print()
    personOwe(totalCost, peopleOwe)
    close = input("Press any key to close")
main()
