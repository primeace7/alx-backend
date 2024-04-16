#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Return deletion-resilient paginated data
        '''
        data = self.dataset()
        indexed_data = self.indexed_dataset()
        max_len = len(data)

        assert index >= 0 and index < max_len

        data = []
        count, i = 0, index
        while count < page_size:
            if indexed_data.get(i) is not None:
                data.append(indexed_data[i])
                count += 1
            i += 1
            if i >= max_len:
                break

        if i < max_len - 1:
            next_index = i
        else:
            next_index = None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
            }
