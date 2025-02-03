# Recipients
(*documents.recipients*)

## Overview

### Available Operations

* [get](#get) - Get document recipient
* [create](#create) - Create document recipient
* [create_many](#create_many) - Create document recipients
* [update](#update) - Update document recipient
* [update_many](#update_many) - Update document recipients
* [delete](#delete) - Delete document recipient

## get

Returns a single recipient. If you want to retrieve all the recipients for a document, use the "Get Document" endpoint.

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.get(recipient_id=7003.47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RecipientGetDocumentRecipientResponseBody](../../models/recipientgetdocumentrecipientresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.RecipientGetDocumentRecipientDocumentsRecipientsResponseBody            | 400                                                                            | application/json                                                               |
| models.RecipientGetDocumentRecipientDocumentsRecipientsResponseResponseBody    | 404                                                                            | application/json                                                               |
| models.RecipientGetDocumentRecipientDocumentsRecipientsResponse500ResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |

## create

Create a single recipient for a document.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.create(document_id=4865.89, recipient={
        "email": "Haylie_Bernhard95@yahoo.com",
        "name": "<value>",
        "role": documenso_sdk.RecipientCreateDocumentRecipientRole.CC,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `recipient`                                                         | [models.Recipient](../../models/recipient.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RecipientCreateDocumentRecipientResponseBody](../../models/recipientcreatedocumentrecipientresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.RecipientCreateDocumentRecipientDocumentsRecipientsResponseBody         | 400                                                                            | application/json                                                               |
| models.RecipientCreateDocumentRecipientDocumentsRecipientsResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |

## create_many

Create multiple recipients for a document.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.create_many(document_id=5158.41, recipients=[
        {
            "email": "Demetrius.Sanford35@hotmail.com",
            "name": "<value>",
            "role": documenso_sdk.RecipientCreateDocumentRecipientsRole.VIEWER,
        },
        {
            "email": "Lyla50@yahoo.com",
            "name": "<value>",
            "role": documenso_sdk.RecipientCreateDocumentRecipientsRole.APPROVER,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                           | *float*                                                                                                                 | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `recipients`                                                                                                            | List[[models.RecipientCreateDocumentRecipientsRecipients](../../models/recipientcreatedocumentrecipientsrecipients.md)] | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.RecipientCreateDocumentRecipientsResponseBody](../../models/recipientcreatedocumentrecipientsresponsebody.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| models.RecipientCreateDocumentRecipientsDocumentsRecipientsResponseBody         | 400                                                                             | application/json                                                                |
| models.RecipientCreateDocumentRecipientsDocumentsRecipientsResponseResponseBody | 500                                                                             | application/json                                                                |
| models.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |

## update

Update a single recipient for a document.

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.update(document_id=8574.78, recipient={
        "id": 5971.29,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                 | *float*                                                                                                       | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `recipient`                                                                                                   | [models.RecipientUpdateDocumentRecipientRecipient](../../models/recipientupdatedocumentrecipientrecipient.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.RecipientUpdateDocumentRecipientResponseBody](../../models/recipientupdatedocumentrecipientresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.RecipientUpdateDocumentRecipientDocumentsRecipientsResponseBody         | 400                                                                            | application/json                                                               |
| models.RecipientUpdateDocumentRecipientDocumentsRecipientsResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |

## update_many

Update multiple recipients for a document.

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.update_many(document_id=4057.69, recipients=[
        {
            "id": 5359.16,
        },
        {
            "id": 8982.15,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                           | *float*                                                                                                                 | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `recipients`                                                                                                            | List[[models.RecipientUpdateDocumentRecipientsRecipients](../../models/recipientupdatedocumentrecipientsrecipients.md)] | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.RecipientUpdateDocumentRecipientsResponseBody](../../models/recipientupdatedocumentrecipientsresponsebody.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| models.RecipientUpdateDocumentRecipientsDocumentsRecipientsResponseBody         | 400                                                                             | application/json                                                                |
| models.RecipientUpdateDocumentRecipientsDocumentsRecipientsResponseResponseBody | 500                                                                             | application/json                                                                |
| models.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |

## delete

Delete document recipient

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.delete(recipient_id=5459.07)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RecipientDeleteDocumentRecipientResponseBody](../../models/recipientdeletedocumentrecipientresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.RecipientDeleteDocumentRecipientDocumentsRecipientsResponseBody         | 400                                                                            | application/json                                                               |
| models.RecipientDeleteDocumentRecipientDocumentsRecipientsResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |