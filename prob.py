import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. Define distribution parameters (e.g., Normal Distribution: mean = 0, std = 1)
mu, std = 0, 1

# 2. Calculate probability values (PDF and CDF)
x_val = 1.96
pdf_value = stats.norm.pdf(x_val, loc=mu, scale=std)
cdf_value = stats.norm.cdf(x_val, loc=mu, scale=std)
print(f"PDF at x={x_val}: {pdf_value:.4f}")
print(f"CDF at x={x_val}: {cdf_value:.4f}")

# 3. Generate data for histogram and fitted curve visualization
data = np.random.normal(mu, std, 1000)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)

# Plotting
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Sample Data Histogram')
plt.plot(x, p, 'k--', linewidth=2, label='Fitted Normal Curve')
plt.title("Probability Distribution: Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()