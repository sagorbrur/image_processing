# converting bmp image to png format using PIL(Pillow)

# for list of images

import glob
from PIL import Image


img_path = glob.glob('GT/*.bmp')

print(len(img_path))

cnt = 0

for img in img_path:
    im = Image.open(img)
    w,h = im.size
    new_im = im.resize((w,h))
    new_im.save('GT_PNG/{}_gt.png'.format(cnt), 'png') # for JPEG just replace png to jpg
    cnt+=1

print('done')


# for single image

"""
from PIL import Image

img = Image.open('myimg.bmp')
w,h = img.size
new_img = img.resize((w,h))
new_img.save('converted_img.png', 'png')
print('done')


"""
