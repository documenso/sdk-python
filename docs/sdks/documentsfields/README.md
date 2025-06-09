# DocumentsFields
(*documents.fields*)

## Overview

### Available Operations

* [get](#get) - Get document field
* [create](#create) - Create document field
* [create_many](#create_many) - Create document fields
* [update](#update) - Update document field
* [update_many](#update_many) - Update document fields
* [delete](#delete) - Delete document field

## get

Returns a single field. If you want to retrieve all the fields for a document, use the "Get Document" endpoint.

### Example Usage

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.fields.get(field_id=6077.81)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `field_id`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FieldGetDocumentFieldResponse](../../models/fieldgetdocumentfieldresponse.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.FieldGetDocumentFieldBadRequestError     | 400                                             | application/json                                |
| models.FieldGetDocumentFieldNotFoundError       | 404                                             | application/json                                |
| models.FieldGetDocumentFieldInternalServerError | 500                                             | application/json                                |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## create

Create a single field for a document.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.fields.create(document_id=8001.93, field={
        "type": documenso_sdk.FieldCreateDocumentFieldTypeNameRequestBody1.NAME,
        "recipient_id": 2564.68,
        "page_number": 791.77,
        "page_x": 7845.22,
        "page_y": 6843.16,
        "width": 3932.15,
        "height": 8879.89,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `document_id`                                                                                   | *float*                                                                                         | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `field`                                                                                         | [models.FieldCreateDocumentFieldFieldUnion](../../models/fieldcreatedocumentfieldfieldunion.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.FieldCreateDocumentFieldResponse](../../models/fieldcreatedocumentfieldresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.FieldCreateDocumentFieldBadRequestError     | 400                                                | application/json                                   |
| models.FieldCreateDocumentFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## create_many

Create multiple fields for a document.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.fields.create_many(document_id=6257.51, fields=[
        {
            "type": documenso_sdk.FieldCreateDocumentFieldsTypeFreeSignature.FREE_SIGNATURE,
            "recipient_id": 679.35,
            "page_number": 5914.59,
            "page_x": 7253.11,
            "page_y": 8426.91,
            "width": 8995.55,
            "height": 9808.97,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                           | *float*                                                                                                 | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `fields`                                                                                                | List[[models.FieldCreateDocumentFieldsFieldUnion](../../models/fieldcreatedocumentfieldsfieldunion.md)] | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.FieldCreateDocumentFieldsResponse](../../models/fieldcreatedocumentfieldsresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.FieldCreateDocumentFieldsBadRequestError     | 400                                                 | application/json                                    |
| models.FieldCreateDocumentFieldsInternalServerError | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## update

Update a single field for a document.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.fields.update(document_id=5956.26, field={
        "type": documenso_sdk.FieldUpdateDocumentFieldTypeFreeSignature.FREE_SIGNATURE,
        "id": 6955.16,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `document_id`                                                                                   | *float*                                                                                         | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `field`                                                                                         | [models.FieldUpdateDocumentFieldFieldUnion](../../models/fieldupdatedocumentfieldfieldunion.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.FieldUpdateDocumentFieldResponse](../../models/fieldupdatedocumentfieldresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.FieldUpdateDocumentFieldBadRequestError     | 400                                                | application/json                                   |
| models.FieldUpdateDocumentFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## update_many

Update multiple fields for a document.

### Example Usage

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.fields.update_many(document_id=9317.43, fields=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                           | *float*                                                                                                 | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `fields`                                                                                                | List[[models.FieldUpdateDocumentFieldsFieldUnion](../../models/fieldupdatedocumentfieldsfieldunion.md)] | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.FieldUpdateDocumentFieldsResponse](../../models/fieldupdatedocumentfieldsresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.FieldUpdateDocumentFieldsBadRequestError     | 400                                                 | application/json                                    |
| models.FieldUpdateDocumentFieldsInternalServerError | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## delete

Delete document field

### Example Usage

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.fields.delete(field_id=4748.27)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `field_id`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FieldDeleteDocumentFieldResponse](../../models/fielddeletedocumentfieldresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.FieldDeleteDocumentFieldBadRequestError     | 400                                                | application/json                                   |
| models.FieldDeleteDocumentFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |