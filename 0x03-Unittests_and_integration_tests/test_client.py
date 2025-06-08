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
        """
        Test that org method returns corrext
          JSON and that get_json is called once with correct url
        """
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        result = client.org()

        expected_url = f"https://api.github.com/orgs/{org_name}"
        self.assertEqual(result, expected_response)
        mock_get_json.assert_called_once_with(expected_url)

    @patch("client.GithubOrgClient.org", new_callable=property)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns the 
        expected value from mocked org.
        """
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test/repos"}
        client = GithubOrgClient("testorg")
        result = client._public_repos_url
        expected_url = "https://api.github.com/orgs/testorg/repos"
        self.assertEqual(result, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected list of repo names."""
        expected_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = expected_payload

        with patch(
                'client.GithubOrgClient._public_repos_url',
                return_value="https://api.github.com/orgs/test/repos"
        ) as mock_repos_url:
            client = GithubOrgClient("testorg")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once()
            mock_repos_url.assert_called_once()

        if __name__ == "__main__":
            unittest.main()
