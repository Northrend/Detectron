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
"""Provide stub objects that can act as stand-in "dummy" datasets for simple use
cases, like getting all classes in a dataset. This exists so that demos can be
run without requiring users to download/install datasets first.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from detectron.utils.collections import AttrDict


def get_coco_dataset():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
        'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
        'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
        'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
        'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',
        'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
        'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass',
        'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich',
        'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake',
        'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
        'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
        'scissors', 'teddy bear', 'hair drier', 'toothbrush'
    ]
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds


def get_juggdet_dataset():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__',
        'penis',
        'vulva',
        'sex',
        'tits',
        'breasts',
        'nipples',
        'ass',
        'tback',
        'anus'
    ]
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds

def get_oiv4_hc_50_dataset():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__',
        '/m/0fqt361', '/m/0271t', '/m/05bm6', '/m/0dtln', '/m/07cx4', '/m/0f4s2w', '/m/06bt6', '/m/027pcv', '/m/0jbk', '/m/0wdt60w', '/m/02ctlc', '/m/01s105', '/m/0djtd', '/m/01prls', '/m/03xxp', '/m/0fqfqc', '/m/0gjbg72', '/m/01btn', '/m/04h8sr', '/m/015h_t', '/m/04brg2', '/m/0dv77', '/m/01s55n', '/m/019dx1', '/m/04szw', '/m/0h99cwc', '/m/02rdsp', '/m/083kb', '/m/0frqm', '/m/04m6gz', '/m/0k0pj', '/m/0283dt1', '/m/0dkzw', '/m/0k65p', '/m/07mhn', '/m/039xj_', '/m/0k5j', '/m/0hf58v5', '/m/035r7c', '/m/0c_jw', '/m/03q69', '/m/07yv9', '/m/0175cv', '/m/01rzcn', '/m/0dzf4', '/m/03m3vtv', '/m/04hgtk', '/m/014sv8', '/m/02pkr5', '/m/02d1br'
    ]
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds
