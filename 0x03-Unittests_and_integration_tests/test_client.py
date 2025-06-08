#!/usr/bin/env python3
"""Unit tests for client module."""

import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized
import fixtures
from parameterized import parameterized_class


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos,
    }
])
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license returns True if the repo
          has the specified license.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @classmethod
    def setUpClass(cls):
        """Set up the mock for requests.get to return test fixtures."""
        cls.get_patcher = patch("requests.get")

        mock_get = cls.get_patcher.start()

        # Mock .json() responses for each URL
        mock_get.side_effect = lambda url: Mock(json=lambda: (
            cls.org_payload if url == "https://api.github.com/orgs/testorg"
            else cls.repos_payload
        ))

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns all expected repo names."""
        client = GithubOrgClient("testorg")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos filters repos by license."""
        client = GithubOrgClient("testorg")
        self.assertEqual(client.public_repos(
            license="apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
