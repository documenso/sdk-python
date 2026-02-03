# Documents.Attachments

## Overview

### Available Operations

* [create](#create) - Create attachment
* [update](#update) - Update attachment
* [delete](#delete) - Delete attachment
* [find](#find) - Find attachments

## create

Create a new attachment for a document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-attachment-create" method="post" path="/document/attachment/create" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.attachments.create(document_id=7014.36, data={
        "label": "<value>",
        "data": "https://cheerful-bourgeoisie.org/",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `document_id`                                                                       | *float*                                                                             | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `data`                                                                              | [models.DocumentAttachmentCreateData](../../models/documentattachmentcreatedata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.DocumentAttachmentCreateResponse](../../models/documentattachmentcreateresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.DocumentAttachmentCreateBadRequestError     | 400                                                | application/json                                   |
| models.DocumentAttachmentCreateUnauthorizedError   | 401                                                | application/json                                   |
| models.DocumentAttachmentCreateForbiddenError      | 403                                                | application/json                                   |
| models.DocumentAttachmentCreateInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## update

Update an existing attachment

### Example Usage

<!-- UsageSnippet language="python" operationID="document-attachment-update" method="post" path="/document/attachment/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.attachments.update(id="<id>", data={
        "label": "<value>",
        "data": "https://tinted-ceramics.biz",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `data`                                                                              | [models.DocumentAttachmentUpdateData](../../models/documentattachmentupdatedata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.DocumentAttachmentUpdateResponse](../../models/documentattachmentupdateresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.DocumentAttachmentUpdateBadRequestError     | 400                                                | application/json                                   |
| models.DocumentAttachmentUpdateUnauthorizedError   | 401                                                | application/json                                   |
| models.DocumentAttachmentUpdateForbiddenError      | 403                                                | application/json                                   |
| models.DocumentAttachmentUpdateInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## delete

Delete an attachment from a document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-attachment-delete" method="post" path="/document/attachment/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.attachments.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentAttachmentDeleteResponse](../../models/documentattachmentdeleteresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.DocumentAttachmentDeleteBadRequestError     | 400                                                | application/json                                   |
| models.DocumentAttachmentDeleteUnauthorizedError   | 401                                                | application/json                                   |
| models.DocumentAttachmentDeleteForbiddenError      | 403                                                | application/json                                   |
| models.DocumentAttachmentDeleteInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## find

Find all attachments for a document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-attachment-find" method="get" path="/document/attachment" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.attachments.find(document_id=965.17)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentAttachmentFindResponse](../../models/documentattachmentfindresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.DocumentAttachmentFindBadRequestError     | 400                                              | application/json                                 |
| models.DocumentAttachmentFindUnauthorizedError   | 401                                              | application/json                                 |
| models.DocumentAttachmentFindForbiddenError      | 403                                              | application/json                                 |
| models.DocumentAttachmentFindNotFoundError       | 404                                              | application/json                                 |
| models.DocumentAttachmentFindInternalServerError | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |