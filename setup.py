from setuptools import setup, find_namespace_packages

setup(name='Infinity',
      version='0.2.1',
      description='This command-line program helps you manage your contact book, notes, and more with simple and intuitive commands.',
      url='https://github.com/Dishalex/Infinity',
      author='Oleksandr Dyshliuk, Dmytro Kruhlov, Michael Ivanov, Artem Dorofeev, Igor Yevtushenko',
      author_email='ivmv2007@gmail.com, a.dorofeev@ukr.net, dishalex@gmail.com, igr.yevtushenko@gmail.com, hazzy1451@gmail.com',
      license='MIT',
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent"],
      # packages=['Infinity'],
      include_package_data=True,
      packages=find_namespace_packages(),
      #entry_points={'console_scripts': ['start = Infinity.main:main']})
      entry_points={'console_scripts': ['bot = Infinity.main:main']},
      install_requires=["rich == 13.5.2",
                        "zipp == 3.16.2",
                        "spacy == 3.6.0",
                        "Levenshtein == 0.21.1"])
                        #"en-core-web-md == 3.6.0"])


# from setuptools import setup, find_namespace_packages

# setup(name='Infinity', # packege name
#     version='0.1.3',
#     description='Sorter of folder content',
#     url='https://github.com/MikeIV2007/HW-module-7/tree/main/clean_folder', #GitHab reference
#     author='Mykhailo Ivanov',
#     author_email='ivmv2007@gmail.com',
#     license='MIT',
#     classifires=[
#         "Programming Language :: Python"
#         "license :: OSI :: MIT license"
#         "Operation System :: OS Independunt"],
#     packages=find_namespace_packages(), # looking for all istalled packages
#     #data_files=['list of data files'], # not done yet
#     #include_package_data=True
#     install_requires='requires',#?
#     entry_points={'console_scripts': ['bot = Infinity.main:main']} # main : created function to privide input of arguments by means of sysargv
#     )


