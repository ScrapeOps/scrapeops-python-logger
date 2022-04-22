from setuptools import setup, find_packages


VERSION = '0.4.7'
DESCRIPTION = 'Scrapeops Python Logger, is a library used by the ScrapeOps Python SDKs.'

setup(name='scrapeops_python_logger',
      description=DESCRIPTION,
      long_description=DESCRIPTION,
      author="ScrapeOps",
      author_email="info@scrapeops.io",
      version=VERSION,
      license="BSD",
      url="https://github.com/ScrapeOps/scrapeops-python-logger",
      packages=find_packages(),
      install_requires=[
          "tld>=0.12.4",
          "requests>=2.24.0",
          "json5>=0.9.5",
          "urllib3>=1.25.10",
          "itemadapter>=0.4.0",
          ],
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
      ],
      python_requires=">=3.6",
      )