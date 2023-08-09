from setuptools import setup, find_namespace_packages

setup(name='Infinity',
      version='0.1.0',
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
      entry_points={'console_scripts': ['Infinity=Infinity.main: main']})