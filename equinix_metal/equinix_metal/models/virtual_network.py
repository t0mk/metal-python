# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from equinix_metal.models.href import Href
from equinix_metal.models.metal_gateway_lite import MetalGatewayLite

class VirtualNetwork(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    assigned_to: Optional[Href] = None
    assigned_to_virtual_circuit: Optional[StrictBool] = Field(None, description="True if the virtual network is attached to a virtual circuit. False if not.")
    description: Optional[StrictStr] = None
    facility: Optional[Href] = None
    href: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    instances: Optional[List[Href]] = Field(None, description="A list of instances with ports currently associated to this Virtual Network.")
    metal_gateways: Optional[List[MetalGatewayLite]] = Field(None, description="A list of metal gateways currently associated to this Virtual Network.")
    metro: Optional[Href] = None
    metro_code: Optional[StrictStr] = Field(None, description="The Metro code of the metro in which this Virtual Network is defined.")
    vxlan: Optional[StrictInt] = None
    __properties = ["assigned_to", "assigned_to_virtual_circuit", "description", "facility", "href", "id", "instances", "metal_gateways", "metro", "metro_code", "vxlan"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> VirtualNetwork:
        """Create an instance of VirtualNetwork from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of assigned_to
        if self.assigned_to:
            _dict['assigned_to'] = self.assigned_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of facility
        if self.facility:
            _dict['facility'] = self.facility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in instances (list)
        _items = []
        if self.instances:
            for _item in self.instances:
                if _item:
                    _items.append(_item.to_dict())
            _dict['instances'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metal_gateways (list)
        _items = []
        if self.metal_gateways:
            for _item in self.metal_gateways:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metal_gateways'] = _items
        # override the default output from pydantic by calling `to_dict()` of metro
        if self.metro:
            _dict['metro'] = self.metro.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VirtualNetwork:
        """Create an instance of VirtualNetwork from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return VirtualNetwork.parse_obj(obj)

        _obj = VirtualNetwork.parse_obj({
            "assigned_to": Href.from_dict(obj.get("assigned_to")) if obj.get("assigned_to") is not None else None,
            "assigned_to_virtual_circuit": obj.get("assigned_to_virtual_circuit"),
            "description": obj.get("description"),
            "facility": Href.from_dict(obj.get("facility")) if obj.get("facility") is not None else None,
            "href": obj.get("href"),
            "id": obj.get("id"),
            "instances": [Href.from_dict(_item) for _item in obj.get("instances")] if obj.get("instances") is not None else None,
            "metal_gateways": [MetalGatewayLite.from_dict(_item) for _item in obj.get("metal_gateways")] if obj.get("metal_gateways") is not None else None,
            "metro": Href.from_dict(obj.get("metro")) if obj.get("metro") is not None else None,
            "metro_code": obj.get("metro_code"),
            "vxlan": obj.get("vxlan")
        })
        return _obj
