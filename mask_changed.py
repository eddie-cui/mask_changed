import os
import cv2

# 设置数据目录
dir_data = r'public_data/data_BlendedMVS/cup2'
dir_mask = os.path.join(dir_data, 'mask')  # mask目录
dir_img = os.path.join(dir_data, 'image')  # image目录

# 获取所有mask和image文件名
mask_list = os.listdir(dir_mask)  # 所有mask文件名
img_list = os.listdir(dir_img)    # 所有image文件名

# 确保mask和image文件数量一致
if len(mask_list) != len(img_list):
    raise ValueError("The number of mask files and image files are not the same.")

# 处理每对mask和image文件
for mask_file, img_file in zip(mask_list, img_list):
    # 获取图像的文件名和扩展名
    (img_filename, img_extension) = os.path.splitext(img_file)
    img_file_png = img_filename + '.png'  # 修改图像的格式为png

    # 读取图像文件
    img = cv2.imread(os.path.join(dir_img, img_file))
    os.remove(os.path.join(dir_img, img_file))  # 删除旧格式的图像
    cv2.imwrite(os.path.join(dir_img, img_file_png), img)  # 保存新格式的图像

    # 获取图像的尺寸
    h, w = img.shape[0], img.shape[1]

    # 读取mask文件并转换为二值mask
    mask = cv2.imread(os.path.join(dir_mask, mask_file), 0) > 0  # 读取mask，并将其转为黑白的mask，只有0和255
    mask = mask * 255
    mask = cv2.resize(mask.astype("uint8"), (w, h), interpolation=cv2.INTER_AREA)  # 调整mask的尺寸

    # 将mask文件名改为与对应的image文件名相同
    mask_file_new = img_filename + '.png'
    cv2.imwrite(os.path.join(dir_mask, mask_file_new), mask)
    os.remove(os.path.join(dir_mask, mask_file))  # 删除旧的mask文件
