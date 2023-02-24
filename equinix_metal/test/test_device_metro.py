# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import equinix_metal
from equinix_metal.models.device_metro import DeviceMetro  # noqa: E501
from equinix_metal.rest import ApiException

class TestDeviceMetro(unittest.TestCase):
    """DeviceMetro unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceMetro
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceMetro`
        """
        model = equinix_metal.models.device_metro.DeviceMetro()  # noqa: E501
        if include_optional :
            return DeviceMetro(
                code = '', 
                country = '', 
                id = '', 
                name = '', 
                href = ''
            )
        else :
            return DeviceMetro(
        )
        """

    def testDeviceMetro(self):
        """Test DeviceMetro"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()