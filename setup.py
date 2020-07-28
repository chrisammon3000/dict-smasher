import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dict-smasher", # Replace with your own username
    version="0.0.1",
    author="Gregory Lindsey",
    author_email="gclindsey@gmail.com",
    description="Flatten Python dictionaries in one go.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gclindsey/dict-smasher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)