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

def get_oiv4_dataset():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__',
        '/m/061hd_', '/m/06m11', '/m/03120', '/m/01kb5b', '/m/0120dh', '/m/0dv5r', '/m/0jbk', '/m/0174n1', '/m/09f_2', '/m/01xq0k1', '/m/03jm5', '/m/02g30s', '/m/05z6w', '/m/01jfm_', '/m/076lb9', '/m/0gj37', '/m/0k0pj', '/m/0kpqd', '/m/0l14j_', '/m/0cyf8', '/m/0174k2', '/m/0dq75', '/m/076bq', '/m/07crc', '/m/0d8zb', '/m/0fszt', '/m/0k1tl', '/m/020kz', '/m/09728', '/m/07j7r', '/m/0fbdv', '/m/03ssj5', '/m/03qrc', '/m/02dl1y', '/m/01k6s3', '/m/02jfl0', '/m/01krhy', '/m/04kkgm', '/m/0ft9s', '/m/0d_2m', '/m/0czz2', '/m/0f4s2w', '/m/07dd4', '/m/0cgh4', '/m/03bbps', '/m/02pjr4', '/m/04p0qw', '/m/02pdsw', '/m/01yx86', '/m/09dzg', '/m/0hkxq', '/m/07dm6', '/m/054_l', '/m/01dws', '/m/027pcv', '/m/01d40f', '/m/02rgn06', '/m/0342h', '/m/06bt6', '/m/0323sq', '/m/02zvsm', '/m/02fq_6', '/m/01lrl', '/m/0k4j', '/m/04h7h', '/m/07xyvk', '/m/03y6mg', '/m/07r04', '/m/03__z0', '/m/019w40', '/m/09j5n', '/m/0cvnqh', '/m/01llwg', '/m/0c9ph5', '/m/015x5n', '/m/0gd2v', '/m/04v6l4', '/m/02jz0l', '/m/0dj6p', '/m/04ctx', '/m/080hkjn', '/m/01c648', '/m/01j61q', '/m/012n7d', '/m/025nd', '/m/09csl', '/m/01lcw4', '/m/0h8n5zk', '/m/0633h', '/m/01fdzj', '/m/01226z', '/m/0mw_6', '/m/04hgtk', '/m/02pv19', '/m/09qck', '/m/063rgb', '/m/0lt4_', '/m/0270h', '/m/01h3n', '/m/01mzpv', '/m/04169hn', '/m/0fm3zh', '/m/0d20w4', '/m/0_cp5', '/m/01dy8n', '/m/03m5k', '/m/03dnzn', '/m/0h8mzrc', '/m/0h8mhzd', '/m/03d443', '/m/01gllr', '/m/0642b4', '/m/09b5t', '/m/04yx4', '/m/01f8m5', '/m/015x4r', '/m/01j51', '/m/02zt3', '/m/03tw93', '/m/01jfsr', '/m/04ylt', '/m/0bt_c3', '/m/0cmx8', '/m/0hqkz', '/m/071qp', '/m/0cyhj_', '/m/01xygc', '/m/0420v5', '/m/0898b', '/m/01knjb', '/m/0199g', '/m/03c7gz', '/m/02x984l', '/m/04zwwv', '/m/04bcr3', '/m/0gv1x', '/m/01nq26', '/m/02s195', '/m/083kb', '/m/06nrc', '/m/0jyfg', '/m/0nybt', '/m/0176mf', '/m/01rzcn', '/m/0d4v4', '/m/03bk1', '/m/096mb', '/m/0h9mv', '/m/07yv9', '/m/0ph39', '/m/01rkbr', '/m/0gjbg72', '/m/06z37_', '/m/01m4t', '/m/035r7c', '/m/019jd', '/m/02tsc9', '/m/015wgc', '/m/0c06p', '/m/01dwwc', '/m/034c16', '/m/0242l', '/m/02lbcq', '/m/03nfch', '/m/03bt1vf', '/m/01lynh', '/m/03q5t', '/m/0fqt361', '/m/01bjv', '/m/01s55n', '/m/0283dt1', '/m/01z1kdw', '/m/016m2d', '/m/02dgv', '/m/07y_7', '/m/01_5g', '/m/06_72j', '/m/0ftb8', '/m/0c29q', '/m/0jg57', '/m/02l8p9', '/m/078jl', '/m/0llzx', '/m/0dbvp', '/m/09ct_', '/m/0dkzw', '/m/02p5f1q', '/m/0fx9l', '/m/01b9xk', '/m/0b3fp9', '/m/0h8n27j', '/m/0h8n6f9', '/m/01599', '/m/017ftj', '/m/044r5d', '/m/01dwsz', '/m/0cdl1', '/m/07gql', '/m/0hdln', '/m/0zvk5', '/m/012w5l', '/m/021sj1', '/m/0bh9flk', '/m/09gtd', '/m/0jwn_', '/m/02wv6h6', '/m/02wv84t', '/m/021mn', '/m/018p4k', '/m/06j2d', '/m/033cnk', '/m/01j3zr', '/m/03fwl', '/m/058qzx', '/m/06_fw', '/m/02x8cch', '/m/04g2r', '/m/01b638', '/m/099ssp', '/m/071p9', '/m/01gkx_', '/m/0b_rs', '/m/03v5tg', '/m/01j5ks', '/m/026t6', '/m/0_k2', '/m/039xj_', '/m/01b7fy', '/m/0220r2', '/m/015p6', '/m/0fly7', '/m/07c52', '/m/0n28_', '/m/0hg7b', '/m/019dx1', '/m/04vv5k', '/m/020jm', '/m/047v4b', '/m/01xs3r', '/m/03kt2w', '/m/03q69', '/m/01dxs', '/m/01h8tj', '/m/0dt3t', '/m/0cjq5', '/m/0h8lkj8', '/m/0271t', '/m/03q5c7', '/m/0fj52s', '/m/03vt0', '/m/01x3z', '/m/0d5gx', '/m/0h8my_4', '/m/03ldnb', '/m/0cjs7', '/m/0449p', '/m/04szw', '/m/07jdr', '/m/01yrx', '/m/06c54', '/m/04h8sr', '/m/050k8', '/m/0pg52', '/m/02f9f_', '/m/054fyh', '/m/09k_b', '/m/03xxp', '/m/0jly1', '/m/06k2mb', '/m/04yqq2', '/m/0bwd_0j', '/m/02h19r', '/m/02zn6n', '/m/07c6l', '/m/05zsy', '/m/025dyy', '/m/07j87', '/m/09ld4', '/m/01vbnl', '/m/0dzct', '/m/03fp41', '/m/0h2r6', '/m/0by6g', '/m/0cxn2', '/m/04tn4x', '/m/0f6wt', '/m/05n4y', '/m/0gxl3', '/m/02d9qx', '/m/04m9y', '/m/05z55', '/m/01x3jk', '/m/0h8l4fh', '/m/031b6r', '/m/01tcjp', '/m/01f91_', '/m/02522', '/m/0319l', '/m/0c_jw', '/m/0l515', '/m/0306r', '/m/0crjs', '/m/0ch_cf', '/m/02xwb', '/m/01r546', '/m/03rszm', '/m/0388q', '/m/03m3pdh', '/m/03k3r', '/m/0hf58v5', '/m/01y9k5', '/m/05441v', '/m/03p3bw', '/m/0175cv', '/m/0cmf2', '/m/0ccs93', '/m/02d1br', '/m/0gjkl', '/m/0jqgx', '/m/0h99cwc', '/m/047j0r', '/m/0k5j', '/m/0h8n6ft', '/m/0gm28', '/m/0130jx', '/m/04rmv', '/m/081qc', '/m/0qmmr', '/m/03fj2', '/m/040b_t', '/m/02y6n', '/m/0fqfqc', '/m/030610', '/m/07kng9', '/m/029b3', '/m/0fbw6', '/m/07qxg_', '/m/068zj', '/m/01g317', '/m/01bfm9', '/m/02068x', '/m/0fz0h', '/m/0jy4k', '/m/05kyg_', '/m/01prls', '/m/01h44', '/m/08pbxl', '/m/02gzp', '/m/04brg2', '/m/031n1', '/m/02jvh9', '/m/046dlr', '/m/0h8ntjv', '/m/0k65p', '/m/011k07', '/m/03grzl', '/m/06y5r', '/m/061_f', '/m/01cmb2', '/m/01mqdt', '/m/05r655', '/m/02p3w7d', '/m/029tx', '/m/04m6gz', '/m/015h_t', '/m/06pcq', '/m/01bms0', '/m/07fbm7', '/m/09tvcd', '/m/06nwz', '/m/0dv9c', '/m/083wq', '/m/0gd36', '/m/0138tl', '/m/07clx', '/m/05ctyq', '/m/0bjyj5', '/m/0dbzx', '/m/02ctlc', '/m/0fp6w', '/m/0djtd', '/m/0167gd', '/m/078n6m', '/m/0152hh', '/m/04gth', '/m/0ll1f78', '/m/0cffdh', '/m/025rp__', '/m/02_n6y', '/m/0wdt60w', '/m/0cydv', '/m/01n5jq', '/m/09rvcxw', '/m/013y1f', '/m/06ncr', '/m/015qff', '/m/024g6', '/m/05gqfk', '/m/0dv77', '/m/052sf', '/m/0cdn1', '/m/03jbxj', '/m/0cyfs', '/m/0kmg4', '/m/02cvgx', '/m/09kx5', '/m/057cc', '/m/02pkr5', '/m/057p5t', '/m/03g8mr', '/m/0frqm', '/m/03m3vtv', '/m/0584n8', '/m/014y4n', '/m/01g3x7', '/m/07cx4', '/m/07bgp', '/m/032b3c', '/m/01bl7v', '/m/0663v', '/m/0cn6p', '/m/02rdsp', '/m/02crq1', '/m/01xqw', '/m/0cnyhnx', '/m/01x_v', '/m/018xm', '/m/09ddx', '/m/084zz', '/m/01n4qj', '/m/07cmd', '/m/04_sv', '/m/0mkg', '/m/09d5_', '/m/0c568', '/m/02wbtzl', '/m/05bm6', '/m/01lsmm', '/m/0dftk', '/m/0dtln', '/m/0nl46', '/m/05r5c', '/m/06msq', '/m/0cd4d', '/m/05kms', '/m/02jnhm', '/m/0fldg', '/m/073bxn', '/m/029bxz', '/m/020lf', '/m/01btn', '/m/02vqfm', '/m/06__v', '/m/043nyj', '/m/0grw1', '/m/03hl4l9', '/m/0hnnb', '/m/04c0y', '/m/0dzf4', '/m/07v9_z', '/m/0f9_l', '/m/0703r8', '/m/01xyhv', '/m/01fh4r', '/m/04dr76w', '/m/0pcr', '/m/03s_tn', '/m/07mhn', '/m/01hrv5', '/m/019h78', '/m/09kmb', '/m/0h23m', '/m/050gv4', '/m/01fb_0', '/m/02w3_ws', '/m/014j1m', '/m/01gmv2', '/m/04y4h8h', '/m/026qbn5', '/m/01m2v', '/m/05_5p_0', '/m/07030', '/m/01s105', '/m/033rq4', '/m/0162_1', '/m/02z51p', '/m/06mf6', '/m/02hj4', '/m/0bt9lr', '/m/08hvt4', '/m/084rd', '/m/01pns0', '/m/014sv8', '/m/079cl', '/m/01940j', '/m/05vtc', '/m/02w3r3', '/m/054xkw', '/m/01bqk0', '/m/09g1w'
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

def get_blued_dataset():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__',
        'beard', 'black_frame_glasses', 'police_cap', 'sun_glasses', 'stud_earrings', 'mouth_mask', 'bangs', 'tattoo', 'shirt', 'suit', 'tie', 'belt', 'jeans', 'shorts', 'leg_hair', 'military_uniform', 'under_shirt', 'gloves', 'pecs', 'abdominal_muscles', 'calf', 'briefs', 'boxers', 'butt', 'leather_shoes', 'black_socks', 'white_socks', 'feet', 'non_leather_shoes', 'hot_pants'
    ]
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds
