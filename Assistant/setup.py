from setuptools import setup, find_namespace_packages

setup(
    name='Assistant_bot',
    version='1',
    description='Assistant with a command line interface',
    # url='https://github.com',
    author='Psar Yelyzaveta, ',
    license='MIT',
    include_package_data=True,
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    data_files=[("Assistant", ["Assistant/address_book.py", "Assistant/bot.py",
                "Assistant/classes.py", "Assistant/notes.py", "Assistant/sort.py", "Assistant/translate.py"])],
    entry_points={'console_scripts': ['assistant = Assistant.assistant:main']}
)