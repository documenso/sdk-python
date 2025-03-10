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
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RecipientCreateTemplateRecipientRole(str, Enum):
    CC = "CC"
    SIGNER = "SIGNER"
    VIEWER = "VIEWER"
    APPROVER = "APPROVER"


class RecipientCreateTemplateRecipientAccessAuth(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class RecipientCreateTemplateRecipientActionAuth(str, Enum):
    r"""The type of authentication required for the recipient to sign the document."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"
    EXPLICIT_NONE = "EXPLICIT_NONE"


class RecipientCreateTemplateRecipientRecipientTypedDict(TypedDict):
    email: str
    name: str
    role: RecipientCreateTemplateRecipientRole
    signing_order: NotRequired[float]
    access_auth: NotRequired[Nullable[RecipientCreateTemplateRecipientAccessAuth]]
    r"""The type of authentication required for the recipient to access the document."""
    action_auth: NotRequired[Nullable[RecipientCreateTemplateRecipientActionAuth]]
    r"""The type of authentication required for the recipient to sign the document."""


class RecipientCreateTemplateRecipientRecipient(BaseModel):
    email: str

    name: str

    role: RecipientCreateTemplateRecipientRole

    signing_order: Annotated[Optional[float], pydantic.Field(alias="signingOrder")] = (
        None
    )

    access_auth: Annotated[
        OptionalNullable[RecipientCreateTemplateRecipientAccessAuth],
        pydantic.Field(alias="accessAuth"),
    ] = UNSET
    r"""The type of authentication required for the recipient to access the document."""

    action_auth: Annotated[
        OptionalNullable[RecipientCreateTemplateRecipientActionAuth],
        pydantic.Field(alias="actionAuth"),
    ] = UNSET
    r"""The type of authentication required for the recipient to sign the document."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["signingOrder", "accessAuth", "actionAuth"]
        nullable_fields = ["accessAuth", "actionAuth"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class RecipientCreateTemplateRecipientRequestBodyTypedDict(TypedDict):
    template_id: float
    recipient: RecipientCreateTemplateRecipientRecipientTypedDict


class RecipientCreateTemplateRecipientRequestBody(BaseModel):
    template_id: Annotated[float, pydantic.Field(alias="templateId")]

    recipient: RecipientCreateTemplateRecipientRecipient


class RecipientCreateTemplateRecipientTemplatesRecipientsIssuesTypedDict(TypedDict):
    message: str


class RecipientCreateTemplateRecipientTemplatesRecipientsIssues(BaseModel):
    message: str


class RecipientCreateTemplateRecipientTemplatesRecipientsResponseResponseBodyData(
    BaseModel
):
    message: str

    code: str

    issues: Optional[
        List[RecipientCreateTemplateRecipientTemplatesRecipientsIssues]
    ] = None


class RecipientCreateTemplateRecipientTemplatesRecipientsResponseResponseBody(
    Exception
):
    r"""Internal server error"""

    data: RecipientCreateTemplateRecipientTemplatesRecipientsResponseResponseBodyData

    def __init__(
        self,
        data: RecipientCreateTemplateRecipientTemplatesRecipientsResponseResponseBodyData,
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data,
            RecipientCreateTemplateRecipientTemplatesRecipientsResponseResponseBodyData,
        )


class RecipientCreateTemplateRecipientIssuesTypedDict(TypedDict):
    message: str


class RecipientCreateTemplateRecipientIssues(BaseModel):
    message: str


class RecipientCreateTemplateRecipientTemplatesRecipientsResponseBodyData(BaseModel):
    message: str

    code: str

    issues: Optional[List[RecipientCreateTemplateRecipientIssues]] = None


class RecipientCreateTemplateRecipientTemplatesRecipientsResponseBody(Exception):
    r"""Invalid input data"""

    data: RecipientCreateTemplateRecipientTemplatesRecipientsResponseBodyData

    def __init__(
        self, data: RecipientCreateTemplateRecipientTemplatesRecipientsResponseBodyData
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data,
            RecipientCreateTemplateRecipientTemplatesRecipientsResponseBodyData,
        )


class RecipientCreateTemplateRecipientTemplatesRecipientsRole(str, Enum):
    CC = "CC"
    SIGNER = "SIGNER"
    VIEWER = "VIEWER"
    APPROVER = "APPROVER"


class RecipientCreateTemplateRecipientReadStatus(str, Enum):
    NOT_OPENED = "NOT_OPENED"
    OPENED = "OPENED"


class RecipientCreateTemplateRecipientSigningStatus(str, Enum):
    NOT_SIGNED = "NOT_SIGNED"
    SIGNED = "SIGNED"
    REJECTED = "REJECTED"


class RecipientCreateTemplateRecipientSendStatus(str, Enum):
    NOT_SENT = "NOT_SENT"
    SENT = "SENT"


class RecipientCreateTemplateRecipientTemplatesRecipientsAccessAuth(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class RecipientCreateTemplateRecipientTemplatesRecipientsActionAuth(str, Enum):
    r"""The type of authentication required for the recipient to sign the document."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"
    EXPLICIT_NONE = "EXPLICIT_NONE"


class RecipientCreateTemplateRecipientAuthOptionsTypedDict(TypedDict):
    access_auth: Nullable[RecipientCreateTemplateRecipientTemplatesRecipientsAccessAuth]
    r"""The type of authentication required for the recipient to access the document."""
    action_auth: Nullable[RecipientCreateTemplateRecipientTemplatesRecipientsActionAuth]
    r"""The type of authentication required for the recipient to sign the document."""


class RecipientCreateTemplateRecipientAuthOptions(BaseModel):
    access_auth: Annotated[
        Nullable[RecipientCreateTemplateRecipientTemplatesRecipientsAccessAuth],
        pydantic.Field(alias="accessAuth"),
    ]
    r"""The type of authentication required for the recipient to access the document."""

    action_auth: Annotated[
        Nullable[RecipientCreateTemplateRecipientTemplatesRecipientsActionAuth],
        pydantic.Field(alias="actionAuth"),
    ]
    r"""The type of authentication required for the recipient to sign the document."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["accessAuth", "actionAuth"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class RecipientCreateTemplateRecipientResponseBodyTypedDict(TypedDict):
    r"""Successful response"""

    role: RecipientCreateTemplateRecipientTemplatesRecipientsRole
    read_status: RecipientCreateTemplateRecipientReadStatus
    signing_status: RecipientCreateTemplateRecipientSigningStatus
    send_status: RecipientCreateTemplateRecipientSendStatus
    id: int
    document_id: Nullable[int]
    template_id: Nullable[int]
    email: str
    name: str
    token: str
    document_deleted_at: Nullable[str]
    expired: Nullable[str]
    signed_at: Nullable[str]
    auth_options: Nullable[RecipientCreateTemplateRecipientAuthOptionsTypedDict]
    signing_order: Nullable[float]
    r"""The order in which the recipient should sign the document. Only works if the document is set to sequential signing."""
    rejection_reason: Nullable[str]


class RecipientCreateTemplateRecipientResponseBody(BaseModel):
    r"""Successful response"""

    role: RecipientCreateTemplateRecipientTemplatesRecipientsRole

    read_status: Annotated[
        RecipientCreateTemplateRecipientReadStatus, pydantic.Field(alias="readStatus")
    ]

    signing_status: Annotated[
        RecipientCreateTemplateRecipientSigningStatus,
        pydantic.Field(alias="signingStatus"),
    ]

    send_status: Annotated[
        RecipientCreateTemplateRecipientSendStatus, pydantic.Field(alias="sendStatus")
    ]

    id: int

    document_id: Annotated[Nullable[int], pydantic.Field(alias="documentId")]

    template_id: Annotated[Nullable[int], pydantic.Field(alias="templateId")]

    email: str

    name: str

    token: str

    document_deleted_at: Annotated[
        Nullable[str], pydantic.Field(alias="documentDeletedAt")
    ]

    expired: Nullable[str]

    signed_at: Annotated[Nullable[str], pydantic.Field(alias="signedAt")]

    auth_options: Annotated[
        Nullable[RecipientCreateTemplateRecipientAuthOptions],
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

        for n, f in self.model_fields.items():
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
