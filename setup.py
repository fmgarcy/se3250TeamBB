from setuptools import setup, find_packages

setup(name='se3250lib',
    version='0.1.0',
    author='Feona Mae Johnson',
    author_email='feonagarcia@gmail.com',
    description='Ship List, Weapons Inventory and Cost Formulas',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fmgarcy/se3250TeamBB.git',
    packages=find_packages(),  # Automatically finds all packages in directory (includes this library by default)
    install_requires=[
        # list other dependencies here
        'graphviz',
        'pandas',
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
    python_requires='>=3.6',
    zip_safe=False)