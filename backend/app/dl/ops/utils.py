import os
import shutil
import sys

import cv2
import numpy as np


from PIL import Image


def softmax(scores):
    es = np.exp(scores - scores.max(axis=-1)[..., None])
    return es / es.sum(axis=-1)[..., None]


class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


def accuracy(output, target, topk=(1,)):
    """Computes the precision@k for the specified values of k"""
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res


def frame2video(im_dir, video_dir, fps=10):
    im_list = os.listdir(im_dir)
    print(im_list)
    # im_list.sort(key=lambda x: int(x.replace("frame", "").split('.')[0]))  # 最好再看看图片顺序对不
    img = Image.open(os.path.join(im_dir, im_list[0]))
    img_size = img.size  # 获得图片分辨率，im_dir文件夹下的图片分辨率需要一致

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # opencv版本是3
    videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)
    for i in im_list:
        im_name = os.path.join(im_dir + i)
        frame = cv2.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)
        videoWriter.write(frame)
    videoWriter.release()
    print('finish')


def video2frame(videos_path, frames_save_path):
    '''
    :param videos_path: 视频的存放路径
    :param frames_save_path: 视频切分成帧之后图片的保存路径
    :param time_interval: 保存间隔
    :return:
    '''
    vidcap = cv2.VideoCapture(videos_path)
    success, image = vidcap.read()
    count = 0
    while success:
        count += 1
        cv2.imencode('.jpg', image)[1].tofile(frames_save_path + "/%d.jpg" % count)
        success, image = vidcap.read()


if __name__ == '__main__':
    # im_dir = "E:\Download\lipDatasets\\1.训练集\lip_train\\0ae1886855358e19a5059a64e21a77f5\\"  # 帧存放路径
    # video_dir = 'C:\\Users\\11542\Desktop\\test.avi'  # 合成视频存放的路径
    # fps = 10  # 帧率，每秒钟帧数越多，所显示的动作就会越流畅
    # frame2video(im_dir, video_dir, fps)
    file_name = sys.argv[1]
    video_path = "/www/backend/static/" + file_name
    save_path = "/www/backend/app/dl/data/2.测试集/lip_test/0a9890743e6f1d0cabc1ebf41232a1a3"
    shutil.rmtree(save_path)
    os.mkdir(save_path)
    video2frame(video_path, save_path)
    os.system("python /www/backend/app/dl/main.py")
