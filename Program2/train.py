iteration = 0
mileage = []
price = []
learning_rate = 0.1
with open("data.csv", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        miles, cost = line.split(",")
        mileage.append(int(miles))
        price.append(int(cost))

max_mileage = max(mileage)
max_price = max(price)    
mileage = [m / max_mileage for m in mileage]
price = [p / max_price for p in price]      
cars = len(mileage)
theta0 = 0.0
theta1 = 0.0
while iteration < 1000 :
    errors = []
    for i in range(cars):
        prediction = theta0 + (theta1 * mileage[i])
        errors.append(prediction - price[i])
    tmp_theta0 = learning_rate * (1/cars) * sum(errors)
    tmp_theta1 = learning_rate * (1/cars) * sum(e * m for e, m in zip(errors, mileage))

    theta0 = theta0 - tmp_theta0
    theta1 = theta1 - tmp_theta1
    print("theta0: ", theta0)
    print("theta1: ", theta1)
    iteration += 1
with open("../Program1/theta", "w") as f:
    f.write(f"{theta0}\n")
    f.write(f"{theta1}\n")
