"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from documenso_sdk import utils
from documenso_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from documenso_sdk.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class QueryParamSource(str, Enum):
    r"""Filter documents by how it was created."""

    DOCUMENT = "DOCUMENT"
    TEMPLATE = "TEMPLATE"
    TEMPLATE_DIRECT_LINK = "TEMPLATE_DIRECT_LINK"


class QueryParamStatus(str, Enum):
    r"""Filter documents by the current status"""

    DRAFT = "DRAFT"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


class OrderByColumn(str, Enum):
    CREATED_AT = "createdAt"


class OrderByDirection(str, Enum):
    ASC = "asc"
    DESC = "desc"


class DocumentFindDocumentsRequestTypedDict(TypedDict):
    query: NotRequired[str]
    r"""The search query."""
    page: NotRequired[float]
    r"""The pagination page number, starts at 1."""
    per_page: NotRequired[float]
    r"""The number of items per page."""
    template_id: NotRequired[float]
    r"""Filter documents by the template ID used to create it."""
    source: NotRequired[QueryParamSource]
    r"""Filter documents by how it was created."""
    status: NotRequired[QueryParamStatus]
    r"""Filter documents by the current status"""
    order_by_column: NotRequired[OrderByColumn]
    order_by_direction: NotRequired[OrderByDirection]


class DocumentFindDocumentsRequest(BaseModel):
    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The search query."""

    page: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The pagination page number, starts at 1."""

    per_page: Annotated[
        Optional[float],
        pydantic.Field(alias="perPage"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The number of items per page."""

    template_id: Annotated[
        Optional[float],
        pydantic.Field(alias="templateId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter documents by the template ID used to create it."""

    source: Annotated[
        Optional[QueryParamSource],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter documents by how it was created."""

    status: Annotated[
        Optional[QueryParamStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter documents by the current status"""

    order_by_column: Annotated[
        Optional[OrderByColumn],
        pydantic.Field(alias="orderByColumn"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    order_by_direction: Annotated[
        Optional[OrderByDirection],
        pydantic.Field(alias="orderByDirection"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = OrderByDirection.DESC


class DocumentFindDocumentsInternalServerErrorIssueTypedDict(TypedDict):
    message: str


class DocumentFindDocumentsInternalServerErrorIssue(BaseModel):
    message: str


class DocumentFindDocumentsInternalServerErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[DocumentFindDocumentsInternalServerErrorIssue]] = None


class DocumentFindDocumentsInternalServerError(Exception):
    r"""Internal server error"""

    data: DocumentFindDocumentsInternalServerErrorData

    def __init__(self, data: DocumentFindDocumentsInternalServerErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, DocumentFindDocumentsInternalServerErrorData
        )


class DocumentFindDocumentsNotFoundIssueTypedDict(TypedDict):
    message: str


class DocumentFindDocumentsNotFoundIssue(BaseModel):
    message: str


class DocumentFindDocumentsNotFoundErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[DocumentFindDocumentsNotFoundIssue]] = None


class DocumentFindDocumentsNotFoundError(Exception):
    r"""Not found"""

    data: DocumentFindDocumentsNotFoundErrorData

    def __init__(self, data: DocumentFindDocumentsNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, DocumentFindDocumentsNotFoundErrorData)


class DocumentFindDocumentsBadRequestIssueTypedDict(TypedDict):
    message: str


class DocumentFindDocumentsBadRequestIssue(BaseModel):
    message: str


class DocumentFindDocumentsBadRequestErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[DocumentFindDocumentsBadRequestIssue]] = None


class DocumentFindDocumentsBadRequestError(Exception):
    r"""Invalid input data"""

    data: DocumentFindDocumentsBadRequestErrorData

    def __init__(self, data: DocumentFindDocumentsBadRequestErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, DocumentFindDocumentsBadRequestErrorData)


class DocumentFindDocumentsVisibility(str, Enum):
    EVERYONE = "EVERYONE"
    MANAGER_AND_ABOVE = "MANAGER_AND_ABOVE"
    ADMIN = "ADMIN"


class DataStatus(str, Enum):
    DRAFT = "DRAFT"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


class DataSource(str, Enum):
    DOCUMENT = "DOCUMENT"
    TEMPLATE = "TEMPLATE"
    TEMPLATE_DIRECT_LINK = "TEMPLATE_DIRECT_LINK"


class DocumentFindDocumentsGlobalAccessAuth(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class DocumentFindDocumentsGlobalActionAuth(str, Enum):
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"


class DocumentFindDocumentsAuthOptionsTypedDict(TypedDict):
    global_access_auth: Nullable[DocumentFindDocumentsGlobalAccessAuth]
    r"""The type of authentication required for the recipient to access the document."""
    global_action_auth: Nullable[DocumentFindDocumentsGlobalActionAuth]
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""


class DocumentFindDocumentsAuthOptions(BaseModel):
    global_access_auth: Annotated[
        Nullable[DocumentFindDocumentsGlobalAccessAuth],
        pydantic.Field(alias="globalAccessAuth"),
    ]
    r"""The type of authentication required for the recipient to access the document."""

    global_action_auth: Annotated[
        Nullable[DocumentFindDocumentsGlobalActionAuth],
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


DocumentFindDocumentsFormValuesTypedDict = TypeAliasType(
    "DocumentFindDocumentsFormValuesTypedDict", Union[str, bool, float]
)


DocumentFindDocumentsFormValues = TypeAliasType(
    "DocumentFindDocumentsFormValues", Union[str, bool, float]
)


class DocumentFindDocumentsUserTypedDict(TypedDict):
    id: float
    name: Nullable[str]
    email: str


class DocumentFindDocumentsUser(BaseModel):
    id: float

    name: Nullable[str]

    email: str

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["name"]
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


class DocumentFindDocumentsRole(str, Enum):
    CC = "CC"
    SIGNER = "SIGNER"
    VIEWER = "VIEWER"
    APPROVER = "APPROVER"
    ASSISTANT = "ASSISTANT"


class DocumentFindDocumentsReadStatus(str, Enum):
    NOT_OPENED = "NOT_OPENED"
    OPENED = "OPENED"


class DocumentFindDocumentsSigningStatus(str, Enum):
    NOT_SIGNED = "NOT_SIGNED"
    SIGNED = "SIGNED"
    REJECTED = "REJECTED"


class DocumentFindDocumentsSendStatus(str, Enum):
    NOT_SENT = "NOT_SENT"
    SENT = "SENT"


class DocumentFindDocumentsAccessAuth(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class DocumentFindDocumentsActionAuth(str, Enum):
    r"""The type of authentication required for the recipient to sign the document."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"
    EXPLICIT_NONE = "EXPLICIT_NONE"


class DocumentFindDocumentsRecipientAuthOptionsTypedDict(TypedDict):
    access_auth: Nullable[DocumentFindDocumentsAccessAuth]
    r"""The type of authentication required for the recipient to access the document."""
    action_auth: Nullable[DocumentFindDocumentsActionAuth]
    r"""The type of authentication required for the recipient to sign the document."""


class DocumentFindDocumentsRecipientAuthOptions(BaseModel):
    access_auth: Annotated[
        Nullable[DocumentFindDocumentsAccessAuth], pydantic.Field(alias="accessAuth")
    ]
    r"""The type of authentication required for the recipient to access the document."""

    action_auth: Annotated[
        Nullable[DocumentFindDocumentsActionAuth], pydantic.Field(alias="actionAuth")
    ]
    r"""The type of authentication required for the recipient to sign the document."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["accessAuth", "actionAuth"]
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


class DocumentFindDocumentsRecipientTypedDict(TypedDict):
    role: DocumentFindDocumentsRole
    read_status: DocumentFindDocumentsReadStatus
    signing_status: DocumentFindDocumentsSigningStatus
    send_status: DocumentFindDocumentsSendStatus
    id: float
    document_id: Nullable[float]
    template_id: Nullable[float]
    email: str
    name: str
    token: str
    document_deleted_at: Nullable[str]
    expired: Nullable[str]
    signed_at: Nullable[str]
    auth_options: Nullable[DocumentFindDocumentsRecipientAuthOptionsTypedDict]
    signing_order: Nullable[float]
    r"""The order in which the recipient should sign the document. Only works if the document is set to sequential signing."""
    rejection_reason: Nullable[str]


class DocumentFindDocumentsRecipient(BaseModel):
    role: DocumentFindDocumentsRole

    read_status: Annotated[
        DocumentFindDocumentsReadStatus, pydantic.Field(alias="readStatus")
    ]

    signing_status: Annotated[
        DocumentFindDocumentsSigningStatus, pydantic.Field(alias="signingStatus")
    ]

    send_status: Annotated[
        DocumentFindDocumentsSendStatus, pydantic.Field(alias="sendStatus")
    ]

    id: float

    document_id: Annotated[Nullable[float], pydantic.Field(alias="documentId")]

    template_id: Annotated[Nullable[float], pydantic.Field(alias="templateId")]

    email: str

    name: str

    token: str

    document_deleted_at: Annotated[
        Nullable[str], pydantic.Field(alias="documentDeletedAt")
    ]

    expired: Nullable[str]

    signed_at: Annotated[Nullable[str], pydantic.Field(alias="signedAt")]

    auth_options: Annotated[
        Nullable[DocumentFindDocumentsRecipientAuthOptions],
        pydantic.Field(alias="authOptions"),
    ]

    signing_order: Annotated[Nullable[float], pydantic.Field(alias="signingOrder")]
    r"""The order in which the recipient should sign the document. Only works if the document is set to sequential signing."""

    rejection_reason: Annotated[Nullable[str], pydantic.Field(alias="rejectionReason")]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "documentId",
            "templateId",
            "documentDeletedAt",
            "expired",
            "signedAt",
            "authOptions",
            "signingOrder",
            "rejectionReason",
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


class DocumentFindDocumentsTeamTypedDict(TypedDict):
    id: float
    url: str


class DocumentFindDocumentsTeam(BaseModel):
    id: float

    url: str


class DocumentFindDocumentsDataTypedDict(TypedDict):
    visibility: DocumentFindDocumentsVisibility
    status: DataStatus
    source: DataSource
    id: float
    external_id: Nullable[str]
    r"""A custom external ID you can use to identify the document."""
    user_id: float
    r"""The ID of the user that created this document."""
    auth_options: Nullable[DocumentFindDocumentsAuthOptionsTypedDict]
    form_values: Nullable[Dict[str, DocumentFindDocumentsFormValuesTypedDict]]
    title: str
    document_data_id: str
    created_at: str
    updated_at: str
    completed_at: Nullable[str]
    deleted_at: Nullable[str]
    team_id: Nullable[float]
    template_id: Nullable[float]
    user: DocumentFindDocumentsUserTypedDict
    recipients: List[DocumentFindDocumentsRecipientTypedDict]
    team: Nullable[DocumentFindDocumentsTeamTypedDict]


class DocumentFindDocumentsData(BaseModel):
    visibility: DocumentFindDocumentsVisibility

    status: DataStatus

    source: DataSource

    id: float

    external_id: Annotated[Nullable[str], pydantic.Field(alias="externalId")]
    r"""A custom external ID you can use to identify the document."""

    user_id: Annotated[float, pydantic.Field(alias="userId")]
    r"""The ID of the user that created this document."""

    auth_options: Annotated[
        Nullable[DocumentFindDocumentsAuthOptions], pydantic.Field(alias="authOptions")
    ]

    form_values: Annotated[
        Nullable[Dict[str, DocumentFindDocumentsFormValues]],
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

    user: DocumentFindDocumentsUser

    recipients: List[DocumentFindDocumentsRecipient]

    team: Nullable[DocumentFindDocumentsTeam]

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
            "team",
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


class DocumentFindDocumentsResponseTypedDict(TypedDict):
    r"""Successful response"""

    data: List[DocumentFindDocumentsDataTypedDict]
    count: float
    r"""The total number of items."""
    current_page: float
    r"""The current page number, starts at 1."""
    per_page: float
    r"""The number of items per page."""
    total_pages: float
    r"""The total number of pages."""


class DocumentFindDocumentsResponse(BaseModel):
    r"""Successful response"""

    data: List[DocumentFindDocumentsData]

    count: float
    r"""The total number of items."""

    current_page: Annotated[float, pydantic.Field(alias="currentPage")]
    r"""The current page number, starts at 1."""

    per_page: Annotated[float, pydantic.Field(alias="perPage")]
    r"""The number of items per page."""

    total_pages: Annotated[float, pydantic.Field(alias="totalPages")]
    r"""The total number of pages."""
