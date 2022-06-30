"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("d", ["/tools/SourcePoint"])
def test_directories(host, d):
    """Test that the expected directories were created and are not empty."""
    assert host.file(d).exists
    assert host.file(d).is_directory
    assert host.file(d).listdir()
    assert host.file(d).mode == 0o755


@pytest.mark.parametrize(
    "f",
    [
        # Profile created by go role
        "/etc/profile.d/go-path.sh",
        # Go file needed for build
        "/tools/SourcePoint/SourcePoint.go",
        # SourcePoint binary created from 'go build'
        "/tools/SourcePoint/SourcePoint",
    ],
)
def test_files(host, f):
    """Test that the expected files were created and are non-empty."""
    assert host.file(f).exists
    assert host.file(f).is_file
    assert host.file(f).content


@pytest.mark.parametrize("command", ["/tools/SourcePoint/SourcePoint"])
def test_commands(host, command):
    """Test that the expected commands are present."""
    assert host.exists(command)
