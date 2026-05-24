import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

# Load dataset
data = pd.read_csv("data.csv")

# Better overall style
plt.style.use('ggplot')

# ================= BAR CHART =================
gender_counts = data["Gender"].value_counts()

plt.figure(figsize=(8,5))

bars = plt.bar(
    gender_counts.index,
    gender_counts.values
)

# Titles and labels
plt.title("Gender Distribution in Population", fontsize=16, fontweight='bold')
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Count", fontsize=12)

# Add values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 0.05,
        int(yval),
        ha='center',
        fontsize=11
    )

plt.tight_layout()
plt.show()

# ================= HISTOGRAM =================
plt.figure(figsize=(8,5))

plt.hist(
    data["Age"],
    bins=5,
    edgecolor='black'
)

plt.title("Age Distribution", fontsize=16, fontweight='bold')
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

plt.tight_layout()
plt.show()