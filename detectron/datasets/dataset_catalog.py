# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

"""Collection of available datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


# Path to data dir
_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Required dataset entry keys
_IM_DIR = 'image_directory'
_ANN_FN = 'annotation_file'

# Optional dataset entry keys
_IM_PREFIX = 'image_prefix'
_DEVKIT_DIR = 'devkit_directory'
_RAW_DIR = 'raw_dir'

# Available datasets
_DATASETS = {
    'cityscapes_fine_instanceonly_seg_train': {
        _IM_DIR:
            _DATA_DIR + '/cityscapes/images',
        _ANN_FN:
            _DATA_DIR + '/cityscapes/annotations/instancesonly_gtFine_train.json',
        _RAW_DIR:
            _DATA_DIR + '/cityscapes/raw'
    },
    'cityscapes_fine_instanceonly_seg_val': {
        _IM_DIR:
            _DATA_DIR + '/cityscapes/images',
        # use filtered validation as there is an issue converting contours
        _ANN_FN:
            _DATA_DIR + '/cityscapes/annotations/instancesonly_filtered_gtFine_val.json',
        _RAW_DIR:
            _DATA_DIR + '/cityscapes/raw'
    },
    'cityscapes_fine_instanceonly_seg_test': {
        _IM_DIR:
            _DATA_DIR + '/cityscapes/images',
        _ANN_FN:
            _DATA_DIR + '/cityscapes/annotations/instancesonly_gtFine_test.json',
        _RAW_DIR:
            _DATA_DIR + '/cityscapes/raw'
    },
    'coco_2014_train': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_train2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/instances_train2014.json'
    },
    'coco_2014_val': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_val2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/instances_val2014.json'
    },
    'coco_2014_minival': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_val2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/instances_minival2014.json'
    },
    'coco_2014_valminusminival': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_val2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/instances_valminusminival2014.json'
    },
    'coco_2015_test': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_test2015',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/image_info_test2015.json'
    },
    'coco_2015_test-dev': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_test2015',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/image_info_test-dev2015.json'
    },
    'coco_2017_test': {  # 2017 test uses 2015 test images
        _IM_DIR:
            _DATA_DIR + '/coco/coco_test2015',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/image_info_test2017.json',
        _IM_PREFIX:
            'COCO_test2015_'
    },
    'coco_2017_test-dev': {  # 2017 test-dev uses 2015 test images
        _IM_DIR:
            _DATA_DIR + '/coco/coco_test2015',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/image_info_test-dev2017.json',
        _IM_PREFIX:
            'COCO_test2015_'
    },
    'coco_stuff_train': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_train2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/coco_stuff_train.json'
    },
    'coco_stuff_val': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_val2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/coco_stuff_val.json'
    },
    'keypoints_coco_2014_train': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_train2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/person_keypoints_train2014.json'
    },
    'keypoints_coco_2014_val': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_val2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/person_keypoints_val2014.json'
    },
    'keypoints_coco_2014_minival': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_val2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/person_keypoints_minival2014.json'
    },
    'keypoints_coco_2014_valminusminival': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_val2014',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/person_keypoints_valminusminival2014.json'
    },
    'keypoints_coco_2015_test': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_test2015',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/image_info_test2015.json'
    },
    'keypoints_coco_2015_test-dev': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_test2015',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/image_info_test-dev2015.json'
    },
    'voc_2007_train': {
        _IM_DIR:
            _DATA_DIR + '/VOC2007/JPEGImages',
        _ANN_FN:
            _DATA_DIR + '/VOC2007/annotations/voc_2007_train.json',
        _DEVKIT_DIR:
            _DATA_DIR + '/VOC2007/VOCdevkit2007'
    },
    'voc_2007_val': {
        _IM_DIR:
            _DATA_DIR + '/VOC2007/JPEGImages',
        _ANN_FN:
            _DATA_DIR + '/VOC2007/annotations/voc_2007_val.json',
        _DEVKIT_DIR:
            _DATA_DIR + '/VOC2007/VOCdevkit2007'
    },
    'voc_2007_test': {
        _IM_DIR:
            _DATA_DIR + '/VOC2007/JPEGImages',
        _ANN_FN:
            _DATA_DIR + '/VOC2007/annotations/voc_2007_test.json',
        _DEVKIT_DIR:
            _DATA_DIR + '/VOC2007/VOCdevkit2007'
    },
    'voc_2012_train': {
        _IM_DIR:
            _DATA_DIR + '/VOC2012/JPEGImages',
        _ANN_FN:
            _DATA_DIR + '/VOC2012/annotations/voc_2012_train.json',
        _DEVKIT_DIR:
            _DATA_DIR + '/VOC2012/VOCdevkit2012'
    },
    'voc_2012_val': {
        _IM_DIR:
            _DATA_DIR + '/VOC2012/JPEGImages',
        _ANN_FN:
            _DATA_DIR + '/VOC2012/annotations/voc_2012_val.json',
        _DEVKIT_DIR:
            _DATA_DIR + '/VOC2012/VOCdevkit2012'
    },
    # -------- customized config --------
    # coco 2017 annotations
    'coco_2017_train': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_train2017',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/instances_train2017.json'
    },
    'coco_2017_val': {
        _IM_DIR:
            _DATA_DIR + '/coco/coco_val2017',
        _ANN_FN:
            _DATA_DIR + '/coco/annotations/instances_val2017.json'
    },
    # oiv4 coco-style annotations
    'openimage_v4_train': {
        _IM_DIR:
            _DATA_DIR + '/openimage/train',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-train-annotations-bbox.json'
    },
    'openimage_v4_dev': {
        _IM_DIR:
            _DATA_DIR + '/openimage/validation',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/validation-annotations-bbox.json'
    },
    'openimage_v4_test': {
        _IM_DIR:
            _DATA_DIR + '/openimage/test',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/test-annotations-bbox.json'
    },
    # oiv4-challenge-2018 coco-style annotations
    'openimage_challenge_2018_train_off': {
        _IM_DIR:
            _DATA_DIR + '/openimage/Image',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-train-official-annotations-bbox.json'
    },
    'openimage_challenge_2018_train_ext': {
        _IM_DIR:
            _DATA_DIR + '/openimage/Image',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-train-extended-annotations-bbox.json'
    },
    'openimage_challenge_2018_train_hc_50': {
        _IM_DIR:
            _DATA_DIR + '/openimage/Image',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-train-hardcat-50-annotations-bbox.json'
    },
    'openimage_challenge_2018_train_hc_51': {
        _IM_DIR:
            _DATA_DIR + '/openimage/Image',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-train-hardcat-51-annotations-bbox.json'
    },
    'openimage_challenge_2018_validation': {
        _IM_DIR:
            _DATA_DIR + '/openimage/Image',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-validation-annotations-bbox.json'
    },
    'openimage_challenge_2018_validation_hc_50': {
        _IM_DIR:
            _DATA_DIR + '/openimage/Image',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-validation-hardcat-50-annotations-bbox.json'
    },
    'openimage_challenge_2018_validation_hc_51': {
        _IM_DIR:
            _DATA_DIR + '/openimage/Image',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-validation-hardcat-51-annotations-bbox.json'
    },
    'openimage_challenge_2018_test': {
        _IM_DIR:
            _DATA_DIR + '/openimage/test-challenge/challenge2018_test',
        _ANN_FN:
            _DATA_DIR + '/openimage/annotations/challenge-2018-test-annotations-bbox-mock.json'
    },
    # blued 
    'blued_0920_train': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_train.json'
    },
    'blued_0920_test': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test.json'
    },
    'blued_0920_test_abdominal_muscles': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_abdominal_muscles.json'
    },
    'blued_0920_test_bangs': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_bangs.json'
    },
    'blued_0920_test_beard': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_beard.json'
    },
    'blued_0920_test_black_frame_glasses': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_black_frame_glasses.json'
    },
    'blued_0920_test_black_socks': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_black_socks.json'
    },
    'blued_0920_test_boxers': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_boxers.json'
    },
    'blued_0920_test_briefs': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_briefs.json'
    },
    'blued_0920_test_calf': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_calf.json'
    },
    'blued_0920_test_feet': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_feet.json'
    },
    'blued_0920_test_leather_shoes': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_leather_shoes.json'
    },
    'blued_0920_test_pecs': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_pecs.json'
    },
    'blued_0920_test_shorts': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_shorts.json'
    },
    'blued_0920_test_stud_earrings': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_stud_earrings.json'
    },
    'blued_0920_test_suit': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_suit.json'
    },
    'blued_0920_test_sun_glasses': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_sun_glasses.json'
    },
    'blued_0920_test_tattoo': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_tattoo.json'
    },
    'blued_0920_test_under_shirt': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_under_shirt.json'
    },
    'blued_0920_test_white_socks': {
        _IM_DIR:
            _DATA_DIR + '/blued/blued_0920/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/blued_0920/Lists/annotations/annotation-0920_test_white_socks.json'
    },
    'qblued_20180803_train': {
        _IM_DIR:
            _DATA_DIR + '/blued/qblued_20180803/Image',
        _ANN_FN:
            _DATA_DIR + '/blued/qblued_20180803/Lists/annotations/qblued_20180803_0926_train.json'
    },
    # juggdet
    'juggdet_0503_train': {
        _IM_DIR:
            _DATA_DIR + '/juggdet/juggdet_0503/Image',
        _ANN_FN:
            _DATA_DIR + '/juggdet/juggdet_0503/Lists/annotations/juggdet_0503_train_0712.json'
    },
    'juggdet_0503_test': {
        _IM_DIR:
            _DATA_DIR + '/juggdet/juggdet_0503/Image',
        _ANN_FN:
            _DATA_DIR + '/juggdet/juggdet_0503/Lists/annotations/juggdet_0503_test_0821.json'
    },
    'juggdet_0622_train': {
        _IM_DIR:
            _DATA_DIR + '/juggdet/juggdet_0622/Image',
        _ANN_FN:
            _DATA_DIR + '/juggdet/juggdet_0622/Lists/annotations/juggdet_0622_train_0927.json'
    }
    # -----------------------------------
}


def datasets():
    """Retrieve the list of available dataset names."""
    return _DATASETS.keys()


def contains(name):
    """Determine if the dataset is in the catalog."""
    return name in _DATASETS.keys()


def get_im_dir(name):
    """Retrieve the image directory for the dataset."""
    return _DATASETS[name][_IM_DIR]


def get_ann_fn(name):
    """Retrieve the annotation file for the dataset."""
    return _DATASETS[name][_ANN_FN]


def get_im_prefix(name):
    """Retrieve the image prefix for the dataset."""
    return _DATASETS[name][_IM_PREFIX] if _IM_PREFIX in _DATASETS[name] else ''


def get_devkit_dir(name):
    """Retrieve the devkit dir for the dataset."""
    return _DATASETS[name][_DEVKIT_DIR]


def get_raw_dir(name):
    """Retrieve the raw dir for the dataset."""
    return _DATASETS[name][_RAW_DIR]
