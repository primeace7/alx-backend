#!/usr/bin/env python3
'''simple server response pagination implementation'''
from typing import Tuple, List, Mapping, Union
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
        '''return a subset of the babynames dataset corresponding to
        the requested page and page size
        '''
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

        result = data[start: stop]
        return result

    def get_hyper(self, page: int = 1, page_size: int =
                  10) -> Mapping[str, Union[None, int, List[List]]]:
        '''return a hypermedia subset of the babynames dataset
        corresponding to the requested page and page size'''
        data = self.get_page(page, page_size)

        results = self.dataset()
        max_len = len(results)
        limits = index_range(page, page_size)

        next_page = page + 1 if limits[1] < max_len else None
        prev_page = page - 1 if limits[0] > page_size else None
        total_pages = math.ceil(max_len / page_size)

        return {'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
