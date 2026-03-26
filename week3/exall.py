# ============================================================
# SciPy Exercises — All in One
# ============================================================

import scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm, binom

print("=" * 50)
print("EXERCISE 1 — SciPy Version")
print("=" * 50)
print(f"SciPy version : {scipy.__version__}")
print(f"NumPy version : {np.__version__}")
print(f"Pandas version: {pd.__version__}")


# ============================================================
print("\n" + "=" * 50)
print("EXERCISE 2 — Descriptive Statistics")
print("=" * 50)
data = [12, 15, 13, 12, 18, 20, 22, 21]

mean     = np.mean(data)
median   = np.median(data)
variance = stats.tvar(data)
std      = stats.tstd(data)

print(f"Mean     : {mean:.2f}")
print(f"Median   : {median:.2f}")
print(f"Variance : {variance:.2f}")
print(f"Std Dev  : {std:.2f}")


# ============================================================
print("\n" + "=" * 50)
print("EXERCISE 3 — Normal Distribution")
print("=" * 50)
mu, sigma = 50, 10
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 300)
y = norm.pdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(10, 5))
plt.plot(x, y, color="steelblue", lw=2.5)
plt.fill_between(x, y, alpha=0.3, color="steelblue")
plt.axvline(mu, color="red", linestyle="--", label=f"Mean = {mu}")
plt.title("Exercise 3 — Normal Distribution (μ=50, σ=10)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.tight_layout()
plt.show()
print("Normal distribution plotted ✅")


# ============================================================
print("\n" + "=" * 50)
print("EXERCISE 4 — T-Test")
print("=" * 50)
np.random.seed(42)
data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)

t_stat, p_value = stats.ttest_ind(data1, data2)

print(f"T-statistic : {t_stat:.4f}")
print(f"P-value     : {p_value:.4f}")
if p_value < 0.05:
    print("✅ Significant difference between the two groups (reject H0)")
else:
    print("❌ No significant difference (fail to reject H0)")


# ============================================================
print("\n" + "=" * 50)
print("EXERCISE 5 — Linear Regression")
print("=" * 50)
house_sizes  = [50, 70, 80, 100, 120]
house_prices = [150000, 200000, 210000, 250000, 280000]

result = stats.linregress(house_sizes, house_prices)

print(f"Slope     : {result.slope:.2f}  → each extra m² adds {result.slope:.0f} units")
print(f"Intercept : {result.intercept:.2f}")
print(f"R²        : {result.rvalue**2:.4f}")
print(f"P-value   : {result.pvalue:.6f}")

predicted_price = result.slope * 90 + result.intercept
print(f"Predicted price for 90m² : {predicted_price:,.0f} currency units")

x_line = np.linspace(40, 130, 200)
y_line = result.slope * x_line + result.intercept

plt.figure(figsize=(9, 5))
plt.scatter(house_sizes, house_prices, color="steelblue", s=80, zorder=5, label="Data")
plt.plot(x_line, y_line, color="red", lw=2, label="Regression line")
plt.scatter(90, predicted_price, color="green", s=150, zorder=6,
            marker="*", label=f"Prediction 90m² = {predicted_price:,.0f}")
plt.title("Exercise 5 — Housing Prices Linear Regression")
plt.xlabel("Size (m²)")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.show()


# ============================================================
print("\n" + "=" * 50)
print("EXERCISE 6 — ANOVA")
print("=" * 50)
fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]

f_stat, p_value = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

print(f"F-value : {f_stat:.4f}")
print(f"P-value : {p_value:.4f}")
if p_value < 0.05:
    print("✅ Fertilizers have significantly different effects (reject H0)")
else:
    print("❌ No significant difference between fertilizers (fail to reject H0)")
print("📌 If p > 0.05 : we cannot conclude any fertilizer is more effective.")


# ============================================================
print("\n" + "=" * 50)
print("EXERCISE 7 — Binomial Distribution (Optional)")
print("=" * 50)
n, p, k = 10, 0.5, 5
prob = binom.pmf(k, n, p)
print(f"P(exactly 5 heads in 10 flips) = {prob:.4f} = {prob*100:.2f}%")

x_binom = np.arange(0, 11)
y_binom = binom.pmf(x_binom, n, p)

plt.figure(figsize=(9, 4))
plt.bar(x_binom, y_binom, color="steelblue", alpha=0.7, edgecolor="white")
plt.bar(k, binom.pmf(k, n, p), color="red", alpha=0.9, label=f"k=5 : {prob:.3f}")
plt.title("Exercise 7 — Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.legend()
plt.tight_layout()
plt.show()


# ============================================================
print("\n" + "=" * 50)
print("EXERCISE 8 — Correlation Coefficients (Optional)")
print("=" * 50)
data_corr = pd.DataFrame({
    'age':    [23, 25, 30, 35, 40],
    'income': [35000, 40000, 50000, 60000, 70000]
})

pearson_r,  p_pearson  = stats.pearsonr(data_corr['age'], data_corr['income'])
spearman_r, p_spearman = stats.spearmanr(data_corr['age'], data_corr['income'])

print(f"Pearson  r = {pearson_r:.4f},  p = {p_pearson:.4f}")
print(f"Spearman ρ = {spearman_r:.4f},  p = {p_spearman:.4f}")
print("📌 Both are close here because the relationship is almost perfectly linear.")

print("\n" + "=" * 50)
print("✅ ALL EXERCISES COMPLETE !")
print("=" * 50)