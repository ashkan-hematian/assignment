import os
from typing import List, Any


def is_convertible_to_int(obj: str) -> bool:
    try:
        int(obj)
        return True
    except (ValueError, TypeError):
        return False


def extract_file_names() -> List[str]:
    try:
        filenames_str = os.getenv('FILENAMES', '')
        if filenames_str is '':
            return []
        filenames: list[str] = filenames_str.split(',')
        return filenames
    except SyntaxError:
        return []
