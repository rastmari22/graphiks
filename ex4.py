
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="dark")
sns.color_palette("rocket", as_cmap=True)

sns.light_palette("seagreen", as_cmap=True)

# Simulate data from a bivariate Gaussian
n = 10000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
rng = np.random.RandomState(0)
x, y = rng.multivariate_normal(mean, cov, n).T

# Draw a combo histogram and scatterplot with density contours
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=x, y=y, s=5, color=".15")
sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)

plt.show()
import seaborn as sns
import matplotlib.pyplot as plt


diamonds = sns.load_dataset("diamonds")


plt.figure(figsize=(10, 6))
sns.scatterplot(x="carat", y="price", data=diamonds, hue="cut", palette="viridis")


plt.xlabel("Carat")
plt.ylabel("Price")
plt.title("Diamond Price by Carat and Cut")


plt.show()


# связи между весом бриллианта (carat) и его ценой (price), при этом каждая точка отображается в зависимости от типа огранки (cut) с помощью цветовой гаммы "viridis".