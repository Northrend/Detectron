from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import defaultdict
import argparse
import cv2  # NOQA (Must import before importing caffe2 due to bug in cv2)
import glob
import logging
import os
import sys
import time

from caffe2.python import workspace
from caffe2.python import net_drawer

from core.config import assert_and_infer_cfg
from core.config import cfg
from core.config import merge_cfg_from_file
from utils.io import cache_url
from utils.timer import Timer
import core.test_engine as infer_engine
import datasets.dummy_datasets as dummy_datasets
import utils.c2 as c2_utils
import utils.logging
import utils.vis as vis_utils


def get_model(cfg_file, weights_file):
    merge_cfg_from_file(cfg_file)
    cfg.TRAIN.WEIGHTS = '' # NOTE: do not download pretrained model weights
    cfg.TEST.WEIGHTS = weights_file
    cfg.NUM_GPUS = 1
    assert_and_infer_cfg()
    model = infer_engine.initialize_model_from_cfg()
    return model

cfg_file = '/workspace/Detectron/configs/coco/e2e_mask_rcnn_R-101-FPN_0412.yaml'
weights_file = '/workspace/northrend/coco/model/mask_rcnn_R-101-FPN_0412/train/coco_2017_train/generalized_rcnn/model_final.pkl'
model = get_model(cfg_file, weights_file)

g = net_drawer.GetPydotGraph(model, rankdir="TB")
g.write_dot(model.Proto().name + '.dot')
