# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.v20_cred_filter import V20CredFilter
from acapy_wrapper.models.v20_cred_preview import V20CredPreview


class V20CredBoundOfferRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredBoundOfferRequest - a model defined in OpenAPI

        counter_preview: The counter_preview of this V20CredBoundOfferRequest [Optional].
        filter: The filter of this V20CredBoundOfferRequest [Optional].
    """

    counter_preview: Optional[V20CredPreview] = None
    filter: Optional[V20CredFilter] = None


V20CredBoundOfferRequest.update_forward_refs()
