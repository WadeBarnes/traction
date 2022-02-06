# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from acapy_wrapper.models.keylist_query_paginate import KeylistQueryPaginate


class KeylistQuery(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistQuery - a model defined in OpenAPI

        id: The id of this KeylistQuery [Optional].
        type: The type of this KeylistQuery [Optional].
        filter: The filter of this KeylistQuery [Optional].
        paginate: The paginate of this KeylistQuery [Optional].
    """

    id: Optional[str] = None
    type: Optional[str] = None
    filter: Optional[Dict[str, Any]] = None
    paginate: Optional[KeylistQueryPaginate] = None


KeylistQuery.update_forward_refs()
