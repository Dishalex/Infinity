from setuptools import setup, find_namespace_packages

setup(name='Infinity',
      version='0.2.6',
      description='This command-line program helps you manage your contact book, notes, and more with simple and intuitive commands.',
      url='https://github.com/Dishalex/Infinity',
      author='Oleksandr Dyshliuk, Dmytro Kruhlov, Michael Ivanov, Artem Dorofeev, Igor Yevtushenko',
      author_email='ivmv2007@gmail.com, a.dorofeev@ukr.net, dishalex@gmail.com, igr.yevtushenko@gmail.com, hazzy1451@gmail.com',
      license='MIT',
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent"],

      include_package_data=True,
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['infinity = Infinity.main:main']},
      install_requires=["rich == 13.5.2",
                        "zipp == 3.16.2",
                        "spacy == 3.6.0",
                        "Levenshtein == 0.21.1",
                        "en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.6.0/en_core_web_md-3.6.0-py3-none-any.whl"
                        ])



