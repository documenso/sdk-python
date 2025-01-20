# Fields
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

    res = documenso.documents.fields.get(field_id=7003.47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `field_id`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FieldGetDocumentFieldResponseBody](../../models/fieldgetdocumentfieldresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ErrorNOTFOUND            | 404                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

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

    res = documenso.documents.fields.create(document_id=4865.89, field={
        "type": documenso_sdk.FieldCreateDocumentFieldFieldDocumentsFieldsRequestRequestBody8Type.NUMBER,
        "recipient_id": 4174.58,
        "page_number": 1343.65,
        "page_x": 690.25,
        "page_y": 7964.74,
        "width": 9510.62,
        "height": 0.86,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `field`                                                             | [models.Field](../../models/field.md)                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FieldCreateDocumentFieldResponseBody](../../models/fieldcreatedocumentfieldresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

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

    res = documenso.documents.fields.create_many(document_id=5158.41, fields=[
        {
            "type": documenso_sdk.FieldCreateDocumentFieldsFieldsDocumentsFieldsRequestRequestBody10Type.CHECKBOX,
            "recipient_id": 2516.72,
            "page_number": 2304.17,
            "page_x": 7760.32,
            "page_y": 3376.66,
            "width": 3566.94,
            "height": 2768.94,
        },
        {
            "type": documenso_sdk.FieldCreateDocumentFieldsFieldsDocumentsFieldsRequestRequestBody8Type.NUMBER,
            "recipient_id": 5689.64,
            "page_number": 6483.69,
            "page_x": 7271.79,
            "page_y": 1891.56,
            "width": 7263.21,
            "height": 5043.41,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `document_id`                                                                                   | *float*                                                                                         | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `fields`                                                                                        | List[[models.FieldCreateDocumentFieldsFields](../../models/fieldcreatedocumentfieldsfields.md)] | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.FieldCreateDocumentFieldsResponseBody](../../models/fieldcreatedocumentfieldsresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

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

    res = documenso.documents.fields.update(document_id=8574.78, field={
        "type": documenso_sdk.FieldUpdateDocumentFieldFieldDocumentsFieldsRequestRequestBody7Type.TEXT,
        "id": 3446.2,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `document_id`                                                                         | *float*                                                                               | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `field`                                                                               | [models.FieldUpdateDocumentFieldField](../../models/fieldupdatedocumentfieldfield.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.FieldUpdateDocumentFieldResponseBody](../../models/fieldupdatedocumentfieldresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## update_many

Update multiple fields for a document.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.fields.update_many(document_id=4057.69, fields=[
        {
            "type": documenso_sdk.FieldUpdateDocumentFieldsFieldsDocumentsFieldsRequestRequestBody6Type.DATE,
            "id": 8982.15,
        },
        {
            "type": documenso_sdk.FieldUpdateDocumentFieldsFieldsDocumentsFieldsRequestRequestBody4Type.NAME,
            "id": 310.19,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `document_id`                                                                                   | *float*                                                                                         | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `fields`                                                                                        | List[[models.FieldUpdateDocumentFieldsFields](../../models/fieldupdatedocumentfieldsfields.md)] | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.FieldUpdateDocumentFieldsResponseBody](../../models/fieldupdatedocumentfieldsresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## delete

Delete document field

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.fields.delete(field_id=5459.07)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `field_id`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FieldDeleteDocumentFieldResponseBody](../../models/fielddeletedocumentfieldresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |