#!/usr/bin/env python3
"""
Version management script for local development.
Generates a unique version using timestamp for local builds.
"""

import os
import time
from datetime import datetime

def get_version():
    """Get version for the package"""
    base_version = "1.0"
    
    # Check for CI environment variables
    azure_build = os.getenv("BUILD_BUILDNUMBER")
    github_run = os.getenv("GITHUB_RUN_NUMBER")
    
    if azure_build:
        # Azure DevOps build number
        return f"{base_version}.{azure_build}"
    elif github_run:
        # GitHub Actions run number
        return f"{base_version}.{github_run}"
    else:
        # Local development - use timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{base_version}.{timestamp}"

def update_version_file():
    """Update version.txt file with current version"""
    version = get_version()
    with open("version.txt", "w") as f:
        f.write(version)
    print(f"Version updated to: {version}")
    return version

if __name__ == "__main__":
    update_version_file()