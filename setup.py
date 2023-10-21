from setuptools import setup, find_packages


classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Education',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          ]
setup(
    name='PyPly',
    version='0.0.1',
    description='A package to build new error messages using templates and infromation extracted from default Python error messages.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Mandisa Tunzi',
    author_email='mandytunzi@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='extractor',
    packages=find_packages(),
    install_requires=['']
)