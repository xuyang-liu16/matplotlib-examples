import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.figsize": (20, 10),   # 整体图像大小
    "font.size": 13,
    "axes.labelsize": 15,
    "axes.titlesize": 17,
    "xtick.labelsize": 13,
    "ytick.labelsize": 13,
})

tau_values = [1, 5, 10, 15, 20]
textvqa_tau = [60.4, 60.4, 60.6, 60.4, 60.5]
pope_tau    = [87.4, 87.5, 87.5, 87.1, 87.1]
mme_tau     = [1467.9, 1540.9, 1473.3, 1469.7, 1463.3]
mmvet_tau   = [39.1, 39.2, 39.6, 39.0, 38.2]

alpha_values = [0, 0.3, 0.5, 0.7, 1.0]
textvqa_alpha = [60.2, 60.4, 60.4, 60.3, 60.1]
pope_alpha    = [87.4, 87.5, 87.6, 87.4, 86.4]
mme_alpha     = [1473.3, 1468.0, 1477.6, 1493.5, 1488.5]
mmvet_alpha   = [39.6, 38.3, 40.7, 38.7, 37.8]

vertical_line_tau = 10
baseline_tau = {'TextVQA': 59, 'POPE': 87.5, 'MME': 1475, 'MM-Vet': 39}
vertical_line_alpha = 0.4
baseline_alpha = {'TextVQA': 59, 'POPE': 88, 'MME': 1475, 'MM-Vet': 39}

offset_fraction = 0.03  # 控制点上数值标签的竖直偏移比例

def plot_values_with_offset(ax, x_vals, y_vals, marker, color,
                            label,             # 图例标签
                            offset_x=0.5,
                            shift_last_point=False):
    """
    在 ax 上绘制折线，并对各点加上数值标签；
    label 用于在 ax.legend(...) 中显示图例文字。
    """
    ax.plot(x_vals, y_vals, marker=marker, color=color, label=label)

    # 计算竖直方向偏移量
    y_min, y_max = ax.get_ylim()
    y_range = y_max - y_min
    offset_y = offset_fraction * y_range

    for i, (x, y) in enumerate(zip(x_vals, y_vals)):
        if shift_last_point and i == len(x_vals) - 1:
            ax.text(x - offset_x, y + offset_y, f"{y:.1f}",
                    ha='right', va='bottom')
        else:
            if y + offset_y > y_max:
                ax.text(x, y - offset_y, f"{y:.1f}",
                        ha='center', va='top')
            elif y - offset_y < y_min:
                ax.text(x, y + offset_y, f"{y:.1f}",
                        ha='center', va='bottom')
            else:
                ax.text(x, y + offset_y, f"{y:.1f}",
                        ha='center', va='bottom')

    # 每条线绘制完成后，添加图例（右上角）
    ax.legend(loc='upper right')


fig, axes = plt.subplots(2, 4)
colors = ['#FFD700', '#66CDAA', '#87CEFA', '#DA70D6']

# --------------------
# 上排：tau
# --------------------
# 1) TextVQA (tau)
ax = axes[0, 0]
# 去掉子图标题：# ax.set_title("TextVQA")
ax.set_xlabel(r'$\tau$ on TextVQA')
ax.set_ylabel("Performance")
ax.set_ylim(56, 63)
ax.set_yticks(range(56, 64))
ax.axvline(vertical_line_tau, color='gray', linestyle='--', linewidth=1)
ax.axhline(baseline_tau['TextVQA'], color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--')
plot_values_with_offset(ax, tau_values, textvqa_tau, 'o', colors[0],
                        label="TextVQA")

# 2) POPE (tau)
ax = axes[0, 1]
# 去掉子图标题：# ax.set_title("POPE")
ax.set_xlabel(r'$\tau$ on POPE')
ax.set_ylim(86, 89)
ax.set_yticks([86, 86.5, 87, 87.5, 88, 88.5, 89])
ax.axvline(vertical_line_tau, color='gray', linestyle='--', linewidth=1)
ax.axhline(baseline_tau['POPE'], color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--')
plot_values_with_offset(ax, tau_values, pope_tau, 's', colors[1],
                        label="POPE")

# 3) MME (tau)
ax = axes[0, 2]
# 去掉子图标题：# ax.set_title("MME")
ax.set_xlabel(r'$\tau$ on MME')
ax.set_ylim(1400, 1620)  # 扩大一些上限
ax.set_yticks(range(1400, 1621, 50))
ax.axvline(vertical_line_tau, color='gray', linestyle='--', linewidth=1)
ax.axhline(baseline_tau['MME'], color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--')
plot_values_with_offset(ax, tau_values, mme_tau, '^', colors[2],
                        label="MME", offset_x=0.03, shift_last_point=True)

# 4) MM-Vet (tau)
ax = axes[0, 3]
# 去掉子图标题：# ax.set_title("MM-Vet")
ax.set_xlabel(r'$\tau$ on MM-Vet')
ax.set_ylim(36, 45)
ax.set_yticks(range(36, 46))
ax.axvline(vertical_line_tau, color='gray', linestyle='--', linewidth=1)
ax.axhline(baseline_tau['MM-Vet'], color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--')
plot_values_with_offset(ax, tau_values, mmvet_tau, 'd', colors[3],
                        label="MM-Vet")

# --------------------
# 下排：alpha
# --------------------
# 1) TextVQA (alpha)
ax = axes[1, 0]
# 去掉子图标题：# ax.set_title("TextVQA")
ax.set_xlabel(r'$\alpha$ on TextVQA')
ax.set_ylabel("Performance")
ax.set_ylim(56, 64)
ax.set_yticks(range(56, 65))
ax.axvline(vertical_line_alpha, color='gray', linestyle='--', linewidth=1)
ax.axhline(baseline_alpha['TextVQA'], color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--')
plot_values_with_offset(ax, alpha_values, textvqa_alpha, 'o', colors[0],
                        label="TextVQA")

# 2) POPE (alpha)
ax = axes[1, 1]
# 去掉子图标题：# ax.set_title("POPE")
ax.set_xlabel(r'$\alpha$ on POPE')
ax.set_ylim(86, 89)
ax.set_yticks([86, 86.5, 87, 87.5, 88, 88.5, 89])
ax.axvline(vertical_line_alpha, color='gray', linestyle='--', linewidth=1)
ax.axhline(baseline_alpha['POPE'], color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--')
plot_values_with_offset(ax, alpha_values, pope_alpha, 's', colors[1],
                        label="POPE")

# 3) MME (alpha)
ax = axes[1, 2]
# 去掉子图标题：# ax.set_title("MME")
ax.set_xlabel(r'$\alpha$ on MME')
ax.set_ylim(1400, 1620)
ax.set_yticks(range(1400, 1621, 50))
ax.axvline(vertical_line_alpha, color='gray', linestyle='--', linewidth=1)
ax.axhline(baseline_alpha['MME'], color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--')
plot_values_with_offset(ax, alpha_values, mme_alpha, '^', colors[2],
                        label="MME", offset_x=0.01, shift_last_point=True)

# 4) MM-Vet (alpha)
ax = axes[1, 3]
# 去掉子图标题：# ax.set_title("MM-Vet")
ax.set_xlabel(r'$\alpha$ on MM-Vet')
ax.set_ylim(36, 45)
ax.set_yticks(range(36, 46))
ax.axvline(vertical_line_alpha, color='gray', linestyle='--', linewidth=1)
ax.axhline(baseline_alpha['MM-Vet'], color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--')
plot_values_with_offset(ax, alpha_values, mmvet_alpha, 'd', colors[3],
                        label="MM-Vet")

plt.tight_layout()
plt.savefig("my_figure_no_titles.pdf", format='pdf', bbox_inches='tight')
plt.show()

