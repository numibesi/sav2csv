from setuptools import setup

setup(
    name='sav2csv',
    version='1.0.0',
    author='Harald von Waldow',
    author_email='harald.vonwaldow@eawag.ch',
    packages=['sav2csv'],
    url='https://github.com/eawag-rdm/sav2csv.git',
    license='GNU Affero General Public License',
    description='Convert a SPSS ".sav" file to CSV',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],
    install_requires=['savReaderWriter>=3.4.2'],
    entry_points={
        'console_scripts': ['sav2csv=sav2csv.sav2csv:main']
    }
)
