from setuptools import setup, find_packages

setup(
    name='pmsa',
    version='0.0.1',
    description='Patrol Management System App',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)