from PIL import Image
import os


images = os.listdir('images')
for i in range(50):
    im = Image.open(f"images\{images[i]}")
    print(i)
    im = im.resize((256,256))
    im.save(f'dataset\{images[i]}')
print(images)

