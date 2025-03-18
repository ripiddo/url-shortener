# pylint: disable=W0201, C0415

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

NAME = 'url-shortener'
VERSION = '0.1'
AUTHOR = 'Sinan Tukek'
REQUIRED_PYTHON_VERSION = (3, 8)
PACKAGES = ['urlshortener']
INSTALL_DEPENDENCIES = [
    'Flask==1.1.2',
    "SQLAlchemy==1.3.20",
    "alembic>=1.5.5",
    "Flask-SQLAlchemy==2.4.4",
    "Flask-Migrate==2.5.3",
    "Flask-Script==2.0.6",
    "Flask-Cors==3.0.9",
    "requests==2.25.0",
    "mysqlclient==2.0.3",
    "pika==1.1.0",
    "pytest==6.2.2",
    "setuptools>=53.1.0",
    "Werkzeug==1.0.1"

]
SETUP_DEPENDENCIES = [
]
TEST_DEPENDENCIES = [
    'pytest'
]
EXTRA_DEPENDENCIES = {
    'dev': [
        'pytest',
        'pylint',
        'pylint-flask',
        'pylint-flask-sqlalchemy'
    ],
    'doc': [
        'Sphinx'
    ]
}

if sys.version_info < REQUIRED_PYTHON_VERSION:
    sys.exit(f'Python >= {REQUIRED_PYTHON_VERSION[0]}.{REQUIRED_PYTHON_VERSION[1]}'
             ' is required. Your version: {sys.version}')


class PyTest(TestCommand):
    """
    Use pytest to run tests
    """
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_DEPENDENCIES,
    setup_requires=SETUP_DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
    extras_require=EXTRA_DEPENDENCIES,
    cmdclass={
        'test': PyTest
    }
)
