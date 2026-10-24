import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# load data set
data = pd.read_csv("experience_salary.csv")

X = data[["YearsExperience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(X, y)

data["PredictedSalary"] = model.predict(X)

print("Coefficient:", model.coef_)
print("Coefficient shape:", model.coef_.shape)
print("Model Coefficient (slope)", round(model.coef_.item(), 2))

print("Model INtercept (base salary)", round(model.intercept_.item()), 2)

plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, data["PredictedSalary"], color="red", label="Regression line")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()