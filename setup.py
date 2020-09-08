from setuptools import setup
setup(name='Main',
      version='1',
      description='Style transfer',
      install_requires=[
          'tensorflow',
          'tensorflow-hub',
          'matplotlib',
          'numpy',
          'pillow'
      ],
      zip_safe=False)