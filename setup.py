from setuptools import setup, find_packages

setup(
    name='anifolder',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'set-folder-icon=meu_pacote.meu_modulo:set_folder_icon',
        ],
    },
)