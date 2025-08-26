import matplotlib.pyplot as plt
import math

mileages = []
price = []
x = []
y = []
with open("../Program2/data.csv", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        miles, cost = line.split(",")
        mileages.append(int(miles))
        price.append(int(cost))
try:
    with open("../Program1/theta", "r") as f:
        lines = f.readlines()
        theta0 = float(lines[0].strip())
        theta1 = float(lines[1].strip())
    for i in range (len(mileages)):
        y.append(mileages[i])
        mileage = float(mileages[i]) / max(mileages)
        estimatPrice = theta0 + (theta1 * mileage)
        x.append(estimatPrice * max(price))
except ValueError:
    print("Something goes wrong")
mse = sum((p - a) ** 2 for p, a in zip(x, price)) / len(mileages)
rmse = math.sqrt(mse)
rmse = f"{rmse:.2f}$"
print("RMSE: ", rmse)
plt.plot(x, y, color="blue", label="Regression line")
plt.plot(price, mileages, color="red", label="Regression line")
plt.ylabel("Mileage (km)")
plt.xlabel("Predicted Price (€)")
plt.title("Regression Result")
plt.legend()
plt.grid(True)
plt.show()