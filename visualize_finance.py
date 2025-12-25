import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Set font for Korean support if available, otherwise fallback might be needed but assuming standard env
# Trying commonly available Korean fonts in Windows
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# Data
years = ["2020", "2021", "2022", "2023", "2024", "2025 (Budget)"]
income = [226944, 240240, 255638, 262625, 267224, 266049]
expenditure = [230744, 243957, 265577, 276671, 275796, 266049]

x = np.arange(len(years))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, income, width, label='Income (수입)', color='skyblue')
rects2 = ax.bar(x + width/2, expenditure, width, label='Expenditure (지출)', color='salmon')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Amount (Million KRW)')
ax.set_title('Yearly Income and Expenditure Status')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

output_path = 'c:/Users/Ben/projects/antigravity_exercise/finance_graph.png'
plt.savefig(output_path)
print(f"Graph saved to {output_path}")
