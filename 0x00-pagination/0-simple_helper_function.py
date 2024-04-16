#!/usr/bin/env python3
'''simple helper function to calculate pagination parameters'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''return start and end index values for an API
    data index
    '''
    start = (page - 1) * page_size
    stop = start + page_size
    return (start, stop)
