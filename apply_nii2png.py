import os
folder_dir = ""
img = 0
image_num = 0
for images in os.listdir('.'):
    img = int(img) + 1
#     print(images)
    os.system('python3 nii2png.py -i '+ images + ' -o ' + str(img))
