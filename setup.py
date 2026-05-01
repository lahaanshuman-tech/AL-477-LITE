from setuptools import setup, find_packages

setup(
    name="al477lite",                     # PyPI package name
    version="0.1.0",                      # Start with 0.1.0
    packages=find_packages(),             # Automatically include al477lite/ folder
    install_requires=[],                  # No external deps (uses stdlib only)
    description="AL-477 Lite educational encoder/decoder library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Anshuman",
    author_email="your_email@example.com",  # replace with your email
    url="https://github.com/lahaanshuman-tech/al477lite",  # replace with your repo URL
    license="All Rights Reserved",        # or MIT/Apache if you want open source
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
