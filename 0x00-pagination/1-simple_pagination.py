#!/usr/bin/env python3
"""
a function named index_range that takes
two integer arguments page and page_size
"""

import csv
import math
from typing import List
import logging


def index_range(page: int, page_size: int) -> tuple:
    '''a function to take page and page size
    and returns a tuple of size two,
    containing a 'start index' and an 'end index' corresponding to
    the range of indexes
    to return in a list for those particular pagination parameters.
    '''

    offset = (page - 1) * page_size
    end = page * page_size
    return (offset, end)

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
        '''
        Retrieve a specific page of data.
        '''
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise TypeError('Page and page_size must be integers.')
        assert page > 0, f"Expected page to be > 0" 
        assert page_size > 0, f"Expected page_size to be > 0" 
        n_index_range = index_range(page=page, page_size=page_size)
        try:
            page_data = self.dataset()[n_index_range[0]: n_index_range[1]]
        except IndexError:
            logging.error("Failed to retrieve the specified page.")
        return []
