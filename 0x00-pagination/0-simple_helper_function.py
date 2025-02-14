#!/usr/bin/env python3
'a function that takes two arguments'
from typing import Tuple

def index_range(page, page_size) -> Tuple[int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
