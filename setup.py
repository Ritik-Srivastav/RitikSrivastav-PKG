import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME  = "RitikSrivastav-pkg"
USER_NAME = "Ritik-Srivastav"

setuptools.setup(
    name = f"{PROJECT_NAME}-{USER_NAME}",
    version = "0.0.2",
    author = USER_NAME,
    author_email = "ritiksrivastav773@gmail.com",
    description = "a small package for perceptron",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    install_requires = [
        "numpy==1.21.6",
        "pandas==1.1.5",
        "joblib==1.1.0"
    ]
)