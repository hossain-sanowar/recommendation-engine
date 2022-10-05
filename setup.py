from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()

##edit below variables as per the requirements
REPO_NAME = "book-recommendation"
AUTHOR_USER_NAME = "hossain-sanowar"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit','numpy']



setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Books Recommender Sysytem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="md.sanowar21@gmail.com"

)