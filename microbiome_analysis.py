import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Set random seed for reproducibility
np.random.seed(42)

# Microbial taxa
taxa = ["Proteobacteria", "Bacteroidetes", "Firmicutes", "Actinobacteria", "Cyanobacteria"]

# Simulated microbiome data
clean_samples = pd.DataFrame(
    np.random.normal(loc=[20, 25, 30, 15, 10], scale=5, size=(20, 5)),
    columns=taxa
)

contaminated_samples = pd.DataFrame(
    np.random.normal(loc=[40, 15, 20, 10, 15], scale=5, size=(20, 5)),
    columns=taxa
)

# Shannon Diversity Function
def shannon_index(df):
    proportions = df.div(df.sum(axis=1), axis=0)
    return -(proportions * np.log(proportions + 1e-9)).sum(axis=1)

clean_div = shannon_index(clean_samples)
cont_div = shannon_index(contaminated_samples)

# Statistical test
t_stat, p_value = ttest_ind(clean_div, cont_div)

print("Shannon Diversity Comparison")
print("T-statistic:", t_stat)
print("P-value:", p_value)

# Boxplot (matplotlib)
plt.figure()
plt.boxplot([clean_div, cont_div])
plt.xticks([1, 2], ["Clean Water", "Contaminated Water"])
plt.ylabel("Shannon Diversity Index")
plt.title("Microbial Diversity Comparison")
plt.show()

# Mean abundance comparison
mean_clean = clean_samples.mean()
mean_cont = contaminated_samples.mean()

abundance_df = pd.DataFrame({
    "Clean Water": mean_clean,
    "Contaminated Water": mean_cont
})

abundance_df.plot(kind="bar")
plt.title("Mean Relative Abundance of Major Taxa")
plt.ylabel("Relative Abundance")
plt.show()
