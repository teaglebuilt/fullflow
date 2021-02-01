from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "apache-airflow:2.0.0"
]

setup(
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Machine Learning and ETL Platform as a service.",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    license='Apache License, Version 2.0',
    include_package_data=True,
    keywords='etl, pipelines, machinelearning',
    name='fullflow',
    packages=find_packages(),
    test_suite='tests',
    url='https://github.com/teaglebuilt/fullflow',
    version='0.0.1',
    zip_safe=False,
)