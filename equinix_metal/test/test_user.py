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
from equinix_metal.models.user import User  # noqa: E501
from equinix_metal.rest import ApiException

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = equinix_metal.models.user.User()  # noqa: E501
        if include_optional :
            return User(
                avatar_thumb_url = '', 
                avatar_url = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                customdata = equinix_metal.models.customdata.customdata(), 
                email = '', 
                emails = [
                    equinix_metal.models.href.Href(
                        href = '', )
                    ], 
                first_name = '', 
                fraud_score = '', 
                full_name = '', 
                href = '', 
                id = '', 
                last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_name = '', 
                max_organizations = 56, 
                max_projects = 56, 
                phone_number = '', 
                short_id = '', 
                timezone = '', 
                two_factor_auth = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return User(
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()