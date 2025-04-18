"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from documenso_sdk import utils
from documenso_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from documenso_sdk.utils import FieldMetadata, PathParamMetadata
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Any, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class RecipientGetDocumentRecipientRequestTypedDict(TypedDict):
    recipient_id: float


class RecipientGetDocumentRecipientRequest(BaseModel):
    recipient_id: Annotated[
        float,
        pydantic.Field(alias="recipientId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]


class RecipientGetDocumentRecipientInternalServerErrorIssueTypedDict(TypedDict):
    message: str


class RecipientGetDocumentRecipientInternalServerErrorIssue(BaseModel):
    message: str


class RecipientGetDocumentRecipientInternalServerErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[RecipientGetDocumentRecipientInternalServerErrorIssue]] = None


class RecipientGetDocumentRecipientInternalServerError(Exception):
    r"""Internal server error"""

    data: RecipientGetDocumentRecipientInternalServerErrorData

    def __init__(self, data: RecipientGetDocumentRecipientInternalServerErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, RecipientGetDocumentRecipientInternalServerErrorData
        )


class RecipientGetDocumentRecipientNotFoundIssueTypedDict(TypedDict):
    message: str


class RecipientGetDocumentRecipientNotFoundIssue(BaseModel):
    message: str


class RecipientGetDocumentRecipientNotFoundErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[RecipientGetDocumentRecipientNotFoundIssue]] = None


class RecipientGetDocumentRecipientNotFoundError(Exception):
    r"""Not found"""

    data: RecipientGetDocumentRecipientNotFoundErrorData

    def __init__(self, data: RecipientGetDocumentRecipientNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, RecipientGetDocumentRecipientNotFoundErrorData
        )


class RecipientGetDocumentRecipientBadRequestIssueTypedDict(TypedDict):
    message: str


class RecipientGetDocumentRecipientBadRequestIssue(BaseModel):
    message: str


class RecipientGetDocumentRecipientBadRequestErrorData(BaseModel):
    message: str

    code: str

    issues: Optional[List[RecipientGetDocumentRecipientBadRequestIssue]] = None


class RecipientGetDocumentRecipientBadRequestError(Exception):
    r"""Invalid input data"""

    data: RecipientGetDocumentRecipientBadRequestErrorData

    def __init__(self, data: RecipientGetDocumentRecipientBadRequestErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, RecipientGetDocumentRecipientBadRequestErrorData
        )


class RecipientGetDocumentRecipientRole(str, Enum):
    CC = "CC"
    SIGNER = "SIGNER"
    VIEWER = "VIEWER"
    APPROVER = "APPROVER"
    ASSISTANT = "ASSISTANT"


class RecipientGetDocumentRecipientReadStatus(str, Enum):
    NOT_OPENED = "NOT_OPENED"
    OPENED = "OPENED"


class RecipientGetDocumentRecipientSigningStatus(str, Enum):
    NOT_SIGNED = "NOT_SIGNED"
    SIGNED = "SIGNED"
    REJECTED = "REJECTED"


class RecipientGetDocumentRecipientSendStatus(str, Enum):
    NOT_SENT = "NOT_SENT"
    SENT = "SENT"


class RecipientGetDocumentRecipientAccessAuth(str, Enum):
    r"""The type of authentication required for the recipient to access the document."""

    ACCOUNT = "ACCOUNT"


class RecipientGetDocumentRecipientActionAuth(str, Enum):
    r"""The type of authentication required for the recipient to sign the document."""

    ACCOUNT = "ACCOUNT"
    PASSKEY = "PASSKEY"
    TWO_FACTOR_AUTH = "TWO_FACTOR_AUTH"
    EXPLICIT_NONE = "EXPLICIT_NONE"


class RecipientGetDocumentRecipientAuthOptionsTypedDict(TypedDict):
    access_auth: Nullable[RecipientGetDocumentRecipientAccessAuth]
    r"""The type of authentication required for the recipient to access the document."""
    action_auth: Nullable[RecipientGetDocumentRecipientActionAuth]
    r"""The type of authentication required for the recipient to sign the document."""


class RecipientGetDocumentRecipientAuthOptions(BaseModel):
    access_auth: Annotated[
        Nullable[RecipientGetDocumentRecipientAccessAuth],
        pydantic.Field(alias="accessAuth"),
    ]
    r"""The type of authentication required for the recipient to access the document."""

    action_auth: Annotated[
        Nullable[RecipientGetDocumentRecipientActionAuth],
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


class RecipientGetDocumentRecipientType(str, Enum):
    SIGNATURE = "SIGNATURE"
    FREE_SIGNATURE = "FREE_SIGNATURE"
    INITIALS = "INITIALS"
    NAME = "NAME"
    EMAIL = "EMAIL"
    DATE = "DATE"
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    RADIO = "RADIO"
    CHECKBOX = "CHECKBOX"
    DROPDOWN = "DROPDOWN"


class RecipientGetDocumentRecipientTypeDropdown(str, Enum):
    DROPDOWN = "dropdown"


class RecipientGetDocumentRecipientValue3TypedDict(TypedDict):
    value: str


class RecipientGetDocumentRecipientValue3(BaseModel):
    value: str


class RecipientGetDocumentRecipientFieldMetaDropdownTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeDropdown
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    values: NotRequired[List[RecipientGetDocumentRecipientValue3TypedDict]]
    default_value: NotRequired[str]


class RecipientGetDocumentRecipientFieldMetaDropdown(BaseModel):
    type: RecipientGetDocumentRecipientTypeDropdown

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    values: Optional[List[RecipientGetDocumentRecipientValue3]] = None

    default_value: Annotated[Optional[str], pydantic.Field(alias="defaultValue")] = None


class RecipientGetDocumentRecipientTypeCheckbox(str, Enum):
    CHECKBOX = "checkbox"


class RecipientGetDocumentRecipientValue2TypedDict(TypedDict):
    id: float
    checked: bool
    value: str


class RecipientGetDocumentRecipientValue2(BaseModel):
    id: float

    checked: bool

    value: str


class RecipientGetDocumentRecipientFieldMetaCheckboxTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeCheckbox
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    values: NotRequired[List[RecipientGetDocumentRecipientValue2TypedDict]]
    validation_rule: NotRequired[str]
    validation_length: NotRequired[float]


class RecipientGetDocumentRecipientFieldMetaCheckbox(BaseModel):
    type: RecipientGetDocumentRecipientTypeCheckbox

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    values: Optional[List[RecipientGetDocumentRecipientValue2]] = None

    validation_rule: Annotated[
        Optional[str], pydantic.Field(alias="validationRule")
    ] = None

    validation_length: Annotated[
        Optional[float], pydantic.Field(alias="validationLength")
    ] = None


class RecipientGetDocumentRecipientTypeRadio(str, Enum):
    RADIO = "radio"


class RecipientGetDocumentRecipientValue1TypedDict(TypedDict):
    id: float
    checked: bool
    value: str


class RecipientGetDocumentRecipientValue1(BaseModel):
    id: float

    checked: bool

    value: str


class RecipientGetDocumentRecipientFieldMetaRadioTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeRadio
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    values: NotRequired[List[RecipientGetDocumentRecipientValue1TypedDict]]


class RecipientGetDocumentRecipientFieldMetaRadio(BaseModel):
    type: RecipientGetDocumentRecipientTypeRadio

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    values: Optional[List[RecipientGetDocumentRecipientValue1]] = None


class RecipientGetDocumentRecipientTypeNumber(str, Enum):
    NUMBER = "number"


class RecipientGetDocumentRecipientTextAlign6(str, Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class RecipientGetDocumentRecipientFieldMetaNumberTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeNumber
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    number_format: NotRequired[str]
    value: NotRequired[str]
    min_value: NotRequired[float]
    max_value: NotRequired[float]
    font_size: NotRequired[float]
    text_align: NotRequired[RecipientGetDocumentRecipientTextAlign6]


class RecipientGetDocumentRecipientFieldMetaNumber(BaseModel):
    type: RecipientGetDocumentRecipientTypeNumber

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    number_format: Annotated[Optional[str], pydantic.Field(alias="numberFormat")] = None

    value: Optional[str] = None

    min_value: Annotated[Optional[float], pydantic.Field(alias="minValue")] = None

    max_value: Annotated[Optional[float], pydantic.Field(alias="maxValue")] = None

    font_size: Annotated[Optional[float], pydantic.Field(alias="fontSize")] = None

    text_align: Annotated[
        Optional[RecipientGetDocumentRecipientTextAlign6],
        pydantic.Field(alias="textAlign"),
    ] = None


class RecipientGetDocumentRecipientTypeText(str, Enum):
    TEXT = "text"


class RecipientGetDocumentRecipientTextAlign5(str, Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class RecipientGetDocumentRecipientFieldMetaTextTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeText
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    text: NotRequired[str]
    character_limit: NotRequired[float]
    font_size: NotRequired[float]
    text_align: NotRequired[RecipientGetDocumentRecipientTextAlign5]


class RecipientGetDocumentRecipientFieldMetaText(BaseModel):
    type: RecipientGetDocumentRecipientTypeText

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    text: Optional[str] = None

    character_limit: Annotated[
        Optional[float], pydantic.Field(alias="characterLimit")
    ] = None

    font_size: Annotated[Optional[float], pydantic.Field(alias="fontSize")] = None

    text_align: Annotated[
        Optional[RecipientGetDocumentRecipientTextAlign5],
        pydantic.Field(alias="textAlign"),
    ] = None


class RecipientGetDocumentRecipientTypeDate(str, Enum):
    DATE = "date"


class RecipientGetDocumentRecipientTextAlign4(str, Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class RecipientGetDocumentRecipientFieldMetaDateTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeDate
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    font_size: NotRequired[float]
    text_align: NotRequired[RecipientGetDocumentRecipientTextAlign4]


class RecipientGetDocumentRecipientFieldMetaDate(BaseModel):
    type: RecipientGetDocumentRecipientTypeDate

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    font_size: Annotated[Optional[float], pydantic.Field(alias="fontSize")] = None

    text_align: Annotated[
        Optional[RecipientGetDocumentRecipientTextAlign4],
        pydantic.Field(alias="textAlign"),
    ] = None


class RecipientGetDocumentRecipientTypeEmail(str, Enum):
    EMAIL = "email"


class RecipientGetDocumentRecipientTextAlign3(str, Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class RecipientGetDocumentRecipientFieldMetaEmailTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeEmail
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    font_size: NotRequired[float]
    text_align: NotRequired[RecipientGetDocumentRecipientTextAlign3]


class RecipientGetDocumentRecipientFieldMetaEmail(BaseModel):
    type: RecipientGetDocumentRecipientTypeEmail

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    font_size: Annotated[Optional[float], pydantic.Field(alias="fontSize")] = None

    text_align: Annotated[
        Optional[RecipientGetDocumentRecipientTextAlign3],
        pydantic.Field(alias="textAlign"),
    ] = None


class RecipientGetDocumentRecipientTypeName(str, Enum):
    NAME = "name"


class RecipientGetDocumentRecipientTextAlign2(str, Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class RecipientGetDocumentRecipientFieldMetaNameTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeName
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    font_size: NotRequired[float]
    text_align: NotRequired[RecipientGetDocumentRecipientTextAlign2]


class RecipientGetDocumentRecipientFieldMetaName(BaseModel):
    type: RecipientGetDocumentRecipientTypeName

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    font_size: Annotated[Optional[float], pydantic.Field(alias="fontSize")] = None

    text_align: Annotated[
        Optional[RecipientGetDocumentRecipientTextAlign2],
        pydantic.Field(alias="textAlign"),
    ] = None


class RecipientGetDocumentRecipientTypeInitials(str, Enum):
    INITIALS = "initials"


class RecipientGetDocumentRecipientTextAlign1(str, Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class RecipientGetDocumentRecipientFieldMetaInitialsTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientTypeInitials
    label: NotRequired[str]
    placeholder: NotRequired[str]
    required: NotRequired[bool]
    read_only: NotRequired[bool]
    font_size: NotRequired[float]
    text_align: NotRequired[RecipientGetDocumentRecipientTextAlign1]


class RecipientGetDocumentRecipientFieldMetaInitials(BaseModel):
    type: RecipientGetDocumentRecipientTypeInitials

    label: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    read_only: Annotated[Optional[bool], pydantic.Field(alias="readOnly")] = None

    font_size: Annotated[Optional[float], pydantic.Field(alias="fontSize")] = None

    text_align: Annotated[
        Optional[RecipientGetDocumentRecipientTextAlign1],
        pydantic.Field(alias="textAlign"),
    ] = None


RecipientGetDocumentRecipientFieldMetaUnionTypedDict = TypeAliasType(
    "RecipientGetDocumentRecipientFieldMetaUnionTypedDict",
    Union[
        RecipientGetDocumentRecipientFieldMetaRadioTypedDict,
        RecipientGetDocumentRecipientFieldMetaInitialsTypedDict,
        RecipientGetDocumentRecipientFieldMetaNameTypedDict,
        RecipientGetDocumentRecipientFieldMetaEmailTypedDict,
        RecipientGetDocumentRecipientFieldMetaDateTypedDict,
        RecipientGetDocumentRecipientFieldMetaDropdownTypedDict,
        RecipientGetDocumentRecipientFieldMetaCheckboxTypedDict,
        RecipientGetDocumentRecipientFieldMetaTextTypedDict,
        RecipientGetDocumentRecipientFieldMetaNumberTypedDict,
    ],
)


RecipientGetDocumentRecipientFieldMetaUnion = TypeAliasType(
    "RecipientGetDocumentRecipientFieldMetaUnion",
    Union[
        RecipientGetDocumentRecipientFieldMetaRadio,
        RecipientGetDocumentRecipientFieldMetaInitials,
        RecipientGetDocumentRecipientFieldMetaName,
        RecipientGetDocumentRecipientFieldMetaEmail,
        RecipientGetDocumentRecipientFieldMetaDate,
        RecipientGetDocumentRecipientFieldMetaDropdown,
        RecipientGetDocumentRecipientFieldMetaCheckbox,
        RecipientGetDocumentRecipientFieldMetaText,
        RecipientGetDocumentRecipientFieldMetaNumber,
    ],
)


class RecipientGetDocumentRecipientFieldTypedDict(TypedDict):
    type: RecipientGetDocumentRecipientType
    id: float
    secondary_id: str
    document_id: Nullable[float]
    template_id: Nullable[float]
    recipient_id: float
    page: float
    r"""The page number of the field on the document. Starts from 1."""
    custom_text: str
    inserted: bool
    field_meta: Nullable[RecipientGetDocumentRecipientFieldMetaUnionTypedDict]
    position_x: NotRequired[Any]
    position_y: NotRequired[Any]
    width: NotRequired[Any]
    height: NotRequired[Any]


class RecipientGetDocumentRecipientField(BaseModel):
    type: RecipientGetDocumentRecipientType

    id: float

    secondary_id: Annotated[str, pydantic.Field(alias="secondaryId")]

    document_id: Annotated[Nullable[float], pydantic.Field(alias="documentId")]

    template_id: Annotated[Nullable[float], pydantic.Field(alias="templateId")]

    recipient_id: Annotated[float, pydantic.Field(alias="recipientId")]

    page: float
    r"""The page number of the field on the document. Starts from 1."""

    custom_text: Annotated[str, pydantic.Field(alias="customText")]

    inserted: bool

    field_meta: Annotated[
        Nullable[RecipientGetDocumentRecipientFieldMetaUnion],
        pydantic.Field(alias="fieldMeta"),
    ]

    position_x: Annotated[Optional[Any], pydantic.Field(alias="positionX")] = None

    position_y: Annotated[Optional[Any], pydantic.Field(alias="positionY")] = None

    width: Optional[Any] = None

    height: Optional[Any] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["positionX", "positionY", "width", "height"]
        nullable_fields = ["documentId", "templateId", "fieldMeta"]
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


class RecipientGetDocumentRecipientResponseTypedDict(TypedDict):
    r"""Successful response"""

    role: RecipientGetDocumentRecipientRole
    read_status: RecipientGetDocumentRecipientReadStatus
    signing_status: RecipientGetDocumentRecipientSigningStatus
    send_status: RecipientGetDocumentRecipientSendStatus
    id: float
    document_id: Nullable[float]
    template_id: Nullable[float]
    email: str
    name: str
    token: str
    document_deleted_at: Nullable[str]
    expired: Nullable[str]
    signed_at: Nullable[str]
    auth_options: Nullable[RecipientGetDocumentRecipientAuthOptionsTypedDict]
    signing_order: Nullable[float]
    r"""The order in which the recipient should sign the document. Only works if the document is set to sequential signing."""
    rejection_reason: Nullable[str]
    fields: List[RecipientGetDocumentRecipientFieldTypedDict]


class RecipientGetDocumentRecipientResponse(BaseModel):
    r"""Successful response"""

    role: RecipientGetDocumentRecipientRole

    read_status: Annotated[
        RecipientGetDocumentRecipientReadStatus, pydantic.Field(alias="readStatus")
    ]

    signing_status: Annotated[
        RecipientGetDocumentRecipientSigningStatus,
        pydantic.Field(alias="signingStatus"),
    ]

    send_status: Annotated[
        RecipientGetDocumentRecipientSendStatus, pydantic.Field(alias="sendStatus")
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
        Nullable[RecipientGetDocumentRecipientAuthOptions],
        pydantic.Field(alias="authOptions"),
    ]

    signing_order: Annotated[Nullable[float], pydantic.Field(alias="signingOrder")]
    r"""The order in which the recipient should sign the document. Only works if the document is set to sequential signing."""

    rejection_reason: Annotated[Nullable[str], pydantic.Field(alias="rejectionReason")]

    fields: List[RecipientGetDocumentRecipientField]

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
