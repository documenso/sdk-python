"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from documenso_sdk import utils
from documenso_sdk.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, TypedDict


class RecipientDeleteDocumentRecipientRequestBodyTypedDict(TypedDict):
    recipient_id: float


class RecipientDeleteDocumentRecipientRequestBody(BaseModel):
    recipient_id: Annotated[float, pydantic.Field(alias="recipientId")]


class RecipientDeleteDocumentRecipientDocumentsRecipientsIssuesTypedDict(TypedDict):
    message: str


class RecipientDeleteDocumentRecipientDocumentsRecipientsIssues(BaseModel):
    message: str


class RecipientDeleteDocumentRecipientDocumentsRecipientsResponseResponseBodyData(
    BaseModel
):
    message: str

    code: str

    issues: Optional[
        List[RecipientDeleteDocumentRecipientDocumentsRecipientsIssues]
    ] = None


class RecipientDeleteDocumentRecipientDocumentsRecipientsResponseResponseBody(
    Exception
):
    r"""Internal server error"""

    data: RecipientDeleteDocumentRecipientDocumentsRecipientsResponseResponseBodyData

    def __init__(
        self,
        data: RecipientDeleteDocumentRecipientDocumentsRecipientsResponseResponseBodyData,
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data,
            RecipientDeleteDocumentRecipientDocumentsRecipientsResponseResponseBodyData,
        )


class RecipientDeleteDocumentRecipientIssuesTypedDict(TypedDict):
    message: str


class RecipientDeleteDocumentRecipientIssues(BaseModel):
    message: str


class RecipientDeleteDocumentRecipientDocumentsRecipientsResponseBodyData(BaseModel):
    message: str

    code: str

    issues: Optional[List[RecipientDeleteDocumentRecipientIssues]] = None


class RecipientDeleteDocumentRecipientDocumentsRecipientsResponseBody(Exception):
    r"""Invalid input data"""

    data: RecipientDeleteDocumentRecipientDocumentsRecipientsResponseBodyData

    def __init__(
        self, data: RecipientDeleteDocumentRecipientDocumentsRecipientsResponseBodyData
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data,
            RecipientDeleteDocumentRecipientDocumentsRecipientsResponseBodyData,
        )


class RecipientDeleteDocumentRecipientResponseBodyTypedDict(TypedDict):
    r"""Successful response"""

    success: bool


class RecipientDeleteDocumentRecipientResponseBody(BaseModel):
    r"""Successful response"""

    success: bool
