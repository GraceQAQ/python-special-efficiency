#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 千图成像_方法一
#
#                   @File Name    : main.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/08 13:14
#
#                   @Last Update  : 2022/01/08 13:14
#
#-------------------------------------------------------------------
'''
import os, shutil, time
from multiprocessing import Pool
import numpy as np
from PIL import Image, ImageFile, ImageOps

ImageFile.LOAD_TRUNCATED_IMAGES = True


class HsvCompositeImage:
    def __init__(self, image_path, imagedb_dir,
                 meta_width=16, meta_height=9, blend_scale=0.5) -> None:
        '''
        :param image_path: The original image path
        :param imagedb_dir: The original image database directory
        :param meta_width: The image's width from meta database(different from original image database)
        :param meta_height: The image's height from meta database(different from original image database)
        :param blend_scale: When the new image is synthesized, it will
            be mixed with original image to improve the recongnition
        '''
        self.meta_width = meta_width
        self.meta_height = meta_height
        self.blend_scale = blend_scale
        self.imagedb_dir = imagedb_dir
        self.image_path = image_path
        self.metadb_width = 160
        self.metadb_height = 90
        self.type = 'hsv'
        self.metadb_dir = "/".join(imagedb_dir.split('/')
                                   [:-1]) + '_' + self.type + 'db/'
        self.metadb_info_dir = "/".join(imagedb_dir.split('/')
                                        [:-1]) + '_' + self.type + 'db.npy'
        self.pool = Pool()

        self.init_func()

    def init_func(self):
        self.init_image()
        self.create_metadb()
        self.init_metadb()

    def init_image(self):
        self.image = Image.open(self.image_path)
        self.image_width, self.image_height = self.image.size
        self.image_hsv = self.image.convert('HSV')
        self.new_image = Image.new('RGB', self.image.size)
        self.new_image_path = "_new.".join(self.image_path.split('.'))
        self.new_image = Image.new('RGB', self.image.size)

    def create_metadb(self):
        print("Create meta database: ", self.metadb_dir)
        if os.path.exists(self.metadb_dir):
            shutil.rmtree(self.metadb_dir)  # test time for creating metadb
            # return
        os.mkdir(self.metadb_dir)
        print('Create metadb...')
        images_path = []
        for filename in os.listdir(self.imagedb_dir):
            images_path.append(self.imagedb_dir + filename)
        start_time = time.time()

        # map:  blocking ans ordered worker pool [returns: list]            2.9s
        # imap: non-blocking and ordered worker pool [returns: iterator]    21.3s
        # uimap: non-blocking and unordered worker pool [reutrns: iterator] 20.5s
        # amap: asynchronosn worker pool [returns: object]                  3.0s
        # 1: 0.83s;    2: 0.64s;    3: 0.73s;    4: 0.87s
        # 5: 1.01s;    6: 1.18s;    7: 1.32s;    8: 1.44s
        pool = Pool(2)
        pool.map(self.convert_imagedb_to_metadb, images_path)
        pool.close()
        pool.join()
        pool.clear()
        end_time = time.time()
        print('Create metadb time:', end_time - start_time)

    def cal_mean_hsv(self, image):
        # ========== method 1: 1.37s ==========
        # width, height = image.size
        # image_load = image.load()
        # H, S, V = 0, 0, 0
        # for w in range(width):
        #     for h in range(height):
        #         r, g, b = image_load[w, h]
        #         h, s, v = rgb_to_hsv(r / 255, g / 255, b / 255)
        #         H += h; S += s; V += v
        # count = width * height
        # H_mean = round(H / count, 3)
        # S_mean = round(S / count, 3)
        # V_mean = round(V/count, 3)
        # return np.array([H_mean, S_mean, V_mean])

        # ========== method 2: 0.63s ==========
        width, height = image.size
        image_hsv = image.convert('HSV')
        image_array = np.array(image_hsv)
        pixels_number = width * height
        hsv_array = np.round(image_array.sum(
            axis=0).sum(axis=0) / pixels_number, 3)
        return hsv_array

    def convert_imagedb_to_metadb(self, image_path):
        image = Image.open(image_path)
        image = ImageOps.fit(
            image, (self.metadb_width, self.metadb_height), Image.LANCZOS)
        image_mean_hsv_value = self.cal_mean_hsv(image)
        image.save(self.metadb_dir + str(list(image_mean_hsv_value)) + ".jpg")

    def init_metadb(self):
        metadb = []
        for filename in os.listdir(self.metadb_dir):
            if filename == 'None.jpg':
                pass
            else:
                filename = filename.split('.jpg')[0][1:-1].split(', ')
                hsv_array = np.array(list(map(float, filename)))
                metadb.append(hsv_array)
        self.metadb = np.array(metadb)

    def find_closed(self, hsv_value):
        distance = np.linalg.norm(hsv_value - self.metadb, axis=1)
        position = np.argmin(distance)
        closed_image_path = self.metadb_dir + \
                            str(list(self.metadb[position])) + ".jpg"
        return closed_image_path

    # Error: class variable can't modify by pool.map()
    def paste_closed_image(self, argc):
        w_start, h_start = argc
        w_end = w_start + self.meta_width
        h_end = h_start + self.meta_height
        block_image = self.image.crop((w_start, h_start, w_end, h_end))
        hsv_value = self.cal_mean_hsv(block_image)
        image_path = self.find_closed(hsv_value)
        image = Image.open(image_path)
        paste_image = ImageOps.fit(
            image, (self.meta_width, self.meta_height), Image.LANCZOS)
        return paste_image
        # self.new_image.paste(paste_image, (w_start, h_start))

    # class variable can't modify by pool.map()
    # ========== parallel create new image: 2.7s ==========#
    def parallel_create_new_image(self):
        print("create new image...")
        start_time = time.time()
        argc = []
        width, height = self.image.size
        for w_start in range(0, width, self.meta_width):
            for h_start in range(0, height, self.meta_height):
                block_argc = [w_start, h_start]
                argc.append(block_argc)
        end_time_1 = time.time()
        # argc = [[w_start, h_start] for w_start in range(0, width, self.meta_width)]
        # 1: 6.87s;    2: 3.85s;    3: 2.94s;    4: 2.42s
        # 5: 2.11s;    6: 1.97s;    7: 1.87s;    8: 2.02s
        pool = Pool(7)
        paste_image_list = pool.map(self.paste_closed_image, argc)
        pool.close()
        pool.join()
        end_time_2 = time.time()

        count = 0
        for w_start in range(0, width, self.meta_width):
            for h_start in range(0, height, self.meta_height):
                self.new_image.paste(paste_image_list[count], (w_start, h_start))
                count += 1
        self.new_image = Image.blend(
            self.new_image, self.image, self.blend_scale)
        self.new_image.save(self.new_image_path)
        end_time = time.time()
        print(len(paste_image_list))
        print('Parallel create new image time for #init argc#:', end_time_1 - start_time)
        print('Parallel create new image time for #find closed#:', end_time_2 - end_time_1)
        print('Parallel create new image time for #paste image#:', end_time - end_time_2)
        print('Parallel create new image time:', end_time - start_time)

    # ========== no parallel create new image: 5.8s ==========#
    def create_new_image(self):
        print("create new image...")
        start_time = time.time()
        width, height = self.image.size
        for w_start in range(0, width, self.meta_width):
            for h_start in range(0, height, self.meta_height):
                w_end = w_start + self.meta_width
                h_end = h_start + self.meta_height
                block_image = self.image.crop((w_start, h_start, w_end, h_end))
                hsv_value = self.cal_mean_hsv(block_image)
                image_path = self.find_closed(hsv_value)
                image = Image.open(image_path)
                paste_image = ImageOps.fit(
                    image, (self.meta_width, self.meta_height), Image.LANCZOS)
                self.new_image.paste(paste_image, (w_start, h_start))
        self.new_image = Image.blend(
            self.new_image, self.image, self.blend_scale)
        self.new_image.save(self.new_image_path)
        end_time = time.time()
        print('No parallel create new image time:', end_time - start_time)


def test():
    h = HsvCompositeImage(image_path="D:/Study/File/千图成像/课程设计/示例图片/“森林”中的一只猫鼬.jpg",
                          imagedb_dir="D:/Study/File/千图成像/mjpg/",
                          meta_width=16,
                          meta_height=9,
                          blend_scale=0.5)
    # h.create_new_image()
    h.parallel_create_new_image()


if __name__ == '__main__':
    test()



