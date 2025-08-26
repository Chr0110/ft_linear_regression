mileage = input("Enter the mileage: ")
mileages = []
price = []
with open("../Program2/data.csv", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        miles, cost = line.split(",")
        mileages.append(int(miles))
        price.append(int(cost))
try:
    with open("theta", "r") as f:
        lines = f.readlines()
        theta0 = float(lines[0].strip())
        theta1 = float(lines[1].strip())
    mileage = float(mileage) / max(mileages)
    estimatPrice = theta0 + (theta1 * mileage)
    realprice = estimatPrice * max(price)
    print("the price is:", realprice)
except ValueError:
    print("Please enter a number!")