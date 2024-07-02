import matplotlib.pyplot as plt
import numpy as np

# サンプルデータ（ダミーデータとしてランダムな画像を生成）
num_labels = 10  # ラベルの数
num_images_per_label = 5  # 各ラベルごとの画像数
image_size = 32  # 画像のサイズ

# ダミーデータ生成（ランダムな画像を生成する部分を適宜置き換えてください）
images = np.random.rand(num_labels * num_images_per_label, image_size, image_size)

# ラベル名（仮のダミーラベル）
labels = [f"Label_{i}" for i in range(num_labels)]

# 画像の描画
fig, axs = plt.subplots(
    num_images_per_label, num_labels, figsize=(num_labels, num_images_per_label)
)

for i in range(num_labels):
    for j in range(num_images_per_label):
        image = images[i * num_images_per_label + j]
        axs[j, i].imshow(image, cmap="gray")
        axs[j, i].axis("off")
        if j == 0:
            axs[j, i].set_title(labels[i])  # 列の頭にラベルを書く

plt.tight_layout()

# 画像の保存
plt.savefig("grid_images.png")
plt.show()
