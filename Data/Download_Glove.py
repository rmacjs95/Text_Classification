'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
RMDL: Random Multimodel Deep Learning for Classification
 * Copyright (C) 2018  Kamran Kowsari <kk7nc@virginia.edu>
 * Last Update: 04/25/2018
 * This file is part of  RMDL project, University of Virginia.
 * Free to use, change, share and distribute source code of RMDL
 * Refrenced paper : RMDL: Random Multimodel Deep Learning for Classification
 * Refrenced paper : An Improvement of Data Classification using Random Multimodel Deep Learning (RMDL)
 * Comments and Error: email: kk7nc@virginia.edu
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


from __future__ import print_function

import os, sys, tarfile
import numpy as np
import zipfile

if sys.version_info >= (3, 0, 0):
    import urllib.request as urllib  # ugly but works
else:
    import urllib

print(sys.version_info)

# image shape


# path to the directory with the data
DATA_DIR = '.\Glove'

# url of the binary data



# path to the binary train file with image data


def download_and_extract(data='Wikipedia'):
    """
    Download and extract the GloVe
    :return: None
    """
    
    data_dict = {
        'Wikipedia':'http://nlp.stanford.edu/data/glove.6B.zip',
        'Common_Crawl_840B':'http://nlp.stanford.edu/data/wordvecs/glove.840B.300d.zip',
        'Common_Crawl_42B':'http://nlp.stanford.edu/data/wordvecs/glove.42B.300d.zip',
        'Twitter':'http://nlp.stanford.edu/data/wordvecs/glove.twitter.27B.zip'
    }
    
    if data in data_dict.keys():
        DATA_URL = data_dict[data]
    else:
        print("prameter should be Twitter, Common_Crawl_42B, Common_Crawl_840B, or Wikipedia")
        exit(0)

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    filename = DATA_URL.split('/')[-1]
    filepath = os.path.join(DATA_DIR, filename)
    print(filepath)

    path = os.path.abspath(DATA_DIR)
    if not os.path.exists(filepath):
        def _progress(count, block_size, total_size):
            sys.stdout.write('\rDownloading %s %.2f%%' % (filename,
                                                          float(count * block_size) / float(total_size) * 100.0))
            sys.stdout.flush()

        filepath, _ = urllib.urlretrieve(DATA_URL, filepath)#, reporthook=_progress)


        zip_ref = zipfile.ZipFile(filepath, 'r')
        zip_ref.extractall(DATA_DIR)
        zip_ref.close()
    return path
