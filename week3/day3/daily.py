# ============================================================
# Daily Challenge — Analysis of Airplane Crashes & Fatalities
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

plt.rcParams["figure.figsize"] = (13, 5)
plt.rcParams["font.size"] = 12

# ============================================================
# PART 1 — DATA IMPORT AND CLEANING
# ============================================================
print("=" * 55)
print("PART 1 — Data Import and Cleaning")
print("=" * 55)

try:
    df = pd.read_csv(
        "https://raw.githubusercontent.com/dsrscientist/dataset1/master/AirplaneCrashes.csv"
    )
    print("✅ Dataset loaded from URL")
except Exception:
    print("⚠️ URL unavailable — generating synthetic data...")
    np.random.seed(42)
    n = 5000
    years  = np.random.randint(1908, 2024, n)
    aboard = np.random.randint(2, 200, n)
    safety = np.clip(1.0 - 0.003 * (years - 1908), 0.2, 1.0)
    fatalities = np.clip(
        (aboard * np.random.uniform(0.2, 1.0, n) * safety).astype(int), 1, aboard
    )
    df = pd.DataFrame({
        "Date"       : pd.to_datetime([f"{y}-{np.random.randint(1,13):02d}-01" for y in years]),
        "Aboard"     : aboard,
        "Fatalities" : fatalities,
        "Location"   : np.random.choice(["USA", "Russia", "Brazil", "France", "China"], n),
    })
    print("✅ Synthetic dataset generated")

# --- Cleaning ---
# Convert Date
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Year"] = df["Date"].dt.year

# Keep useful columns
cols_needed = ["Year", "Aboard", "Fatalities"]
for col in cols_needed:
    if col not in df.columns:
        df[col] = np.nan

df_clean = df[cols_needed].dropna().astype(int)
df_clean["Survivors"] = df_clean["Aboard"] - df_clean["Fatalities"]
df_clean["Survival_Rate"] = (df_clean["Survivors"] / df_clean["Aboard"]) * 100
df_clean = df_clean[df_clean["Aboard"] > 0]  # remove invalid rows

print(f"\nShape after cleaning : {df_clean.shape}")
print(f"Years covered        : {df_clean.Year.min()} → {df_clean.Year.max()}")
print(f"Missing values       :\n{df_clean.isnull().sum()}")
print(f"\nFirst 5 rows:")
print(df_clean.head())


# ============================================================
# PART 2 — EXPLORATORY DATA ANALYSIS
# ============================================================
print("\n" + "=" * 55)
print("PART 2 — Exploratory Data Analysis")
print("=" * 55)

total_crashes    = len(df_clean)
total_fatalities = df_clean["Fatalities"].sum()
total_aboard     = df_clean["Aboard"].sum()
total_survivors  = df_clean["Survivors"].sum()
avg_survival     = df_clean["Survival_Rate"].mean()

print(f"Total crashes        : {total_crashes:,}")
print(f"Total fatalities     : {total_fatalities:,}")
print(f"Total aboard         : {total_aboard:,}")
print(f"Total survivors      : {total_survivors:,}")
print(f"Avg survival rate    : {avg_survival:.1f}%")

# Crashes per decade
df_clean["Decade"] = (df_clean["Year"] // 10) * 10
crashes_by_decade = df_clean.groupby("Decade").size()
print(f"\nCrashes by decade:")
print(crashes_by_decade)

# Crashes per year
crashes_by_year = df_clean.groupby("Year").size()

# Visualization — crashes over time
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle("PART 2 — Exploratory Data Analysis", fontsize=14, fontweight="bold")

# Crashes per year
axes[0].plot(crashes_by_year.index, crashes_by_year.values,
             color="steelblue", lw=2)
axes[0].fill_between(crashes_by_year.index, crashes_by_year.values,
                     alpha=0.3, color="steelblue")
axes[0].set_title("Number of Crashes per Year")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Number of Crashes")

# Crashes by decade (bar chart)
axes[1].bar(crashes_by_decade.index, crashes_by_decade.values,
            width=8, color="coral", alpha=0.85, edgecolor="white")
axes[1].set_title("Crashes by Decade")
axes[1].set_xlabel("Decade")
axes[1].set_ylabel("Number of Crashes")

plt.tight_layout()
plt.show()


# ============================================================
# PART 3 — STATISTICAL ANALYSIS
# ============================================================
print("\n" + "=" * 55)
print("PART 3 — Statistical Analysis")
print("=" * 55)

fatalities = df_clean["Fatalities"].values

desc = stats.describe(fatalities)
print(f"Count    : {desc.nobs}")
print(f"Mean     : {desc.mean:.2f}")
print(f"Median   : {np.median(fatalities):.2f}")
print(f"Std Dev  : {np.sqrt(desc.variance):.2f}")
print(f"Skewness : {desc.skewness:.4f}")
print(f"Kurtosis : {desc.kurtosis:.4f}")

if abs(desc.skewness) < 0.5:
    shape = "symmetric"
elif desc.skewness > 0:
    shape = "right-skewed (most crashes have low fatalities, few are very deadly)"
else:
    shape = "left-skewed"
print(f"Shape    : {shape}")

# --- Hypothesis Test: pre-1970 vs post-1970 ---
print("\n--- T-Test: Pre-1970 vs Post-1970 fatalities ---")
pre_1970  = df_clean[df_clean["Year"] < 1970]["Fatalities"].values
post_1970 = df_clean[df_clean["Year"] >= 1970]["Fatalities"].values

print(f"Pre-1970  : n={len(pre_1970)},  mean={np.mean(pre_1970):.2f}")
print(f"Post-1970 : n={len(post_1970)}, mean={np.mean(post_1970):.2f}")

print("\nH0: mean fatalities pre-1970 == mean fatalities post-1970")
print("H1: mean fatalities differ between eras")

t_stat, p_value = stats.ttest_ind(pre_1970, post_1970)
print(f"T-statistic : {t_stat:.4f}")
print(f"P-value     : {p_value:.4f}")

if p_value < 0.05:
    print("✅ Significant difference in fatalities between eras (reject H0)")
else:
    print("❌ No significant difference found (fail to reject H0)")

# Visualization — Statistical Analysis
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("PART 3 — Statistical Analysis", fontsize=14, fontweight="bold")

# Histogram of fatalities
axes[0].hist(fatalities, bins=40, color="steelblue", alpha=0.75, edgecolor="white")
axes[0].axvline(np.mean(fatalities), color="red", lw=2,
                linestyle="--", label=f"Mean={np.mean(fatalities):.1f}")
axes[0].axvline(np.median(fatalities), color="orange", lw=2,
                linestyle="-", label=f"Median={np.median(fatalities):.1f}")
axes[0].set_title("Distribution of Fatalities")
axes[0].set_xlabel("Fatalities")
axes[0].legend()

# Box plot pre vs post 1970
axes[1].boxplot([pre_1970, post_1970],
                labels=["Pre-1970", "Post-1970"],
                patch_artist=True,
                boxprops=dict(facecolor="lightblue", alpha=0.7))
axes[1].set_title("Fatalities: Pre vs Post 1970")
axes[1].set_ylabel("Fatalities")

# Survival rate histogram
axes[2].hist(df_clean["Survival_Rate"], bins=30,
             color="green", alpha=0.7, edgecolor="white")
axes[2].axvline(df_clean["Survival_Rate"].mean(), color="red",
                lw=2, linestyle="--",
                label=f"Mean={df_clean['Survival_Rate'].mean():.1f}%")
axes[2].set_title("Distribution of Survival Rate")
axes[2].set_xlabel("Survival Rate (%)")
axes[2].legend()

plt.tight_layout()
plt.show()


# ============================================================
# PART 4 — ADVANCED STATISTICS (Bonus)
# ============================================================
print("\n" + "=" * 55)
print("PART 4 — Advanced Statistics (Bonus)")
print("=" * 55)

# --- ANOVA by decade ---
print("\n--- ANOVA: Fatalities by Decade ---")
decades = sorted(df_clean["Decade"].unique())
groups  = [df_clean[df_clean["Decade"] == d]["Fatalities"].values for d in decades]

for d, g in zip(decades, groups):
    print(f"  {d}s : n={len(g):4d}, mean={np.mean(g):.2f}")

f_stat, p_anova = stats.f_oneway(*groups)
print(f"\nF-statistic : {f_stat:.4f}")
print(f"P-value     : {p_anova:.4f}")
if p_anova < 0.05:
    print("✅ Fatalities differ significantly across decades (reject H0)")
else:
    print("❌ No significant difference across decades")

# --- Regression: Aboard vs Fatalities ---
print("\n--- Linear Regression: Aboard → Fatalities ---")
reg = stats.linregress(df_clean["Aboard"].values,
                       df_clean["Fatalities"].values)
print(f"Slope     : {reg.slope:.4f}  → each extra person = +{reg.slope:.2f} fatalities")
print(f"Intercept : {reg.intercept:.4f}")
print(f"R²        : {reg.rvalue**2:.4f}")
print(f"P-value   : {reg.pvalue:.6f}")

# --- Pearson vs Spearman ---
print("\n--- Correlation: Aboard vs Fatalities ---")
r_p, p_p = stats.pearsonr(df_clean["Aboard"], df_clean["Fatalities"])
r_s, p_s = stats.spearmanr(df_clean["Aboard"], df_clean["Fatalities"])
print(f"Pearson  r = {r_p:.4f},  p = {p_p:.6f}")
print(f"Spearman ρ = {r_s:.4f},  p = {p_s:.6f}")
print("📌 Spearman may differ from Pearson if the relationship is")
print("   non-linear or if there are outliers (extreme crashes).")

# Visualization — Regression
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle("PART 4 — Regression & Correlation", fontsize=14, fontweight="bold")

# Scatter + regression line
x_vals = df_clean["Aboard"].values
y_vals = df_clean["Fatalities"].values
x_line = np.linspace(x_vals.min(), x_vals.max(), 300)
y_line = reg.slope * x_line + reg.intercept

axes[0].scatter(x_vals, y_vals, alpha=0.3, color="steelblue", s=15)
axes[0].plot(x_line, y_line, color="red", lw=2.5,
             label=f"R²={reg.rvalue**2:.3f}")
axes[0].set_title("Aboard vs Fatalities — Regression")
axes[0].set_xlabel("People Aboard")
axes[0].set_ylabel("Fatalities")
axes[0].legend()

# Mean fatalities by decade
mean_by_decade = df_clean.groupby("Decade")["Fatalities"].mean()
axes[1].bar(mean_by_decade.index, mean_by_decade.values,
            width=8, color="coral", alpha=0.85, edgecolor="white")
axes[1].set_title("Mean Fatalities by Decade")
axes[1].set_xlabel("Decade")
axes[1].set_ylabel("Mean Fatalities")

plt.tight_layout()
plt.show()


# ============================================================
# PART 5 — SUMMARY & INSIGHTS
# ============================================================
print("\n" + "=" * 55)
print("PART 5 — Summary & Insights")
print("=" * 55)
print(f"""
📊 DATASET
   • {total_crashes:,} crash records analyzed
   • Years covered: {df_clean.Year.min()} to {df_clean.Year.max()}

💀 FATALITIES
   • Total fatalities : {total_fatalities:,}
   • Mean per crash   : {np.mean(fatalities):.1f}
   • Median per crash : {np.median(fatalities):.1f}
   • Distribution     : {shape}

🛡️ SURVIVAL
   • Average survival rate : {avg_survival:.1f}%

📈 HYPOTHESIS TEST (Pre vs Post 1970)
   • T={t_stat:.3f}, p={p_value:.4f}
   • {'Significant ✅ — flying became statistically safer' if p_value < 0.05 else 'Not significant ❌'}

📉 REGRESSION (Aboard → Fatalities)
   • R² = {reg.rvalue**2:.3f} — {'strong' if reg.rvalue**2 > 0.5 else 'moderate' if reg.rvalue**2 > 0.3 else 'weak'} relationship
   • Each extra person aboard adds ~{reg.slope:.2f} expected fatalities

🔬 ANOVA (by decade)
   • F={f_stat:.3f}, p={p_anova:.4f}
   • {'Fatalities differ significantly across decades ✅' if p_anova < 0.05 else 'No significant difference across decades ❌'}
""")

print("=" * 55)
print("✅ DAILY CHALLENGE COMPLETE !")
print("=" * 55)