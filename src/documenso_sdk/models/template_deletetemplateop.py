"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from documenso_sdk import utils
from documenso_sdk.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, TypedDict


class TemplateDeleteTemplateRequestBodyTypedDict(TypedDict):
    template_id: float


class TemplateDeleteTemplateRequestBody(BaseModel):
    template_id: Annotated[float, pydantic.Field(alias="templateId")]


class TemplateDeleteTemplateTemplatesIssuesTypedDict(TypedDict):
    message: str


class TemplateDeleteTemplateTemplatesIssues(BaseModel):
    message: str


class TemplateDeleteTemplateTemplatesResponseResponseBodyData(BaseModel):
    message: str

    code: str

    issues: Optional[List[TemplateDeleteTemplateTemplatesIssues]] = None


class TemplateDeleteTemplateTemplatesResponseResponseBody(Exception):
    r"""Internal server error"""

    data: TemplateDeleteTemplateTemplatesResponseResponseBodyData

    def __init__(self, data: TemplateDeleteTemplateTemplatesResponseResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, TemplateDeleteTemplateTemplatesResponseResponseBodyData
        )


class TemplateDeleteTemplateIssuesTypedDict(TypedDict):
    message: str


class TemplateDeleteTemplateIssues(BaseModel):
    message: str


class TemplateDeleteTemplateTemplatesResponseBodyData(BaseModel):
    message: str

    code: str

    issues: Optional[List[TemplateDeleteTemplateIssues]] = None


class TemplateDeleteTemplateTemplatesResponseBody(Exception):
    r"""Invalid input data"""

    data: TemplateDeleteTemplateTemplatesResponseBodyData

    def __init__(self, data: TemplateDeleteTemplateTemplatesResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, TemplateDeleteTemplateTemplatesResponseBodyData
        )


class TemplateDeleteTemplateResponseBodyTypedDict(TypedDict):
    r"""Successful response"""

    success: bool


class TemplateDeleteTemplateResponseBody(BaseModel):
    r"""Successful response"""

    success: bool
