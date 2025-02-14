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
        """Returns a dictionary with pagination details while handling deletions."""
        assert isinstance(index, int) and 0 <= index < len(self.__indexed_dataset)
        dataset = self.indexed_dataset()
        sorted_indexes = sorted(dataset.keys()) 
        
        while index not in dataset and index < sorted_indexes[-1]:
            index += 1
        
        data = []
        current_position = index
        for _ in range(page_size):
            if current_position in dataset:
                data.append(dataset[current_position])
            current_position += 1
            if current_position > sorted_indexes[-1]:
                break

        next_index = current_position if current_position in dataset else None
        
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
