#!/usr/bin/env python3
""""Unit tests for utils module."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test return value of access_nested_map ."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b",), "'b'"),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception_message):
        """Test KeyError raised for invalid path."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(
            str(context.exception), expected_exception_message)


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": "true"}),
        ("http://holberton.io", {"payload": "false"}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test return value of get_json."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """"Test that memoize decorator caches return value of a method."""

    def test_memoize(self):
        """" Test that memoized property calls method only once."""

        class TestClass:
            """Test class with a method and a memoized property."""

            def a_method(self):
                """A simple method to be memoized."""
                return 42

            @memoize
            def a_property(self):
                """ Memoized property calling a_method"""

                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            obj = TestClass()

            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
