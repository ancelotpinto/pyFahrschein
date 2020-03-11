import re

import fahrschein

# https://github.com/semver/semver/blob/master/semver.md#is-there-a-suggested-regular
# -expression-regex-to-check-a-semver-string
SEMVER_REGEX = r"^(?P<major>0|[1-9]\d*)\." \
               r"(?P<minor>0|[1-9]\d*)\." \
               r"(?P<patch>0|[1-9]\d*)" \
               r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)" \
               r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?" \
               r"(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"


def test_version_regex():
    assert re.search(SEMVER_REGEX, fahrschein.VERSION)


def test_version_pyproject_toml():
    import tomlkit
    config = tomlkit.loads(open('pyproject.toml').read())
    assert config['tool']['poetry']['version'] == fahrschein.VERSION
