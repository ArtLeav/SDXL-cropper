from PIL import Image
import os

src_dir = r'/path/to/source/directory'
dst_dir = r'/path/to/destination/directory'

quality_val = 100

resolutions = [(1024, 1024), (896, 1152), (832, 1216), (768, 1344), (640, 1536), (1152, 896), (1216, 832), (1344, 768), (1536, 640)]

def resize_and_crop(img, size):
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    
    if ratio > img_ratio:
        img = img.resize((size[0], int(size[0] * img.size[1] / img.size[0])), Image.LANCZOS)
        box = (0, (img.size[1] - size[1]) / 2, img.size[0], (img.size[1] + size[1]) / 2)
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((int(size[1] * img.size[0] / img.size[1]), size[1]), Image.LANCZOS)
        box = ((img.size[0] - size[0]) / 2, 0, (img.size[0] + size[0]) / 2, img.size[1])
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]), Image.LANCZOS)
    return img

def closest(lst, K): 
     return lst[min(range(len(lst)), key = lambda i: abs(lst[i][0]/lst[i][1]-K))]

for filename in os.listdir(src_dir):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  # add file types as needed
        img = Image.open(os.path.join(src_dir, filename))
        closest_res = closest(resolutions, img.size[0]/img.size[1])
        new_img = resize_and_crop(img, closest_res)
        if new_img.mode == 'RGBA':
            new_img = new_img.convert('RGB')
        new_filename = f'{os.path.splitext(filename)[0]}.jpg'
        new_img.save(os.path.join(dst_dir, new_filename), quality=quality_val)