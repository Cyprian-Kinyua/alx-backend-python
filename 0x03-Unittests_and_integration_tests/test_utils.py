#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function."""
    @parameterized.expand(
        [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )

    @parameterized.expand(
        [
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a" "b",), "'b'"),
        ]
    )


    def test_access_nested_map(self, nested_map, path, expected):
        """Test return value of access_nested_map ."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        """Test KeyError raised for invalid path."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)



