import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.dpi'] = 120

df = pd.read_csv('../day5/Sample - Superstore.csv', encoding='latin-1')
df = df.drop_duplicates()
for col in ['Order Date', 'Ship Date']:
    df[col] = pd.to_datetime(df[col])
df['Profit Margin']    = (df['Profit'] / df['Sales']) * 100
df['Order Year']       = df['Order Date'].dt.year
df['Order Month']      = df['Order Date'].dt.month
df['Order Month-Year'] = df['Order Date'].dt.to_period('M')
print("Dataset prêt :", df.shape)

monthly_total = df.groupby('Order Month-Year')['Sales'].sum()
plt.figure(figsize=(12, 6))
plt.plot(monthly_total.index.to_timestamp(), monthly_total.values, marker='o', color='#7F77DD', linewidth=2)
plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
plt.xlabel('Date'); plt.ylabel('Sales ($)'); plt.xticks(rotation=45); plt.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('timeseries.png'); plt.show()

state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=True)
top_states = state_sales.tail(10)
plt.figure(figsize=(12, 6))
plt.barh(range(len(top_states)), top_states.values, color='#7F77DD')
plt.yticks(range(len(top_states)), top_states.index)
plt.title('Top 10 States by Sales', fontsize=16, fontweight='bold')
plt.grid(axis='x', alpha=0.3); plt.tight_layout(); plt.savefig('geo_states.png'); plt.show()

product_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x=product_profit.values, y=product_profit.index, palette='viridis', orient='h')
plt.title('Top 10 Most Profitable Products', fontsize=16, fontweight='bold')
plt.tight_layout(); plt.savefig('top10_products.png'); plt.show()

plt.figure(figsize=(14, 8))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', alpha=0.6, s=50)
sns.regplot(data=df, x='Discount', y='Profit', scatter=False, color='red', line_kws={'linewidth': 2, 'linestyle': '--'})
plt.title('Discount vs Profit by Category', fontsize=16, fontweight='bold')
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout(); plt.savefig('discount_profit.png'); plt.show()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
ax1.plot(monthly_total.index.to_timestamp(), monthly_total.values, marker='o', color='#7F77DD')
ax1.set_title('Monthly Sales Trend'); ax1.tick_params(axis='x', rotation=45)
category_sales = df.groupby('Category')['Sales'].sum()
ax2.bar(category_sales.index, category_sales.values, color='#1D9E75'); ax2.set_title('Sales by Category')
ax3.barh(range(len(top_states)), top_states.values, color='#7F77DD')
ax3.set_yticks(range(len(top_states))); ax3.set_yticklabels(top_states.index); ax3.set_title('Top 10 States')
for cat in df['Category'].unique():
    d = df[df['Category']==cat]
    ax4.scatter(d['Discount'], d['Profit'], label=cat, alpha=0.6)
ax4.axhline(y=0, color='black', linestyle='--', alpha=0.5); ax4.legend(); ax4.set_title('Discount vs Profit')
plt.suptitle('Superstore Dashboard', fontsize=18, fontweight='bold')
plt.tight_layout(); plt.savefig('dashboard.png'); plt.show()

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
high_disc = df[df['Discount'] > 0.2]
print(f"\n=== EXECUTIVE SUMMARY ===")
print(f"Total Revenue  : ${total_sales:,.0f}")
print(f"Total Profit   : ${total_profit:,.0f}")
print(f"Profit Margin  : {(total_profit/total_sales)*100:.1f}%")
print(f"Top State      : {state_sales.index[-1]}")
print(f"Top Product    : {product_profit.index[0]}")
print(f"Loss rate >20% discount : {(high_disc['Profit']<0).mean()*100:.1f}%")
print("Recommandation : limiter les remises a 20% max.")