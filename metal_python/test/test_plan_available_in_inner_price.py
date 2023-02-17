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

import metal_python
from metal_python.models.plan_available_in_inner_price import PlanAvailableInInnerPrice  # noqa: E501
from metal_python.rest import ApiException

class TestPlanAvailableInInnerPrice(unittest.TestCase):
    """PlanAvailableInInnerPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PlanAvailableInInnerPrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanAvailableInInnerPrice`
        """
        model = metal_python.models.plan_available_in_inner_price.PlanAvailableInInnerPrice()  # noqa: E501
        if include_optional :
            return PlanAvailableInInnerPrice(
                hour = 1.23, 
                href = ''
            )
        else :
            return PlanAvailableInInnerPrice(
        )
        """

    def testPlanAvailableInInnerPrice(self):
        """Test PlanAvailableInInnerPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()