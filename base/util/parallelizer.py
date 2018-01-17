#!/usr/bin/env python3

import argparse, sys

from base.converter.common import *

def parse_args(label):
    base_dir = r'D:\document\program\ml\machine-learning-databases\kaggle\Click-Through Rate Prediction\\'
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='nr_thread', default=12, type=int)
    parser.add_argument('--cvt_path', default=base_dir+'converter/2.py')
    parser.add_argument('--tr_src_path', default=base_dir+'tr.r0.{label}.new.csv'.format(label=label))
    parser.add_argument('--va_src_path', default=base_dir+'va.r0.{label}.new.csv'.format(label=label))
    parser.add_argument('--tr_dst_path', default=base_dir+'tr.r0.{label}.sp'.format(label=label))
    parser.add_argument('--va_dst_path', default=base_dir+'va.r0.{label}.sp'.format(label=label))
    args = vars(parser.parse_args())

    return args

def main():
    label = 'app'
    args = parse_args(label)

    nr_thread = args['nr_thread']
    
    split(args['tr_src_path'], nr_thread, True)
    split(args['va_src_path'], nr_thread, True)

    parallel_convert(args['cvt_path'], [args['tr_src_path'], args['va_src_path'], args['tr_dst_path'], args['va_dst_path']], nr_thread)

    delete(args['tr_src_path'], nr_thread)
    delete(args['va_src_path'], nr_thread)

    cat(args['tr_dst_path'], nr_thread)
    cat(args['va_dst_path'], nr_thread)

    delete(args['tr_dst_path'], nr_thread)
    delete(args['va_dst_path'], nr_thread)

main()
