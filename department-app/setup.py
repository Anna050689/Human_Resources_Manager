import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Manager_of_Human_Resources_Department", # Replace with your own username
    version="0.0.1",
    author="Hanna Imshenetska",
    author_email="anna.imshen@gmail.com",
    description="The web application for managing departments and employees",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Anna050689/final_project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)