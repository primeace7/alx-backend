#!/usr/bin/env python3
'''simple server response pagination implementation'''
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    '''return start and end index values for an API
    data index
    '''
    start = (page - 1) * page_size
    stop = start + page_size
    return (start, stop)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        limits = index_range(page, page_size)
        start = limits[0]
        stop = limits[1]
        max_len = len(data)
        if start > max_len:
            return []
        if stop > max_len:
            stop = max_len

        result = data[start: stop + 1]
        return result