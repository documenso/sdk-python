# Document

## Overview

### Available Operations

* [document_get_many](#document_get_many) - Get multiple documents
* [document_download](#document_download) - Download document (beta)

## document_get_many

Retrieve multiple documents by their IDs

### Example Usage

<!-- UsageSnippet language="python" operationID="document-getMany" method="post" path="/document/get-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.document.document_get_many(document_ids=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_ids`                                                      | List[*float*]                                                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentGetManyResponse](../../models/documentgetmanyresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| models.DocumentGetManyBadRequestError     | 400                                       | application/json                          |
| models.DocumentGetManyUnauthorizedError   | 401                                       | application/json                          |
| models.DocumentGetManyForbiddenError      | 403                                       | application/json                          |
| models.DocumentGetManyInternalServerError | 500                                       | application/json                          |
| models.APIError                           | 4XX, 5XX                                  | \*/\*                                     |

## document_download

Get a pre-signed download URL for the original or signed version of a document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-downloadBeta" method="get" path="/document/{documentId}/download-beta" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.document.document_download(document_id=9550.11, version=documenso_sdk.DocumentDownloadBetaVersion.SIGNED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                                                        | *float*                                                                                                                                              | :heavy_check_mark:                                                                                                                                   | The ID of the document to download.                                                                                                                  |
| `version`                                                                                                                                            | [Optional[models.DocumentDownloadBetaVersion]](../../models/documentdownloadbetaversion.md)                                                          | :heavy_minus_sign:                                                                                                                                   | The version of the document to download. "signed" returns the completed document with signatures, "original" returns the original uploaded document. |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[models.DocumentDownloadBetaResponse](../../models/documentdownloadbetaresponse.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.DocumentDownloadBetaBadRequestError     | 400                                            | application/json                               |
| models.DocumentDownloadBetaUnauthorizedError   | 401                                            | application/json                               |
| models.DocumentDownloadBetaForbiddenError      | 403                                            | application/json                               |
| models.DocumentDownloadBetaNotFoundError       | 404                                            | application/json                               |
| models.DocumentDownloadBetaInternalServerError | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |