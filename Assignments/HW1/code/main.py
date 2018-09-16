import skimage.io
import numpy as np
import torchvision
import matplotlib.pyplot as plt

import util
import deep_recog
import visual_words
import visual_recog

if __name__ == '__main__':

    num_cores = util.get_num_CPU()

    # path_img = "../data/kitchen/sun_aasmevtpkslccptd.jpg"
    # path_img = "../data/auditorium/sun_afcwsapxpihedtku.jpg" # 4 channels
    # image = skimage.io.imread(path_img)
    # image = image.astype('float')/255
    # filter_responses = visual_words.extract_filter_responses(image)
    # util.display_filter_responses(filter_responses)

    visual_words.compute_dictionary(num_workers=num_cores)
    
    # dictionary = np.load('dictionary.npy')
    # img = visual_words.get_visual_words(image,dictionary)
    # util.save_wordmap(wordmap, filename)
    # visual_recog.build_recognition_system(num_workers=num_cores)

    # conf, accuracy = visual_recog.evaluate_recognition_system(num_workers=num_cores)
    # print(conf)
    # print(np.diag(conf).sum()/conf.sum())

    # vgg16 = torchvision.models.vgg16(pretrained=True).double()
    # vgg16.eval()
    # deep_recog.build_recognition_system(vgg16,num_workers=num_cores//2)
    # conf = deep_recog.evaluate_recognition_system(vgg16,num_workers=num_cores//2)
    # print(conf)
    # print(np.diag(conf).sum()/conf.sum())

