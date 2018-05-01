from pdb import set_trace as st
import os
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser('creer les images de contours')
parser.add_argument('--fold_src', dest='fold_src', help='input directory for image', type=str, default='../dataset/50kshoes_edges')
parser.add_argument('--fold_dst', dest='fold_dst', help='output directory', type=str, default='../dataset/test_AB')
parser.add_argument('--num_imgs', dest='num_imgs', help='number of images',type=int, default=1000)
args = parser.parse_args()

for arg in vars(args):
    print('[%s] = ' % arg,  getattr(args, arg))

splits = filter( lambda f: not f.startswith('.'), os.listdir(args.fold_src)) # ignore hidden folders like .DS_Store

for sp in splits:
    img_fold_src = os.path.join(args.fold_src, sp)
    img_list = list(filter( lambda f: not f.startswith('.'), os.listdir(img_fold_src))) # ignore hidden folders like .DS_Store

    num_imgs = min(args.num_imgs, len(img_list))
    print('split = %s, use %d/%d images' % (sp, num_imgs, len(img_list)))
    img_fold_dst = os.path.join(args.fold_dst, sp)
    if not os.path.isdir(img_fold_dst):
        os.makedirs(img_fold_dst)
    print('split = %s, number of images = %d' % (sp, num_imgs))
    for n in range(num_imgs):
        name_src = img_list[n]
        path_src = os.path.join(img_fold_src, name_src)

        if os.path.isfile(path_src):
            # Changer le nom du type de l"image pour eviter un bug de cv
            filename_old = os.path.splitext(path_src)[0]
            filetype_old = os.path.splitext(path_src)[1]
            Newdir = os.path.join(img_fold_src, filename_old + '.jpg')
            os.rename(path_src, Newdir)
            name_dst = name_src
            print("Processing: %s" % name_src)
            path_dst = os.path.join(img_fold_dst, name_dst)
            img_src = cv2.imread(Newdir, cv2.IMREAD_COLOR)
            img_R1 = cv2.resize(img_src, (128, 128), interpolation=cv2.INTER_LINEAR)
            img_G = cv2.GaussianBlur(img_src, (3, 3), 0)
            img_R2 = cv2.resize(img_G, (128, 128), interpolation=cv2.INTER_LINEAR)
            img_C = cv2.Canny(img_R2, 50, 150)
            cv2.imwrite(path_dst, img_C)
            img = cv2.imread(path_dst)
            w = img.shape[1]
            h = img.shape[0]
            ii = 0
            # divider un multi-channel array a trois single-channel arrays
            b, g, r = cv2.split(img)
            b = 255 - b
            g = 255 - g
            r = 255 - r
            # changer le valeur de channel
            img[:, :, 0] = b
            img[:, :, 1] = g
            img[:, :, 2] = r
            img_dst = np.concatenate([img_R1, img], 1)
            cv2.imwrite(path_dst, img_dst)

# --fold_src
# C:\Users\olivier\Desktop\S8\PAR\Jeudedonnee\Git2Olivier\PAR\google_pictures\bar+chart C:\Users\olivier\Desktop\S8\PAR\Viztransfer\VizTransfert\dataset\google
# --fold_dst
# C:\Users\olivier\Desktop\S8\PAR\Jeudedonnee\bar+chart_contour
