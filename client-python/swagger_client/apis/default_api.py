# coding: utf-8

"""
    Gene Feature Enumeration Service

    The Gene Feature Enumeration (GFE) Submission service provides an API for converting raw sequence data to GFE. It provides both a RESTful API and a simple user interface for converting raw sequence data to GFE results. Sequences can be submitted one at a time or as a fasta file. This service uses <a href=\"https://github.com/nmdp-bioinformatics/service-feature\">nmdp-bioinformatics/service-feature</a> for encoding the raw sequence data and <a href=\"https://github.com/nmdp-bioinformatics/HSA\">nmdp-bioinformatics/HSA</a> for aligning the raw sequence data. The code is open source, and available on <a href=\"https://github.com/nmdp-bioinformatics/service-gfe-submission\">GitHub</a>.<br><br>Go to <a href=\"http://service-gfe-submission.readthedocs.io\">service-gfe-submission.readthedocs.io</a> for more information

    OpenAPI spec version: 1.0.7
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def fasta_post(self, **kwargs):
        """
        Get Gene Feature Enumeration (GFE) from fasta file
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fasta_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str locus: Valid HLA, KIR or ABO locus
        :param file file: HML file
        :param int retry: Number of retry requests to feature-service
        :param str feature_url: URL for the feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: SubjectData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.fasta_post_with_http_info(**kwargs)
        else:
            (data) = self.fasta_post_with_http_info(**kwargs)
            return data

    def fasta_post_with_http_info(self, **kwargs):
        """
        Get Gene Feature Enumeration (GFE) from fasta file
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fasta_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str locus: Valid HLA, KIR or ABO locus
        :param file file: HML file
        :param int retry: Number of retry requests to feature-service
        :param str feature_url: URL for the feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: SubjectData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['locus', 'file', 'retry', 'feature_url', 'structures', 'verbose']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fasta_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/fasta'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'retry' in params:
            query_params['retry'] = params['retry']
        if 'feature_url' in params:
            query_params['feature_url'] = params['feature_url']
        if 'structures' in params:
            query_params['structures'] = params['structures']
        if 'verbose' in params:
            query_params['verbose'] = params['verbose']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'locus' in params:
            form_params.append(('locus', params['locus']))
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SubjectData',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def flowhml_post(self, **kwargs):
        """
        Get Gene Feature Enumeration (GFE) from HML file using nextflow
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.flowhml_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: HML file
        :param str type: Option for returning HML or JSON
        :param str feature_url: URL for the feature-service
        :param int retry: Number of retry requests to feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: SubjectData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.flowhml_post_with_http_info(**kwargs)
        else:
            (data) = self.flowhml_post_with_http_info(**kwargs)
            return data

    def flowhml_post_with_http_info(self, **kwargs):
        """
        Get Gene Feature Enumeration (GFE) from HML file using nextflow
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.flowhml_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: HML file
        :param str type: Option for returning HML or JSON
        :param str feature_url: URL for the feature-service
        :param int retry: Number of retry requests to feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: SubjectData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'type', 'feature_url', 'retry', 'structures', 'verbose']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method flowhml_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/flowhml'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']
        if 'feature_url' in params:
            query_params['feature_url'] = params['feature_url']
        if 'retry' in params:
            query_params['retry'] = params['retry']
        if 'structures' in params:
            query_params['structures'] = params['structures']
        if 'verbose' in params:
            query_params['verbose'] = params['verbose']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SubjectData',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def gfe_post(self, locus, sequence, **kwargs):
        """
        Get Gene Feature Enumeration (GFE) from sequence and locus
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.gfe_post(locus, sequence, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str locus: Valid HLA, KIR or ABO locus (required)
        :param str sequence: Sequence data (required)
        :param int retry: Number of retry requests to feature-service
        :param str feature_url: URL for the feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: Typing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.gfe_post_with_http_info(locus, sequence, **kwargs)
        else:
            (data) = self.gfe_post_with_http_info(locus, sequence, **kwargs)
            return data

    def gfe_post_with_http_info(self, locus, sequence, **kwargs):
        """
        Get Gene Feature Enumeration (GFE) from sequence and locus
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.gfe_post_with_http_info(locus, sequence, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str locus: Valid HLA, KIR or ABO locus (required)
        :param str sequence: Sequence data (required)
        :param int retry: Number of retry requests to feature-service
        :param str feature_url: URL for the feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: Typing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['locus', 'sequence', 'retry', 'feature_url', 'structures', 'verbose']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gfe_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'locus' is set
        if ('locus' not in params) or (params['locus'] is None):
            raise ValueError("Missing the required parameter `locus` when calling `gfe_post`")
        # verify the required parameter 'sequence' is set
        if ('sequence' not in params) or (params['sequence'] is None):
            raise ValueError("Missing the required parameter `sequence` when calling `gfe_post`")


        collection_formats = {}

        resource_path = '/gfe'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'locus' in params:
            query_params['locus'] = params['locus']
        if 'sequence' in params:
            query_params['sequence'] = params['sequence']
        if 'retry' in params:
            query_params['retry'] = params['retry']
        if 'feature_url' in params:
            query_params['feature_url'] = params['feature_url']
        if 'structures' in params:
            query_params['structures'] = params['structures']
        if 'verbose' in params:
            query_params['verbose'] = params['verbose']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Typing',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def hml_post(self, **kwargs):
        """
        Get Gene Feature Enumeration (GFE) from HML file
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.hml_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: HML file
        :param str type: Option for returning HML or JSON
        :param str feature_url: URL for the feature-service
        :param int retry: Number of retry requests to feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: SubjectData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.hml_post_with_http_info(**kwargs)
        else:
            (data) = self.hml_post_with_http_info(**kwargs)
            return data

    def hml_post_with_http_info(self, **kwargs):
        """
        Get Gene Feature Enumeration (GFE) from HML file
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.hml_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: HML file
        :param str type: Option for returning HML or JSON
        :param str feature_url: URL for the feature-service
        :param int retry: Number of retry requests to feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: SubjectData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'type', 'feature_url', 'retry', 'structures', 'verbose']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hml_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/hml'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']
        if 'feature_url' in params:
            query_params['feature_url'] = params['feature_url']
        if 'retry' in params:
            query_params['retry'] = params['retry']
        if 'structures' in params:
            query_params['structures'] = params['structures']
        if 'verbose' in params:
            query_params['verbose'] = params['verbose']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SubjectData',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def sequence_post(self, locus, gfe, **kwargs):
        """
        Get sequence data from gene feature enumeration (GFE) annotation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sequence_post(locus, gfe, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str locus: Valid HLA, KIR or ABO locus (required)
        :param str gfe: GFE annotation (required)
        :param int retry: Number of retry requests to feature-service
        :param str feature_url: URL for the feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: Sequence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sequence_post_with_http_info(locus, gfe, **kwargs)
        else:
            (data) = self.sequence_post_with_http_info(locus, gfe, **kwargs)
            return data

    def sequence_post_with_http_info(self, locus, gfe, **kwargs):
        """
        Get sequence data from gene feature enumeration (GFE) annotation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sequence_post_with_http_info(locus, gfe, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str locus: Valid HLA, KIR or ABO locus (required)
        :param str gfe: GFE annotation (required)
        :param int retry: Number of retry requests to feature-service
        :param str feature_url: URL for the feature-service
        :param bool structures: Flag for returning the sequence and accession number of each feature
        :param bool verbose: Flag for running service in verbose
        :return: Sequence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['locus', 'gfe', 'retry', 'feature_url', 'structures', 'verbose']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sequence_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'locus' is set
        if ('locus' not in params) or (params['locus'] is None):
            raise ValueError("Missing the required parameter `locus` when calling `sequence_post`")
        # verify the required parameter 'gfe' is set
        if ('gfe' not in params) or (params['gfe'] is None):
            raise ValueError("Missing the required parameter `gfe` when calling `sequence_post`")


        collection_formats = {}

        resource_path = '/sequence'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'locus' in params:
            query_params['locus'] = params['locus']
        if 'gfe' in params:
            query_params['gfe'] = params['gfe']
        if 'retry' in params:
            query_params['retry'] = params['retry']
        if 'feature_url' in params:
            query_params['feature_url'] = params['feature_url']
        if 'structures' in params:
            query_params['structures'] = params['structures']
        if 'verbose' in params:
            query_params['verbose'] = params['verbose']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Sequence',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)