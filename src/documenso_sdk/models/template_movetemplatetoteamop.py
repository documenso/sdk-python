"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from documenso_sdk import utils
from documenso_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, TypedDict


class TemplateMoveTemplateToTeamRequestTypedDict(TypedDict):
    template_id: float
    r"""The ID of the template to move to."""
    team_id: float
    r"""The ID of the team to move the template to."""


class TemplateMoveTemplateToTeamRequest(BaseModel):
    template_id: Annotated[float, pydantic.Field(alias="templateId")]
    r"""The ID of the template to move to."""

    team_id: Annotated[float, pydantic.Field(alias="teamId")]
    r"""The ID of the team to move the template to."""


class TemplateMoveTemplateToTeamInternalServerErrorIssueTypedDict(TypedDict):
    message: str


class TemplateMoveTemplateToTeamInternalServerErrorIssue(BaseModel):
    message: str


class TemplateMoveTemplateToTeamInternalServerErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[TemplateMoveTemplateToTeamInternalServerErrorIssue]] = None


class TemplateMoveTemplateToTeamInternalServerError(Exception):
    r"""Internal server error"""

    data: TemplateMoveTemplateToTeamInternalServerErrorData

    def __init__(self, data: TemplateMoveTemplateToTeamInternalServerErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, TemplateMoveTemplateToTeamInternalServerErrorData
        )


class TemplateMoveTemplateToTeamBadRequestIssueTypedDict(TypedDict):
    message: str


class TemplateMoveTemplateToTeamBadRequestIssue(BaseModel):
    message: str


class TemplateMoveTemplateToTeamBadRequestErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[TemplateMoveTemplateToTeamBadRequestIssue]] = None


class TemplateMoveTemplateToTeamBadRequestError(Exception):
    r"""Invalid input data"""

    data: TemplateMoveTemplateToTeamBadRequestErrorData

    def __init__(self, data: TemplateMoveTemplateToTeamBadRequestErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, TemplateMoveTemplateToTeamBadRequestErrorData
        )


class TemplateMoveTemplateToTeamType(str, Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class TemplateMoveTemplateToTeamVisibility(str, Enum):
    EVERYONE = "EVERYONE"
    MANAGER_AND_ABOVE = "MANAGER_AND_ABOVE"
    ADMIN = "ADMIN"


class TemplateMoveTemplateToTeamGlobalAccessAuth(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class TemplateMoveTemplateToTeamGlobalActionAuth(str, Enum):
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"


class TemplateMoveTemplateToTeamAuthOptionsTypedDict(TypedDict):
    global_access_auth: Nullable[TemplateMoveTemplateToTeamGlobalAccessAuth]
    r"""The type of authentication required for the recipient to access the document."""
    global_action_auth: Nullable[TemplateMoveTemplateToTeamGlobalActionAuth]
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""


class TemplateMoveTemplateToTeamAuthOptions(BaseModel):
    global_access_auth: Annotated[
        Nullable[TemplateMoveTemplateToTeamGlobalAccessAuth],
        pydantic.Field(alias="globalAccessAuth"),
    ]
    r"""The type of authentication required for the recipient to access the document."""

    global_action_auth: Annotated[
        Nullable[TemplateMoveTemplateToTeamGlobalActionAuth],
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


class TemplateMoveTemplateToTeamResponseTypedDict(TypedDict):
    r"""Successful response"""

    type: TemplateMoveTemplateToTeamType
    visibility: TemplateMoveTemplateToTeamVisibility
    id: float
    external_id: Nullable[str]
    title: str
    user_id: float
    team_id: Nullable[float]
    auth_options: Nullable[TemplateMoveTemplateToTeamAuthOptionsTypedDict]
    template_document_data_id: str
    created_at: str
    updated_at: str
    public_title: str
    public_description: str


class TemplateMoveTemplateToTeamResponse(BaseModel):
    r"""Successful response"""

    type: TemplateMoveTemplateToTeamType

    visibility: TemplateMoveTemplateToTeamVisibility

    id: float

    external_id: Annotated[Nullable[str], pydantic.Field(alias="externalId")]

    title: str

    user_id: Annotated[float, pydantic.Field(alias="userId")]

    team_id: Annotated[Nullable[float], pydantic.Field(alias="teamId")]

    auth_options: Annotated[
        Nullable[TemplateMoveTemplateToTeamAuthOptions],
        pydantic.Field(alias="authOptions"),
    ]

    template_document_data_id: Annotated[
        str, pydantic.Field(alias="templateDocumentDataId")
    ]

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]

    updated_at: Annotated[str, pydantic.Field(alias="updatedAt")]

    public_title: Annotated[str, pydantic.Field(alias="publicTitle")]

    public_description: Annotated[str, pydantic.Field(alias="publicDescription")]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["externalId", "teamId", "authOptions"]
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
