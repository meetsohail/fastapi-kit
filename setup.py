from setuptools import setup, find_packages

setup(
    name="fastforge",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "fastforge=fastforge.cli:main",
        ],
    },
    python_requires=">=3.8",
)
