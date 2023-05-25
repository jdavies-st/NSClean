from setuptools import setup

setup(name='nsclean',
      version='1.5',
      description='Clean residual noise from JWST NIRSpec images',
      author='Bernard J. Rauscher',
      author_email='Bernard.J.Rauscher@nasa.gov',
      packages=['nsclean'],
      install_requires=[
          'astropy',
          'numpy',
          'Pillow',
      ],
      zip_safe=False)
