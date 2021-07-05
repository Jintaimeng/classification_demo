import pickle
import numpy as np
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
label_name = ["airplane",
             "automobile",
             "bird",
              "cat",
              "deer",
              "dog",
              "frog",
              "horse",
              "ship",
              "truck"]
import glob

train_list = glob.glob("/home/jinyue/PycharmProjects/cifar-10-python/data_batch_*")
print(train_list)
for l in train_list:
    print(l)
    l_dict = unpickle(l)
    #print(l_dict)
    print(l_dict.keys())
    for im_idx, im_data in enumerate(l_dict[b'data']):
        print(im_idx)
        print(im_data)