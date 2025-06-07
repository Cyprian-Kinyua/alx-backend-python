#!/usr/bin/env python3
"""Unit tests for client module."""

import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google",
                    "id": 123, }),
        ("abc", {"login": "abc",
                 "id": 456, }),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that org method returns corrext JSON and that get_json is called once with correct url"""
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        result = client.org()

        expected_url = f"https://api.github.com/orgs/{org_name}"
        self.assertEqual(result, expected_response)
        mock_get_json.assert_called_once_with(expected_url)
