import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import fontManager

# # 添加自定义字体到 Matplotlib
# font_path = "Cambria Bold.ttf"
# fontManager.addfont(font_path)

# 原始数据
methods = ["LLaVA-NeXT", "FiCoCo-V", "FiCoCo-L", " ", "LLaVA", "FiCoCo-V", "FiCoCo-L"]
tflops = [42.7, 2.9, 2.9, None, 8.5, 1.5, 1.5]
throughput = [3.8, 7.9, 6.5, None, 8.99, 12.9, 11.6]

# 归一化基准
base_tflops_left = tflops[0]  # LLaVA-NeXT 的 TFlops 归一化为 100%
base_throughput_left = throughput[0]  # LLaVA-NeXT 的 Throughput 归一化为 1.0 倍

base_tflops_right = tflops[4]  # LLaVA 的 TFlops 归一化为 100%
base_throughput_right = throughput[4]  # LLaVA 的 Throughput 归一化为 1.0 倍

# 计算归一化数据
tflops_normalized = [
    100 * (x / base_tflops_left) if i < 3 else (100 * (x / base_tflops_right) if x is not None else None)
    for i, x in enumerate(tflops)
]

throughput_normalized = [
    (x / base_throughput_left) if i < 3 else ((x / base_throughput_right) if x is not None else None)
    for i, x in enumerate(throughput)
]

x = np.arange(len(methods))

# 颜色
color_tflops = '#1f77b4'  # 蓝色
color_throughput = '#c00000'  # 深红色

# 统一五角星大小
star_size = 120.0

fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
ax2 = ax.twinx()  # 第二个 Y 轴

# TFlops 柱状图（归一化）
bars = ax.bar(x, [val if val is not None else 0 for val in tflops_normalized],
              color=color_tflops, alpha=0.7, label='TFLOPs (Normalized)', width=0.5)

ax.set_ylabel("TFLOPS (Normalized, %)", color=color_tflops, fontsize=14, fontweight='bold')
ax.tick_params(axis='y', labelcolor=color_tflops, labelsize=12)

# Throughput 折线图（归一化，并分两段）
valid_x_1 = [i for i in range(3) if throughput_normalized[i] is not None]  # 第一部分 (LLaVA-NeXT 归一化)
valid_y_1 = [throughput_normalized[i] for i in range(3) if throughput_normalized[i] is not None]

valid_x_2 = [i for i in range(4, len(throughput_normalized)) if throughput_normalized[i] is not None]  # 第二部分 (LLaVA 归一化)
valid_y_2 = [throughput_normalized[i] for i in range(4, len(throughput_normalized)) if throughput_normalized[i] is not None]

ax2.plot(valid_x_1, valid_y_1, marker='*', linestyle='--', color=color_throughput,
         label='Throughput (Normalized, x)', markersize=8, linewidth=2)
ax2.plot(valid_x_2, valid_y_2, marker='*', linestyle='--', color=color_throughput,
         markersize=8, linewidth=2)

# 添加星形散点
for i in valid_x_1 + valid_x_2:
    ax2.scatter(i, throughput_normalized[i], marker='*', color=color_throughput, s=star_size, alpha=0.75)

ax2.set_ylabel("Throughput (x)", color=color_throughput, fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=color_throughput, labelsize=12)

# **数值标签（显示归一化百分比+原始值）**
for bar, norm_val, raw_val in zip(bars, tflops_normalized, tflops):
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width() / 2, height, f"{norm_val:.1f}% ({raw_val:.1f})",
                ha='center', va='bottom', fontsize=10, color=color_tflops)

for i, norm_val in enumerate(throughput_normalized):
    if norm_val is not None:
        ax2.text(i, norm_val + 0.02, f"{norm_val:.2f}x ({throughput[i]:.1f})",
                 color=color_throughput, ha='center', va='bottom', fontsize=10)

# X轴
ax.set_xticks(x)
ax.set_xticklabels(methods, fontsize=10, fontweight='bold')

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
ax2.grid(False)

# 移除边框
for spine in ax.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

# 设置左/右坐标轴颜色
ax.spines["left"].set_visible(True)
ax.spines["left"].set_color(color_tflops)
ax.spines["left"].set_linewidth(3)

ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(color_throughput)
ax2.spines["right"].set_linewidth(3)

plt.tight_layout()

# 保存为 SVG 文件
plt.savefig("output.pdf", format="svg")
plt.show()