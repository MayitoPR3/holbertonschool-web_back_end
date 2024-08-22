#!/usr/bin/env python3

""" 1. Simple pagination """

import csv
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of
    popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.
        """
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise TypeError("Both page and page_size must be integers.")
        if page <= 0 or page_size <= 0:
            raise ValueError("Both page and page_size must be greater than 0.")

        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end]
