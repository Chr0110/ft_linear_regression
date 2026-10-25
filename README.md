# ft_linear_regression

A from-scratch linear regression that predicts the price of a car from its mileage, trained with gradient descent.

## Problem

Given a dataset of used cars (`data.csv`) with two columns:

| km | price |
|---|---|
| 240000 | 3650 |
| 139800 | 3800 |
| ... | ... |

Find the relationship between mileage and price, then use it to estimate the price of a car for any mileage entered by the user.

Constraint: the model and the training loop are coded by hand, with no ML library doing the fitting.

## Solution

### Model

A straight line with two parameters:

```
estimatePrice(mileage) = θ0 + θ1 × mileage
```

- `θ0`: intercept (price at 0 km)
- `θ1`: slope (price change per km, expected to be negative)

### Training: gradient descent

Starting from `θ0 = θ1 = 0`, both parameters are updated at each iteration to reduce the error:

```
tmpθ0 = α × 1/m × Σ (estimatePrice(km_i) - price_i)
tmpθ1 = α × 1/m × Σ (estimatePrice(km_i) - price_i) × km_i

θ0 -= tmpθ0
θ1 -= tmpθ1
```

- `m`: number of samples
- `α`: learning rate
- Both parameters are updated **simultaneously** (computed first, applied after).

### Normalization

Mileage (~10⁵) and price (~10³) have very different scales, which makes gradient descent slow or divergent. The data is normalized before training, and θ is converted back to the original scale afterward so predictions work on raw mileage.

### Programs

| Program | Role |
|---|---|
| `train` | Reads `data.csv`, runs gradient descent, saves `θ0` and `θ1` to a file |
| `predict` | Loads the saved θ (0 if none), asks for a mileage, prints the estimated price |

### Bonus

- Plot of the data points and the fitted line
- Precision metrics of the model (e.g. MSE, R²)

## Usage

```bash
python3 train.py
python3 predict.py
# Enter a mileage: 100000
# Estimated price: ...
```

> Adjust script names to match your repo.

## Concepts covered

- Supervised learning and linear hypothesis
- Cost function (mean squared error)
- Gradient descent and learning rate
- Feature scaling
- Model evaluation
