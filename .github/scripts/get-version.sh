#!/bin/bash
set -e

# Extract version from pyproject.toml
VERSION=$(grep -m 1 '^version =' pyproject.toml | cut -d '"' -f 2)

IS_PRERELEASE="false"

# Check to handle both PEP 440 (0.2.1a1) and SemVer (0.2.1-alpha.1)
if [[ "$VERSION" =~ [ab] ]] || [[ "$VERSION" == *"alpha"* ]] || [[ "$VERSION" == *"beta"* ]]; then
  IS_PRERELEASE="true"
fi

echo "VERSION=$VERSION" >> $GITHUB_OUTPUT
echo "IS_PRERELEASE=$IS_PRERELEASE" >> $GITHUB_OUTPUT
