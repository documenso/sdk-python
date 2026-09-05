# ~~Documents.Recipients~~

> [!WARNING]
> This SDK is **DEPRECATED**

## Overview

### Available Operations

* [~~get~~](#get) - Get document recipient :warning: **Deprecated**
* [~~create~~](#create) - Create document recipient :warning: **Deprecated**
* [~~create_many~~](#create_many) - Create document recipients :warning: **Deprecated**
* [~~update~~](#update) - Update document recipient :warning: **Deprecated**
* [~~update_many~~](#update_many) - Update document recipients :warning: **Deprecated**
* [~~delete~~](#delete) - Delete document recipient :warning: **Deprecated**

## ~~get~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Returns a single recipient. If you want to retrieve all the recipients for a document, use the "Get Document" endpoint.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-getDocumentRecipient" method="get" path="/document/recipient/{recipientId}" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.get(recipient_id=874.3)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RecipientGetDocumentRecipientResponse](../../models/recipientgetdocumentrecipientresponse.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.RecipientGetDocumentRecipientBadRequestError     | 400                                                     | application/json                                        |
| models.RecipientGetDocumentRecipientUnauthorizedError   | 401                                                     | application/json                                        |
| models.RecipientGetDocumentRecipientForbiddenError      | 403                                                     | application/json                                        |
| models.RecipientGetDocumentRecipientNotFoundError       | 404                                                     | application/json                                        |
| models.RecipientGetDocumentRecipientInternalServerError | 500                                                     | application/json                                        |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## ~~create~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Create a single recipient for a document.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-createDocumentRecipient" method="post" path="/document/recipient/create" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.create(document_id=3058.31, recipient={
        "email": "Ila.Steuber@yahoo.com",
        "name": "<value>",
        "role": documenso_sdk.RecipientCreateDocumentRecipientRoleRequest.ASSISTANT,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                 | *float*                                                                                                       | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `recipient`                                                                                                   | [models.RecipientCreateDocumentRecipientRecipient](../../models/recipientcreatedocumentrecipientrecipient.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.RecipientCreateDocumentRecipientResponse](../../models/recipientcreatedocumentrecipientresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.RecipientCreateDocumentRecipientBadRequestError     | 400                                                        | application/json                                           |
| models.RecipientCreateDocumentRecipientUnauthorizedError   | 401                                                        | application/json                                           |
| models.RecipientCreateDocumentRecipientForbiddenError      | 403                                                        | application/json                                           |
| models.RecipientCreateDocumentRecipientInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## ~~create_many~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Create multiple recipients for a document.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-createDocumentRecipients" method="post" path="/document/recipient/create-many" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.create_many(document_id=9983.95, recipients=[
        {
            "email": "Roosevelt_Baumbach@yahoo.com",
            "name": "<value>",
            "role": documenso_sdk.RecipientCreateDocumentRecipientsRoleRequest.CC,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                                       | *float*                                                                                                                             | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `recipients`                                                                                                                        | List[[models.RecipientCreateDocumentRecipientsRecipientRequest](../../models/recipientcreatedocumentrecipientsrecipientrequest.md)] | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.RecipientCreateDocumentRecipientsResponse](../../models/recipientcreatedocumentrecipientsresponse.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| models.RecipientCreateDocumentRecipientsBadRequestError     | 400                                                         | application/json                                            |
| models.RecipientCreateDocumentRecipientsUnauthorizedError   | 401                                                         | application/json                                            |
| models.RecipientCreateDocumentRecipientsForbiddenError      | 403                                                         | application/json                                            |
| models.RecipientCreateDocumentRecipientsInternalServerError | 500                                                         | application/json                                            |
| models.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## ~~update~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Update a single recipient for a document.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-updateDocumentRecipient" method="post" path="/document/recipient/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.update(document_id=7045.62, recipient={
        "id": 2224.05,
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

**[models.RecipientUpdateDocumentRecipientResponse](../../models/recipientupdatedocumentrecipientresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.RecipientUpdateDocumentRecipientBadRequestError     | 400                                                        | application/json                                           |
| models.RecipientUpdateDocumentRecipientUnauthorizedError   | 401                                                        | application/json                                           |
| models.RecipientUpdateDocumentRecipientForbiddenError      | 403                                                        | application/json                                           |
| models.RecipientUpdateDocumentRecipientInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## ~~update_many~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Update multiple recipients for a document.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-updateDocumentRecipients" method="post" path="/document/recipient/update-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.update_many(document_id=3189.76, recipients=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                                       | *float*                                                                                                                             | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `recipients`                                                                                                                        | List[[models.RecipientUpdateDocumentRecipientsRecipientRequest](../../models/recipientupdatedocumentrecipientsrecipientrequest.md)] | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.RecipientUpdateDocumentRecipientsResponse](../../models/recipientupdatedocumentrecipientsresponse.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| models.RecipientUpdateDocumentRecipientsBadRequestError     | 400                                                         | application/json                                            |
| models.RecipientUpdateDocumentRecipientsUnauthorizedError   | 401                                                         | application/json                                            |
| models.RecipientUpdateDocumentRecipientsForbiddenError      | 403                                                         | application/json                                            |
| models.RecipientUpdateDocumentRecipientsInternalServerError | 500                                                         | application/json                                            |
| models.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## ~~delete~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-deleteDocumentRecipient" method="post" path="/document/recipient/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.recipients.delete(recipient_id=5490.43)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RecipientDeleteDocumentRecipientResponse](../../models/recipientdeletedocumentrecipientresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.RecipientDeleteDocumentRecipientBadRequestError     | 400                                                        | application/json                                           |
| models.RecipientDeleteDocumentRecipientUnauthorizedError   | 401                                                        | application/json                                           |
| models.RecipientDeleteDocumentRecipientForbiddenError      | 403                                                        | application/json                                           |
| models.RecipientDeleteDocumentRecipientInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |