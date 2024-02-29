import seaborn as sns
import matplotlib.pyplot as plt


penguins = sns.load_dataset("penguins")

sns.set(style="whitegrid")
palette = sns.color_palette("Set2")

fig, axes = plt.subplots(2, 2, figsize=(12, 6))

sns.stripplot(x="species", y="body_mass_g", data=penguins, palette=palette,ax=axes[0,0])
axes[0, 0].set_title("Распределение массы пингвинов по видам")


sns.boxplot(x="species", y="bill_length_mm", data=penguins, ax=axes[0, 1], palette=palette)
axes[0, 1].set_title("Сравнение размеров клюва различных видов пингвинов")


sns.histplot(data=penguins, x="body_mass_g", hue="species", multiple="stack", kde=True, palette=palette, ax=axes[1, 0])
axes[1, 0].set_title("Распределение массы пингвинов разных видов")


sns.violinplot(x="species", y="bill_depth_mm", data=penguins, ax=axes[1, 1], palette=palette)
axes[1, 1].set_title("Распределение глубины клюва в разбивке по видам пингвинов")

plt.tight_layout()
plt.show()
