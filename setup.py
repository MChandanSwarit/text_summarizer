import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "text_summarizer"    
AUTHOR_USER_NAME = "MChandanSwarit"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "chandanswarit2804@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/MChandanSwarit/textSummarizer",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

