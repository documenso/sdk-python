"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from documenso_sdk import utils
from documenso_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class DocumentUpdateDocumentVisibilityRequestBody(str, Enum):
    r"""The visibility of the document."""

    EVERYONE = "EVERYONE"
    MANAGER_AND_ABOVE = "MANAGER_AND_ABOVE"
    ADMIN = "ADMIN"


class DocumentUpdateDocumentGlobalAccessAuthRequestBody(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class DocumentUpdateDocumentGlobalActionAuthRequestBody(str, Enum):
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"


class DocumentUpdateDocumentDataTypedDict(TypedDict):
    title: NotRequired[str]
    r"""The title of the document."""
    external_id: NotRequired[Nullable[str]]
    r"""The external ID of the document."""
    visibility: NotRequired[DocumentUpdateDocumentVisibilityRequestBody]
    r"""The visibility of the document."""
    global_access_auth: NotRequired[
        Nullable[DocumentUpdateDocumentGlobalAccessAuthRequestBody]
    ]
    r"""The type of authentication required for the recipient to access the document."""
    global_action_auth: NotRequired[
        Nullable[DocumentUpdateDocumentGlobalActionAuthRequestBody]
    ]
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""


class DocumentUpdateDocumentData(BaseModel):
    title: Optional[str] = None
    r"""The title of the document."""

    external_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="externalId")
    ] = UNSET
    r"""The external ID of the document."""

    visibility: Optional[DocumentUpdateDocumentVisibilityRequestBody] = None
    r"""The visibility of the document."""

    global_access_auth: Annotated[
        OptionalNullable[DocumentUpdateDocumentGlobalAccessAuthRequestBody],
        pydantic.Field(alias="globalAccessAuth"),
    ] = UNSET
    r"""The type of authentication required for the recipient to access the document."""

    global_action_auth: Annotated[
        OptionalNullable[DocumentUpdateDocumentGlobalActionAuthRequestBody],
        pydantic.Field(alias="globalActionAuth"),
    ] = UNSET
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "title",
            "externalId",
            "visibility",
            "globalAccessAuth",
            "globalActionAuth",
        ]
        nullable_fields = ["externalId", "globalAccessAuth", "globalActionAuth"]
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


class DocumentUpdateDocumentDateFormat(str, Enum):
    r"""The date format to use for date fields and signing the document."""

    YYYY_MM_DD_HH_MM_A = "yyyy-MM-dd hh:mm a"
    YYYY_MM_DD = "yyyy-MM-dd"
    DD_MM_YYYY_HH_MM_A = "dd/MM/yyyy hh:mm a"
    MM_DD_YYYY_HH_MM_A = "MM/dd/yyyy hh:mm a"
    YYYY_MM_DD_HH_MM = "yyyy-MM-dd HH:mm"
    YY_MM_DD_HH_MM_A = "yy-MM-dd hh:mm a"
    YYYY_MM_DD_HH_MM_SS = "yyyy-MM-dd HH:mm:ss"
    MMMM_DD_YYYY_HH_MM_A = "MMMM dd, yyyy hh:mm a"
    EEEE_MMMM_DD_YYYY_HH_MM_A = "EEEE, MMMM dd, yyyy hh:mm a"
    YYYY_MM_DD_T_HH_MM_SS_SSSXXX = "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"


class DocumentUpdateDocumentDistributionMethod(str, Enum):
    r"""The distribution method to use when sending the document to the recipients."""

    EMAIL = "EMAIL"
    NONE = "NONE"


class DocumentUpdateDocumentSigningOrder(str, Enum):
    PARALLEL = "PARALLEL"
    SEQUENTIAL = "SEQUENTIAL"


class DocumentUpdateDocumentLanguage(str, Enum):
    r"""The language to use for email communications with recipients."""

    DE = "de"
    EN = "en"
    FR = "fr"
    ES = "es"
    IT = "it"
    PL = "pl"


class DocumentUpdateDocumentEmailSettingsTypedDict(TypedDict):
    recipient_signing_request: NotRequired[bool]
    r"""Whether to send an email to all recipients that the document is ready for them to sign."""
    recipient_removed: NotRequired[bool]
    r"""Whether to send an email to the recipient who was removed from a pending document."""
    recipient_signed: NotRequired[bool]
    r"""Whether to send an email to the document owner when a recipient has signed the document."""
    document_pending: NotRequired[bool]
    r"""Whether to send an email to the recipient who has just signed the document indicating that there are still other recipients who need to sign the document. This will only be sent if the document is still pending after the recipient has signed."""
    document_completed: NotRequired[bool]
    r"""Whether to send an email to all recipients when the document is complete."""
    document_deleted: NotRequired[bool]
    r"""Whether to send an email to all recipients if a pending document has been deleted."""
    owner_document_completed: NotRequired[bool]
    r"""Whether to send an email to the document owner when the document is complete."""


class DocumentUpdateDocumentEmailSettings(BaseModel):
    recipient_signing_request: Annotated[
        Optional[bool], pydantic.Field(alias="recipientSigningRequest")
    ] = True
    r"""Whether to send an email to all recipients that the document is ready for them to sign."""

    recipient_removed: Annotated[
        Optional[bool], pydantic.Field(alias="recipientRemoved")
    ] = True
    r"""Whether to send an email to the recipient who was removed from a pending document."""

    recipient_signed: Annotated[
        Optional[bool], pydantic.Field(alias="recipientSigned")
    ] = True
    r"""Whether to send an email to the document owner when a recipient has signed the document."""

    document_pending: Annotated[
        Optional[bool], pydantic.Field(alias="documentPending")
    ] = True
    r"""Whether to send an email to the recipient who has just signed the document indicating that there are still other recipients who need to sign the document. This will only be sent if the document is still pending after the recipient has signed."""

    document_completed: Annotated[
        Optional[bool], pydantic.Field(alias="documentCompleted")
    ] = True
    r"""Whether to send an email to all recipients when the document is complete."""

    document_deleted: Annotated[
        Optional[bool], pydantic.Field(alias="documentDeleted")
    ] = True
    r"""Whether to send an email to all recipients if a pending document has been deleted."""

    owner_document_completed: Annotated[
        Optional[bool], pydantic.Field(alias="ownerDocumentCompleted")
    ] = True
    r"""Whether to send an email to the document owner when the document is complete."""


class DocumentUpdateDocumentMetaTypedDict(TypedDict):
    subject: NotRequired[str]
    r"""The subject of the email that will be sent to the recipients."""
    message: NotRequired[str]
    r"""The message of the email that will be sent to the recipients."""
    timezone: NotRequired[str]
    r"""The timezone to use for date fields and signing the document. Example Etc/UTC, Australia/Melbourne"""
    date_format: NotRequired[DocumentUpdateDocumentDateFormat]
    r"""The date format to use for date fields and signing the document."""
    distribution_method: NotRequired[DocumentUpdateDocumentDistributionMethod]
    r"""The distribution method to use when sending the document to the recipients."""
    signing_order: NotRequired[DocumentUpdateDocumentSigningOrder]
    allow_dictate_next_signer: NotRequired[bool]
    redirect_url: NotRequired[str]
    r"""The URL to which the recipient should be redirected after signing the document."""
    language: NotRequired[DocumentUpdateDocumentLanguage]
    r"""The language to use for email communications with recipients."""
    typed_signature_enabled: NotRequired[bool]
    r"""Whether to allow recipients to sign using a typed signature."""
    upload_signature_enabled: NotRequired[bool]
    r"""Whether to allow recipients to sign using an uploaded signature."""
    draw_signature_enabled: NotRequired[bool]
    r"""Whether to allow recipients to sign using a draw signature."""
    email_settings: NotRequired[DocumentUpdateDocumentEmailSettingsTypedDict]


class DocumentUpdateDocumentMeta(BaseModel):
    subject: Optional[str] = None
    r"""The subject of the email that will be sent to the recipients."""

    message: Optional[str] = None
    r"""The message of the email that will be sent to the recipients."""

    timezone: Optional[str] = None
    r"""The timezone to use for date fields and signing the document. Example Etc/UTC, Australia/Melbourne"""

    date_format: Annotated[
        Optional[DocumentUpdateDocumentDateFormat], pydantic.Field(alias="dateFormat")
    ] = None
    r"""The date format to use for date fields and signing the document."""

    distribution_method: Annotated[
        Optional[DocumentUpdateDocumentDistributionMethod],
        pydantic.Field(alias="distributionMethod"),
    ] = None
    r"""The distribution method to use when sending the document to the recipients."""

    signing_order: Annotated[
        Optional[DocumentUpdateDocumentSigningOrder],
        pydantic.Field(alias="signingOrder"),
    ] = None

    allow_dictate_next_signer: Annotated[
        Optional[bool], pydantic.Field(alias="allowDictateNextSigner")
    ] = None

    redirect_url: Annotated[Optional[str], pydantic.Field(alias="redirectUrl")] = None
    r"""The URL to which the recipient should be redirected after signing the document."""

    language: Optional[DocumentUpdateDocumentLanguage] = None
    r"""The language to use for email communications with recipients."""

    typed_signature_enabled: Annotated[
        Optional[bool], pydantic.Field(alias="typedSignatureEnabled")
    ] = None
    r"""Whether to allow recipients to sign using a typed signature."""

    upload_signature_enabled: Annotated[
        Optional[bool], pydantic.Field(alias="uploadSignatureEnabled")
    ] = None
    r"""Whether to allow recipients to sign using an uploaded signature."""

    draw_signature_enabled: Annotated[
        Optional[bool], pydantic.Field(alias="drawSignatureEnabled")
    ] = None
    r"""Whether to allow recipients to sign using a draw signature."""

    email_settings: Annotated[
        Optional[DocumentUpdateDocumentEmailSettings],
        pydantic.Field(alias="emailSettings"),
    ] = None


class DocumentUpdateDocumentRequestTypedDict(TypedDict):
    document_id: float
    data: NotRequired[DocumentUpdateDocumentDataTypedDict]
    meta: NotRequired[DocumentUpdateDocumentMetaTypedDict]


class DocumentUpdateDocumentRequest(BaseModel):
    document_id: Annotated[float, pydantic.Field(alias="documentId")]

    data: Optional[DocumentUpdateDocumentData] = None

    meta: Optional[DocumentUpdateDocumentMeta] = None


class DocumentUpdateDocumentInternalServerErrorIssueTypedDict(TypedDict):
    message: str


class DocumentUpdateDocumentInternalServerErrorIssue(BaseModel):
    message: str


class DocumentUpdateDocumentInternalServerErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[DocumentUpdateDocumentInternalServerErrorIssue]] = None


class DocumentUpdateDocumentInternalServerError(Exception):
    r"""Internal server error"""

    data: DocumentUpdateDocumentInternalServerErrorData

    def __init__(self, data: DocumentUpdateDocumentInternalServerErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, DocumentUpdateDocumentInternalServerErrorData
        )


class DocumentUpdateDocumentBadRequestIssueTypedDict(TypedDict):
    message: str


class DocumentUpdateDocumentBadRequestIssue(BaseModel):
    message: str


class DocumentUpdateDocumentBadRequestErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[DocumentUpdateDocumentBadRequestIssue]] = None


class DocumentUpdateDocumentBadRequestError(Exception):
    r"""Invalid input data"""

    data: DocumentUpdateDocumentBadRequestErrorData

    def __init__(self, data: DocumentUpdateDocumentBadRequestErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, DocumentUpdateDocumentBadRequestErrorData)


class DocumentUpdateDocumentVisibilityResponse(str, Enum):
    EVERYONE = "EVERYONE"
    MANAGER_AND_ABOVE = "MANAGER_AND_ABOVE"
    ADMIN = "ADMIN"


class DocumentUpdateDocumentStatus(str, Enum):
    DRAFT = "DRAFT"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


class DocumentUpdateDocumentSource(str, Enum):
    DOCUMENT = "DOCUMENT"
    TEMPLATE = "TEMPLATE"
    TEMPLATE_DIRECT_LINK = "TEMPLATE_DIRECT_LINK"


class DocumentUpdateDocumentGlobalAccessAuthResponse(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class DocumentUpdateDocumentGlobalActionAuthResponse(str, Enum):
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"


class DocumentUpdateDocumentAuthOptionsTypedDict(TypedDict):
    global_access_auth: Nullable[DocumentUpdateDocumentGlobalAccessAuthResponse]
    r"""The type of authentication required for the recipient to access the document."""
    global_action_auth: Nullable[DocumentUpdateDocumentGlobalActionAuthResponse]
    r"""The type of authentication required for the recipient to sign the document. This field is restricted to Enterprise plan users only."""


class DocumentUpdateDocumentAuthOptions(BaseModel):
    global_access_auth: Annotated[
        Nullable[DocumentUpdateDocumentGlobalAccessAuthResponse],
        pydantic.Field(alias="globalAccessAuth"),
    ]
    r"""The type of authentication required for the recipient to access the document."""

    global_action_auth: Annotated[
        Nullable[DocumentUpdateDocumentGlobalActionAuthResponse],
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


DocumentUpdateDocumentFormValuesTypedDict = TypeAliasType(
    "DocumentUpdateDocumentFormValuesTypedDict", Union[str, bool, float]
)


DocumentUpdateDocumentFormValues = TypeAliasType(
    "DocumentUpdateDocumentFormValues", Union[str, bool, float]
)


class DocumentUpdateDocumentResponseTypedDict(TypedDict):
    r"""Successful response"""

    visibility: DocumentUpdateDocumentVisibilityResponse
    status: DocumentUpdateDocumentStatus
    source: DocumentUpdateDocumentSource
    id: float
    external_id: Nullable[str]
    r"""A custom external ID you can use to identify the document."""
    user_id: float
    r"""The ID of the user that created this document."""
    auth_options: Nullable[DocumentUpdateDocumentAuthOptionsTypedDict]
    form_values: Nullable[Dict[str, DocumentUpdateDocumentFormValuesTypedDict]]
    title: str
    document_data_id: str
    created_at: str
    updated_at: str
    completed_at: Nullable[str]
    deleted_at: Nullable[str]
    team_id: Nullable[float]
    template_id: Nullable[float]


class DocumentUpdateDocumentResponse(BaseModel):
    r"""Successful response"""

    visibility: DocumentUpdateDocumentVisibilityResponse

    status: DocumentUpdateDocumentStatus

    source: DocumentUpdateDocumentSource

    id: float

    external_id: Annotated[Nullable[str], pydantic.Field(alias="externalId")]
    r"""A custom external ID you can use to identify the document."""

    user_id: Annotated[float, pydantic.Field(alias="userId")]
    r"""The ID of the user that created this document."""

    auth_options: Annotated[
        Nullable[DocumentUpdateDocumentAuthOptions], pydantic.Field(alias="authOptions")
    ]

    form_values: Annotated[
        Nullable[Dict[str, DocumentUpdateDocumentFormValues]],
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
