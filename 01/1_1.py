from random import shuffle
import unittest
import numpy as np

def selectionSortInplaceC(array:list):
    sublist_boundary = 0
    for _ in range(len(array)):
        # find smallest
        curr_small = sublist_boundary
        for i in range(sublist_boundary,len(array)):
            curr_small = i if array[i]<array[curr_small] else curr_small
        array[sublist_boundary],array[curr_small] =array[curr_small], array[sublist_boundary]
        sublist_boundary+=1 


class TestInplaceSort(unittest.TestCase):
    def test_sort_even(self):
        random_list = np.random.randint(0,100,size=100)
        input_list = random_list.tolist()
        selectionSortInplaceC(input_list)
        random_list.sort()
        self.assertListEqual(random_list.tolist(),input_list)
    def test_sort_uneven(self):
        random_list = np.random.randint(0,100,size=101)
        input_list = random_list.tolist()
        selectionSortInplaceC(input_list)
        random_list.sort()
        self.assertListEqual(random_list.tolist(),input_list)
    def test_sort_sorted(self):
        random_list = np.random.randint(0,100,size=100)
        random_list.sort()
        input_list = random_list.tolist()
        selectionSortInplaceC(input_list)
        self.assertListEqual(random_list.tolist(),input_list)

    def test_sort_negative(self):
        random_list = np.random.randint(0,100,size=100)*-1
        input_list = random_list.tolist()
        selectionSortInplaceC(input_list)
        random_list.sort()
        self.assertListEqual(random_list.tolist(),input_list)

    def test_sort_empty(self):
        input_list = []
        selectionSortInplaceC(input_list)
        self.assertListEqual([],input_list)

    def test_sort_one(self):
        random_list = np.random.randint(0,100,size=1)
        input_list = random_list.tolist()
        selectionSortInplaceC(input_list)
        random_list.sort()
        self.assertListEqual(random_list.tolist(),input_list)

unittest.main()