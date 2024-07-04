import glob

from PIL import Image

# 画像のパスを取得
image_paths = sorted(
    glob.glob("/home/a6000/github/pilot-GAN/C-DCGAN_weak/result/fake_samples_epoch_*.png")
)

# 画像を読み込む
images = [Image.open(image) for image in image_paths]

# GIFを作成して保存
images[0].save("output.gif", save_all=True, append_images=images[1:], duration=100, loop=0)

print("GIFが正常に作成されました！")
