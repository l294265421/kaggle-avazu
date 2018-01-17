#!/usr/bin/env python3

import argparse, csv, hashlib

base_dir = r'D:\document\program\ml\machine-learning-databases\kaggle\Click-Through Rate Prediction\\'
train = base_dir + 'train.csv'
test = base_dir + 'test.csv'

parser = argparse.ArgumentParser(description='process some integers')
parser.add_argument('--csv_path', type=str, nargs=1, help='set path to the csv file', default=test)
parser.add_argument('--out_path', type=str, nargs=1, help='set path to the svm file', default=base_dir+'va.r0.csv')
args = parser.parse_args()

CSV_PATH, OUT_PATH = args.csv_path, args.out_path

f = csv.writer(open(OUT_PATH, 'w'))
for i, row in enumerate(csv.reader(open(CSV_PATH))):
    if i == 0:
        row.insert(1, 'click')
    else:
        row.insert(1, '0')
    f.writerow(row)
