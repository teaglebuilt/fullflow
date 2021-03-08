from setuptools import setup, find_packages
from pathlib import Path


HERE = Path(__file__).parent.resolve()

with open('README.md') as readme_file:
    readme = readme_file.read()

# lab_path = (HERE / "fullflow" / "labextension")

# jstargets = [
#     str(lab_path / "package.json"),
# ]

requirements = [
    "apache-airflow:2.0.0",
    "jupyterlab=3.0.9"
]

setup(
    name='fullflow',
    description="Machine Learning and ETL Platform as a service.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    include_package_data=True,
    keywords='etl, pipelines, machinelearning',
    packages=find_packages(),
    test_suite='tests',
    url='https://github.com/teaglebuilt/fullflow',
    version='0.0.1',
    zip_safe=False
)