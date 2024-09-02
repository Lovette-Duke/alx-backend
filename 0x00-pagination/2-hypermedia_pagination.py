#!/usr/bin/env python3
"""Hpermedia Pagination"""


import csv
import math
from typing import List, Tuple


class Server:
    """class to paginate the popular baby names dataset."""
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
        """verifies that page and page_size are ints,
        returns a chunk of a dataset."""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns dict of pagination metadata."""
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages}


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple containing a start index
    and an end index for pagination params."""
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
