from setuptools import setup, find_packages

setup(
    name='wine_quality_predictor',
    version='0.1.0',
    author='Harsh Kumar',
    author_email='harshnpng@example.com',
    description='An MLOps-based Wine Quality Prediction project',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
