import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=== Exercise 1 : Matrix Operations ===")
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 10]])
det = np.linalg.det(matrix)
print(f"Determinant : {det:.2f}")
inverse = np.linalg.inv(matrix)
print(f"Inverse :\n{inverse.round(2)}")

print("\n=== Exercise 2 : Statistical Analysis ===")
data = np.random.rand(50) * 100
print(f"Mean: {np.mean(data):.2f}")
print(f"Median: {np.median(data):.2f}")
print(f"Std: {np.std(data):.2f}")

print("\n=== Exercise 3 : Date Manipulation ===")
dates = np.arange('2023-01', '2023-02', dtype='datetime64[D]')
dates_formatted = [str(d).replace('-', '/') for d in dates]
print(dates[:5])
print(dates_formatted[:5])

print("\n=== Exercise 4 : Data Manipulation with NumPy and Pandas ===")
df = pd.DataFrame(np.random.randint(0, 100, size=(5, 3)), columns=['A', 'B', 'C'])
print(df)
print("Valeurs > 50 :")
print(df[df > 50].dropna())
print(f"Somme:\n{df.sum()}")
print(f"Moyenne:\n{df.mean().round(2)}")

print("\n=== Exercise 5 : Image Representation ===")
print("Images = tableaux NumPy : 2D pour grayscale, 3D pour RGB (hauteur x largeur x canaux)")
image = np.array([[0,50,100,150,200],[50,100,150,200,250],[100,150,200,250,255],[150,200,250,255,200],[200,250,255,200,150]], dtype=np.uint8)
print(image)
plt.figure(figsize=(4,4))
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.title('Image 5x5 Grayscale')
plt.colorbar()
plt.tight_layout()
plt.savefig('exercise5_image.png')
plt.show()

print("\n=== Exercise 6 : Basic Hypothesis Testing ===")
np.random.seed(42)
productivity_before = np.random.normal(loc=50, scale=10, size=30)
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)
diff = productivity_after - productivity_before
t_stat = np.mean(diff) / (np.std(diff) / np.sqrt(len(diff)))
print(f"Moyenne avant : {np.mean(productivity_before):.2f}")
print(f"Moyenne après : {np.mean(productivity_after):.2f}")
print(f"Statistique t : {t_stat:.2f}")
print("Conclusion : La formation a significativement amélioré la productivité." if t_stat > 2 else "Pas de différence significative.")

print("\n=== Exercise 7 : Complex Array Comparison ===")
arr_a = np.array([10, 25, 3, 47, 8, 33])
arr_b = np.array([15, 20, 5, 40, 12, 33])
result = arr_a > arr_b
print(f"Array A : {arr_a}")
print(f"Array B : {arr_b}")
print(f"A > B   : {result}")

print("\n=== Exercise 8 : Time Series Data Manipulation ===")
dates_2023 = np.arange('2023-01-01', '2024-01-01', dtype='datetime64[D]')
values = np.random.randn(len(dates_2023)).cumsum()
print(f"Janvier-Mars      : {len(values[0:90])} jours, moyenne = {values[0:90].mean():.2f}")
print(f"Avril-Juin        : {len(values[90:181])} jours, moyenne = {values[90:181].mean():.2f}")
print(f"Juillet-Septembre : {len(values[181:273])} jours, moyenne = {values[181:273].mean():.2f}")
print(f"Octobre-Décembre  : {len(values[273:])} jours, moyenne = {values[273:].mean():.2f}")

print("\n=== Exercise 9 : Data Conversion ===")
numpy_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
df2 = pd.DataFrame(numpy_array, columns=['Col1','Col2','Col3'])
print("NumPy → DataFrame :")
print(df2)
print("DataFrame → NumPy :")
print(df2.to_numpy())

print("\n=== Exercise 10 : Basic Visualization ===")
x = np.arange(50)
y = np.random.randn(50).cumsum()
plt.figure(figsize=(10,5))
plt.plot(x, y, color='#7F77DD', linewidth=2, marker='o', markersize=4)
plt.title('Line Graph of Random Numbers')
plt.xlabel('Index'); plt.ylabel('Cumulative Value')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('exercise10_visualization.png')
plt.show()

print("\nTous les exercices sont terminés !")
