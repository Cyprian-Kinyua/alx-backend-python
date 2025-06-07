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
    def test_org(self):
        """Test that org method returns corrext JSON and that get_json is called once with correct url"""
        org_name = "google"
        client = GithubOrgClient(org_name)
        mock_response = {"name": org_name,
                         "repos_url": "https://api.github.com/orgs/google/repos"}
        client.org = Mock(return_value=mock_response)

        result = client.org()
        self.assertEqual(result, mock_response)
        client.org.assert_called_once()
