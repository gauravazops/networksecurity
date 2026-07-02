from setuptools import setup, find_packages

from typing import List

requirement_lst = List[str]
def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """
    try:
        with open("requirements.txt") as file:
            ## Read lines from the file 
            lines = file.readlines()
            ## Process each line 
            for line in lines:
                requirement = line.strip()
                ## Ignore empty line and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Gaurav Lalwani",
    author_email="gaurav.lalwani@example.com",
    packages=find_packages(),
    install_requires=get_requirements()
)