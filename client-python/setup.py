# coding: utf-8

"""
    Gene Feature Enumeration Service

    The Gene Feature Enumeration (GFE) Submission service provides an API for converting raw sequence data to GFE. It provides both a RESTful API and a simple user interface for converting raw sequence data to GFE results. Sequences can be submitted one at a time or as a fasta file. This service uses <a href=\"https://github.com/nmdp-bioinformatics/service-feature\">nmdp-bioinformatics/service-feature</a> for encoding the raw sequence data and <a href=\"https://github.com/nmdp-bioinformatics/HSA\">nmdp-bioinformatics/HSA</a> for aligning the raw sequence data. The code is open source, and available on <a href=\"https://github.com/nmdp-bioinformatics/service-gfe-submission\">GitHub</a>.<br><br>Go to <a href=\"http://service-gfe-submission.readthedocs.io\">service-gfe-submission.readthedocs.io</a> for more information

    OpenAPI spec version: 1.0.7
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "swagger_client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Gene Feature Enumeration Service",
    author_email="mhalagan@nmdp.org",
    url="",
    keywords=["Swagger", "Gene Feature Enumeration Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Gene Feature Enumeration (GFE) Submission service provides an API for converting raw sequence data to GFE. It provides both a RESTful API and a simple user interface for converting raw sequence data to GFE results. Sequences can be submitted one at a time or as a fasta file. This service uses &lt;a href&#x3D;\&quot;https://github.com/nmdp-bioinformatics/service-feature\&quot;&gt;nmdp-bioinformatics/service-feature&lt;/a&gt; for encoding the raw sequence data and &lt;a href&#x3D;\&quot;https://github.com/nmdp-bioinformatics/HSA\&quot;&gt;nmdp-bioinformatics/HSA&lt;/a&gt; for aligning the raw sequence data. The code is open source, and available on &lt;a href&#x3D;\&quot;https://github.com/nmdp-bioinformatics/service-gfe-submission\&quot;&gt;GitHub&lt;/a&gt;.&lt;br&gt;&lt;br&gt;Go to &lt;a href&#x3D;\&quot;http://service-gfe-submission.readthedocs.io\&quot;&gt;service-gfe-submission.readthedocs.io&lt;/a&gt; for more information
    """
)
