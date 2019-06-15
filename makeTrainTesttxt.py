"""A utility program to make train.txt and test.txt
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

_TEST_SEQ = [3, 4, 5, 8, 10, 16]
_TRAIN_SEQ = [0, 1, 2, 6, 7, 9, 11, 12, 13, 14, 15, 17, 18, 19, 20]


def main():
	"""Main function."""
	train_file = open("cache/train.txt", "w+")
	test_file = open("cache/test.txt", "w+")
	dataset = "data/KITTI_Tracking/seg_data"

	for seq in _TRAIN_SEQ:
		seq_name = str(seq).zfill(4)
		for file_name in sorted(os.listdir(os.path.join(dataset,seq_name))):
			train_file.write("{0}/{1}\n".format(seq_name, file_name))

	for seq in _TEST_SEQ:
		seq_name = str(seq).zfill(4)
		for file_name in sorted(os.listdir(os.path.join(dataset,seq_name))):
			test_file.write("{0}/{1}\n".format(seq_name, file_name))

	train_file.close()
	test_file.close()


if __name__=='__main__':
	main()
