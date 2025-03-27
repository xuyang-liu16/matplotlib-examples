import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager

# 添加自定义字体到 Matplotlib
font_path = "Cambria Bold.ttf"
fontManager.addfont(font_path)

# 设置全局默认字体和样式
sns.set_style("whitegrid", {'grid.linewidth': 2})
plt.rcParams.update({
    "font.family": "Cambria",
    "font.weight": "bold",
    "font.size": 15
})

# 示例数据
data = {
    'Model': ["GQA", "VizWiz", "ScienceQA", "AI2D", "MMStar", "MME", "SEEDBench", "Average"] * 8,
    'Ratio': np.tile(np.asarray([100, 75, 50, 25, 15, 10, 5, 0])[:, np.newaxis], (1, 8)).flatten(),
    'Performance': [
        100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00, 100.00,
        99.10, 96.70, 100.00, 97.20, 102.50, 99.10, 99.20, 99.10,
        96.50, 96.30, 99.50, 95.90, 102.20, 100.00, 98.10, 98.40,
        91.10, 91.50, 98.70, 94.70, 98.90, 98.80, 94.70, 95.40,
        85.00, 89.13, 99.41, 92.96, 97.79, 89.28, 89.00, 91.10,
        81.70, 88.50, 98.80, 92.20, 96.70, 89.30, 86.10, 90.50,
        74.79, 82.17, 97.05, 89.71, 90.88, 75.88, 76.03, 83.93,
        50.80, 81.30, 90.40, 86.50, 76.00, 53.00, 57.30, 70.80,
    ],
}

df = pd.DataFrame(data)

# 设置颜色
colors = {
    "GQA": "#1f77b4",       # 蓝色
    "VizWiz": "#ff7f0e",    # 橙色
    "ScienceQA": "#2ca02c", # 绿色
    "AI2D": "#7f7f7f",      # 灰色
    "MMStar": "#9467bd",    # 紫色
    "MME": "#8c564b",       # 棕色
    "SEEDBench": "#e377c2", # 粉色
    "Average": "#8B0000"    # 深红色
}

# 设置画布大小
plt.figure(figsize=(6, 4))

# 使用 seaborn 绘制线图，去掉点的白色边线
ax = sns.lineplot(data=df, x='Ratio', y='Performance', hue='Model', palette=colors, linestyle="-", marker='o', linewidth=3, markeredgewidth=0)

# 添加标题和标签
plt.xlabel('Retention Ratio (%)', fontsize=15)
plt.ylabel('Relative Performance (%)', fontsize=15)
plt.xticks(np.arange(0, 110, 10), fontsize=15)
plt.yticks(np.arange(50, 105, 5), fontsize=15)

# 显示图例
legend = ax.legend(ncol=2)

# 设置边框颜色
for spine in ax.spines.values():
    spine.set_edgecolor('black')

# 设置网格线为实线
plt.grid(True, color='#e0e0e0', linestyle='-', linewidth=1)

# 保存图表
plt.savefig("llava_ov_performance.pdf", format='pdf', bbox_inches='tight')

# 显示图表
plt.show()
