import os
from setuptools import find_packages, setup


def readme() -> str:
    """Utility function to read the README.md.
    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.
    Args:
        nothing
    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


setup(
    name='proyecto_rastreo_satelital_team_56',
    version='0.1.0',
    author='Alejandro Borda',
    author_email='alejandro.borda13@gmail.com',
    description='Proyecto del equipo 56 de DS4A Colombia Cohort 6 con Rastreo Satelital',
    python_requires='>=3',
    license="MIT",
    url='',
    packages=find_packages(),
    long_description=readme()
)