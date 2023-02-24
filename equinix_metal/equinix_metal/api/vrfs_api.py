# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import List, Optional

from equinix_metal.models.vrf_ip_reservation import VrfIpReservation

from equinix_metal.api_client import ApiClient
from equinix_metal.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VRFsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def find_vrf_ip_reservation(self, vrf_id : Annotated[StrictStr, Field(..., description="VRF UUID")], id : Annotated[StrictStr, Field(..., description="IP UUID")], include : Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.")] = None, exclude : Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.")] = None, **kwargs) -> VrfIpReservation:  # noqa: E501
        """Retrieve all VRF IP Reservations in the VRF  # noqa: E501

        Returns the IP Reservation for the VRF.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_vrf_ip_reservation(vrf_id, id, include, exclude, async_req=True)
        >>> result = thread.get()

        :param vrf_id: VRF UUID (required)
        :type vrf_id: str
        :param id: IP UUID (required)
        :type id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: List[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VrfIpReservation
        """
        kwargs['_return_http_data_only'] = True
        return self.find_vrf_ip_reservation_with_http_info(vrf_id, id, include, exclude, **kwargs)  # noqa: E501

    @validate_arguments
    def find_vrf_ip_reservation_with_http_info(self, vrf_id : Annotated[StrictStr, Field(..., description="VRF UUID")], id : Annotated[StrictStr, Field(..., description="IP UUID")], include : Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.")] = None, exclude : Annotated[Optional[List[StrictStr]], Field(description="Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.")] = None, **kwargs):  # noqa: E501
        """Retrieve all VRF IP Reservations in the VRF  # noqa: E501

        Returns the IP Reservation for the VRF.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_vrf_ip_reservation_with_http_info(vrf_id, id, include, exclude, async_req=True)
        >>> result = thread.get()

        :param vrf_id: VRF UUID (required)
        :type vrf_id: str
        :param id: IP UUID (required)
        :type id: str
        :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
        :type include: List[str]
        :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
        :type exclude: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VrfIpReservation, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vrf_id',
            'id',
            'include',
            'exclude'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_vrf_ip_reservation" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['vrf_id']:
            _path_params['vrf_id'] = _params['vrf_id']
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []
        if _params.get('include') is not None:  # noqa: E501
            _query_params.append(('include', _params['include']))
            _collection_formats['include'] = 'multi'
        if _params.get('exclude') is not None:  # noqa: E501
            _query_params.append(('exclude', _params['exclude']))
            _collection_formats['exclude'] = 'multi'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['x_auth_token']  # noqa: E501

        _response_types_map = {
            '200': "VrfIpReservation",
            '403': "Error",
            '404': "Error",
        }

        return self.api_client.call_api(
            '/vrfs/{vrf_id}/ips/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))