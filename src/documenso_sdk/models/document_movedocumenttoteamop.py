"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from documenso_sdk import utils
from documenso_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class DocumentMoveDocumentToTeamRequestTypedDict(TypedDict):
    document_id: float
    r"""The ID of the document to move to a team."""
    team_id: float
    r"""The ID of the team to move the document to."""


class DocumentMoveDocumentToTeamRequest(BaseModel):
    document_id: Annotated[float, pydantic.Field(alias="documentId")]
    r"""The ID of the document to move to a team."""

    team_id: Annotated[float, pydantic.Field(alias="teamId")]
    r"""The ID of the team to move the document to."""


class DocumentMoveDocumentToTeamInternalServerErrorIssueTypedDict(TypedDict):
    message: str


class DocumentMoveDocumentToTeamInternalServerErrorIssue(BaseModel):
    message: str


class DocumentMoveDocumentToTeamInternalServerErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[DocumentMoveDocumentToTeamInternalServerErrorIssue]] = None


class DocumentMoveDocumentToTeamInternalServerError(Exception):
    r"""Internal server error"""

    data: DocumentMoveDocumentToTeamInternalServerErrorData

    def __init__(self, data: DocumentMoveDocumentToTeamInternalServerErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, DocumentMoveDocumentToTeamInternalServerErrorData
        )


class DocumentMoveDocumentToTeamBadRequestIssueTypedDict(TypedDict):
    message: str


class DocumentMoveDocumentToTeamBadRequestIssue(BaseModel):
    message: str


class DocumentMoveDocumentToTeamBadRequestErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[DocumentMoveDocumentToTeamBadRequestIssue]] = None


class DocumentMoveDocumentToTeamBadRequestError(Exception):
    r"""Invalid input data"""

    data: DocumentMoveDocumentToTeamBadRequestErrorData

    def __init__(self, data: DocumentMoveDocumentToTeamBadRequestErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, DocumentMoveDocumentToTeamBadRequestErrorData
        )


class DocumentMoveDocumentToTeamVisibility(str, Enum):
    EVERYONE = "EVERYONE"
    MANAGER_AND_ABOVE = "MANAGER_AND_ABOVE"
    ADMIN = "ADMIN"


class DocumentMoveDocumentToTeamStatus(str, Enum):
    DRAFT = "DRAFT"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


class DocumentMoveDocumentToTeamSource(str, Enum):
    DOCUMENT = "DOCUMENT"
    TEMPLATE = "TEMPLATE"
    TEMPLATE_DIRECT_LINK = "TEMPLATE_DIRECT_LINK"


class DocumentMoveDocumentToTeamGlobalAccessAuth(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class DocumentMoveDocumentToTeamGlobalActionAuth(str, Enum):
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"


class DocumentMoveDocumentToTeamAuthOptionsTypedDict(TypedDict):
    global_access_auth: Nullable[DocumentMoveDocumentToTeamGlobalAccessAuth]
    r"""The type of authentication required for the recipient to access the document."""
    global_action_auth: Nullable[DocumentMoveDocumentToTeamGlobalActionAuth]
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""


class DocumentMoveDocumentToTeamAuthOptions(BaseModel):
    global_access_auth: Annotated[
        Nullable[DocumentMoveDocumentToTeamGlobalAccessAuth],
        pydantic.Field(alias="globalAccessAuth"),
    ]
    r"""The type of authentication required for the recipient to access the document."""

    global_action_auth: Annotated[
        Nullable[DocumentMoveDocumentToTeamGlobalActionAuth],
        pydantic.Field(alias="globalActionAuth"),
    ]
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["globalAccessAuth", "globalActionAuth"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


DocumentMoveDocumentToTeamFormValuesTypedDict = TypeAliasType(
    "DocumentMoveDocumentToTeamFormValuesTypedDict", Union[str, bool, float]
)


DocumentMoveDocumentToTeamFormValues = TypeAliasType(
    "DocumentMoveDocumentToTeamFormValues", Union[str, bool, float]
)


class DocumentMoveDocumentToTeamResponseTypedDict(TypedDict):
    r"""Successful response"""

    visibility: DocumentMoveDocumentToTeamVisibility
    status: DocumentMoveDocumentToTeamStatus
    source: DocumentMoveDocumentToTeamSource
    id: float
    external_id: Nullable[str]
    r"""A custom external ID you can use to identify the document."""
    user_id: float
    r"""The ID of the user that created this document."""
    auth_options: Nullable[DocumentMoveDocumentToTeamAuthOptionsTypedDict]
    form_values: Nullable[Dict[str, DocumentMoveDocumentToTeamFormValuesTypedDict]]
    title: str
    document_data_id: str
    created_at: str
    updated_at: str
    completed_at: Nullable[str]
    deleted_at: Nullable[str]
    team_id: Nullable[float]
    template_id: Nullable[float]


class DocumentMoveDocumentToTeamResponse(BaseModel):
    r"""Successful response"""

    visibility: DocumentMoveDocumentToTeamVisibility

    status: DocumentMoveDocumentToTeamStatus

    source: DocumentMoveDocumentToTeamSource

    id: float

    external_id: Annotated[Nullable[str], pydantic.Field(alias="externalId")]
    r"""A custom external ID you can use to identify the document."""

    user_id: Annotated[float, pydantic.Field(alias="userId")]
    r"""The ID of the user that created this document."""

    auth_options: Annotated[
        Nullable[DocumentMoveDocumentToTeamAuthOptions],
        pydantic.Field(alias="authOptions"),
    ]

    form_values: Annotated[
        Nullable[Dict[str, DocumentMoveDocumentToTeamFormValues]],
        pydantic.Field(alias="formValues"),
    ]

    title: str

    document_data_id: Annotated[str, pydantic.Field(alias="documentDataId")]

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]

    updated_at: Annotated[str, pydantic.Field(alias="updatedAt")]

    completed_at: Annotated[Nullable[str], pydantic.Field(alias="completedAt")]

    deleted_at: Annotated[Nullable[str], pydantic.Field(alias="deletedAt")]

    team_id: Annotated[Nullable[float], pydantic.Field(alias="teamId")]

    template_id: Annotated[Nullable[float], pydantic.Field(alias="templateId")]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "externalId",
            "authOptions",
            "formValues",
            "completedAt",
            "deletedAt",
            "teamId",
            "templateId",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
