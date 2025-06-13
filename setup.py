from setuptools import setup

setup(
    name='sav2csv',
    version='1.2.0',  # versão bump
    author='Nuno Simões',
    author_email='nuno.simoes@wdx.pt',
    packages=['sav2csv'],
    url='https://github.com/numibesi/sav2csv',  # apontar para o seu fork
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    description='Convert a SPSS .sav file to CSV (fork com pyreadstat/pandas)',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
    install_requires=[
        'pyreadstat>=1.2.9',
        'pandas>=2.3.0',
    ],
    entry_points={
        'console_scripts': [
            'sav2csv=sav2csv.sav2csv:main',
        ],
    },
)
