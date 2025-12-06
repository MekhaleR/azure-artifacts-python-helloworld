import os
from datetime import datetime
from setuptools import setup, find_packages

def get_version():
    """Get version for the package"""
    base_version = "1.0"
    
    # Check for CI environment variables
    azure_build = os.getenv("BUILD_BUILDNUMBER")
    github_run = os.getenv("GITHUB_RUN_NUMBER")
    
    if azure_build:
        # Azure DevOps build number (format: yyyymmdd.r)
        return f"{base_version}.{azure_build}"
    elif github_run:
        # GitHub Actions run number
        return f"{base_version}.{github_run}"
    else:
        # Local development - use timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{base_version}.{timestamp}"

# For backward compatibility and dynamic version access
__version__ = get_version()

if __name__ == "__main__":
    setup(
        name="azurehello",
        version=__version__,
        packages=find_packages(),
        install_requires=[],
        author="Atul J. Kamble",
        description="Basic Python Hello World package published to Azure Artifacts",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        python_requires=">=3.8",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9", 
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
        ],
    )