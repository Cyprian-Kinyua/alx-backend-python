#!/usr/bin/env python3
"""generic utilities for a github org client"""

from typing import Any, Mapping, Sequence, Dict, Callable
from functools import wraps
import requests

__all__ = [
    'access_nested_map',
    'get_json',
    'memoize',
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a nested dictionary map using a path of keys."""
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Dict:
    """Fetch JSON content from a remote URL."""
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """Decorator to cache (memoize) method results."""
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """Memoized wrapsfunction."""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
