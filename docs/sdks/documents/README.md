# Documents

## Overview

### Available Operations

* [get](#get) - Get document
* [find](#find) - Find documents
* [create](#create) - Create document
* [update](#update) - Update document
* [delete](#delete) - Delete document
* [duplicate](#duplicate) - Duplicate document
* [distribute](#distribute) - Distribute document
* [redistribute](#redistribute) - Redistribute document
* [download](#download) - Download document
* [create_v0](#create_v0) - Create document

## get

Returns a document given an ID

### Example Usage

<!-- UsageSnippet language="python" operationID="document-get" method="get" path="/document/{documentId}" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.get(document_id=6150.61)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentGetResponse](../../models/documentgetresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.DocumentGetBadRequestError     | 400                                   | application/json                      |
| models.DocumentGetUnauthorizedError   | 401                                   | application/json                      |
| models.DocumentGetForbiddenError      | 403                                   | application/json                      |
| models.DocumentGetNotFoundError       | 404                                   | application/json                      |
| models.DocumentGetInternalServerError | 500                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## find

Find documents based on a search criteria

### Example Usage

<!-- UsageSnippet language="python" operationID="document-find" method="get" path="/document" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find(order_by_direction=documenso_sdk.DocumentFindOrderByDirection.DESC)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `query`                                                                                       | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | The search query.                                                                             |
| `page`                                                                                        | *Optional[float]*                                                                             | :heavy_minus_sign:                                                                            | The pagination page number, starts at 1.                                                      |
| `per_page`                                                                                    | *Optional[float]*                                                                             | :heavy_minus_sign:                                                                            | The number of items per page.                                                                 |
| `template_id`                                                                                 | *Optional[float]*                                                                             | :heavy_minus_sign:                                                                            | Filter documents by the template ID used to create it.                                        |
| `source`                                                                                      | [Optional[models.DocumentFindQueryParamSource]](../../models/documentfindqueryparamsource.md) | :heavy_minus_sign:                                                                            | Filter documents by how it was created.                                                       |
| `status`                                                                                      | [Optional[models.DocumentFindQueryParamStatus]](../../models/documentfindqueryparamstatus.md) | :heavy_minus_sign:                                                                            | Filter documents by the current status                                                        |
| `folder_id`                                                                                   | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | Filter documents by folder ID                                                                 |
| `order_by_column`                                                                             | [Optional[models.DocumentFindOrderByColumn]](../../models/documentfindorderbycolumn.md)       | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `order_by_direction`                                                                          | [Optional[models.DocumentFindOrderByDirection]](../../models/documentfindorderbydirection.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.DocumentFindResponse](../../models/documentfindresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.DocumentFindBadRequestError     | 400                                    | application/json                       |
| models.DocumentFindUnauthorizedError   | 401                                    | application/json                       |
| models.DocumentFindForbiddenError      | 403                                    | application/json                       |
| models.DocumentFindNotFoundError       | 404                                    | application/json                       |
| models.DocumentFindInternalServerError | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

Create a document using form data.

### Example Usage

<!-- UsageSnippet language="python" operationID="document-create" method="post" path="/document/create" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.create(payload={
        "title": "<value>",
    }, file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `payload`                                                             | [models.DocumentCreatePayload](../../models/documentcreatepayload.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `file`                                                                | [models.DocumentCreateFile](../../models/documentcreatefile.md)       | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.DocumentCreateResponse](../../models/documentcreateresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.DocumentCreateBadRequestError     | 400                                      | application/json                         |
| models.DocumentCreateUnauthorizedError   | 401                                      | application/json                         |
| models.DocumentCreateForbiddenError      | 403                                      | application/json                         |
| models.DocumentCreateInternalServerError | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## update

Update document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-update" method="post" path="/document/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.update(document_id=3428.95)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `document_id`                                                             | *float*                                                                   | :heavy_check_mark:                                                        | N/A                                                                       |
| `data`                                                                    | [Optional[models.DocumentUpdateData]](../../models/documentupdatedata.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `meta`                                                                    | [Optional[models.DocumentUpdateMeta]](../../models/documentupdatemeta.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.DocumentUpdateResponse](../../models/documentupdateresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.DocumentUpdateBadRequestError     | 400                                      | application/json                         |
| models.DocumentUpdateUnauthorizedError   | 401                                      | application/json                         |
| models.DocumentUpdateForbiddenError      | 403                                      | application/json                         |
| models.DocumentUpdateInternalServerError | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## delete

Delete document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-delete" method="post" path="/document/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.delete(document_id=3963.4)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentDeleteResponse](../../models/documentdeleteresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.DocumentDeleteBadRequestError     | 400                                      | application/json                         |
| models.DocumentDeleteUnauthorizedError   | 401                                      | application/json                         |
| models.DocumentDeleteForbiddenError      | 403                                      | application/json                         |
| models.DocumentDeleteInternalServerError | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## duplicate

Duplicate document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-duplicate" method="post" path="/document/duplicate" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.duplicate(document_id=5285.3)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentDuplicateResponse](../../models/documentduplicateresponse.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.DocumentDuplicateBadRequestError     | 400                                         | application/json                            |
| models.DocumentDuplicateUnauthorizedError   | 401                                         | application/json                            |
| models.DocumentDuplicateForbiddenError      | 403                                         | application/json                            |
| models.DocumentDuplicateInternalServerError | 500                                         | application/json                            |
| models.APIError                             | 4XX, 5XX                                    | \*/\*                                       |

## distribute

Send the document out to recipients based on your distribution method

### Example Usage

<!-- UsageSnippet language="python" operationID="document-distribute" method="post" path="/document/distribute" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.distribute(document_id=7548.74)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `document_id`                                                                     | *float*                                                                           | :heavy_check_mark:                                                                | N/A                                                                               |
| `meta`                                                                            | [Optional[models.DocumentDistributeMeta]](../../models/documentdistributemeta.md) | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.DocumentDistributeResponse](../../models/documentdistributeresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.DocumentDistributeBadRequestError     | 400                                          | application/json                             |
| models.DocumentDistributeUnauthorizedError   | 401                                          | application/json                             |
| models.DocumentDistributeForbiddenError      | 403                                          | application/json                             |
| models.DocumentDistributeInternalServerError | 500                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## redistribute

Redistribute the document to the provided recipients who have not actioned the document. Will use the distribution method set in the document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-redistribute" method="post" path="/document/redistribute" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.redistribute(document_id=9084.69, recipients=[
        6011.8,
        4441.56,
        4251.15,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `recipients`                                                        | List[*float*]                                                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentRedistributeResponse](../../models/documentredistributeresponse.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.DocumentRedistributeBadRequestError     | 400                                            | application/json                               |
| models.DocumentRedistributeUnauthorizedError   | 401                                            | application/json                               |
| models.DocumentRedistributeForbiddenError      | 403                                            | application/json                               |
| models.DocumentRedistributeInternalServerError | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## download

Download document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-download" method="get" path="/document/{documentId}/download" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.download(document_id=5396.97, version=documenso_sdk.DocumentDownloadVersion.SIGNED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_id`                                                                                                                                        | *float*                                                                                                                                              | :heavy_check_mark:                                                                                                                                   | The ID of the document to download.                                                                                                                  |
| `version`                                                                                                                                            | [Optional[models.DocumentDownloadVersion]](../../models/documentdownloadversion.md)                                                                  | :heavy_minus_sign:                                                                                                                                   | The version of the document to download. "signed" returns the completed document with signatures, "original" returns the original uploaded document. |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[models.DocumentDownloadResponse](../../models/documentdownloadresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.DocumentDownloadBadRequestError     | 400                                        | application/json                           |
| models.DocumentDownloadUnauthorizedError   | 401                                        | application/json                           |
| models.DocumentDownloadForbiddenError      | 403                                        | application/json                           |
| models.DocumentDownloadNotFoundError       | 404                                        | application/json                           |
| models.DocumentDownloadInternalServerError | 500                                        | application/json                           |
| models.APIError                            | 4XX, 5XX                                   | \*/\*                                      |

## create_v0

You will need to upload the PDF to the provided URL returned. Note: Once V2 API is released, this will be removed since we will allow direct uploads, instead of using an upload URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="document-createDocumentTemporary" method="post" path="/document/create/beta" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.create_v0(title="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`                                                                                                                                       | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |
| `external_id`                                                                                                                                 | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `visibility`                                                                                                                                  | [Optional[models.DocumentCreateDocumentTemporaryVisibilityRequest]](../../models/documentcreatedocumenttemporaryvisibilityrequest.md)         | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `global_access_auth`                                                                                                                          | List[[models.DocumentCreateDocumentTemporaryGlobalAccessAuthRequest](../../models/documentcreatedocumenttemporaryglobalaccessauthrequest.md)] | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `global_action_auth`                                                                                                                          | List[[models.DocumentCreateDocumentTemporaryGlobalActionAuthRequest](../../models/documentcreatedocumenttemporaryglobalactionauthrequest.md)] | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `form_values`                                                                                                                                 | Dict[str, [models.DocumentCreateDocumentTemporaryFormValuesRequest](../../models/documentcreatedocumenttemporaryformvaluesrequest.md)]        | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `folder_id`                                                                                                                                   | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `recipients`                                                                                                                                  | List[[models.DocumentCreateDocumentTemporaryRecipientRequest](../../models/documentcreatedocumenttemporaryrecipientrequest.md)]               | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `attachments`                                                                                                                                 | List[[models.DocumentCreateDocumentTemporaryAttachment](../../models/documentcreatedocumenttemporaryattachment.md)]                           | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `meta`                                                                                                                                        | [Optional[models.DocumentCreateDocumentTemporaryMeta]](../../models/documentcreatedocumenttemporarymeta.md)                                   | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.DocumentCreateDocumentTemporaryResponse](../../models/documentcreatedocumenttemporaryresponse.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| models.DocumentCreateDocumentTemporaryBadRequestError     | 400                                                       | application/json                                          |
| models.DocumentCreateDocumentTemporaryUnauthorizedError   | 401                                                       | application/json                                          |
| models.DocumentCreateDocumentTemporaryForbiddenError      | 403                                                       | application/json                                          |
| models.DocumentCreateDocumentTemporaryInternalServerError | 500                                                       | application/json                                          |
| models.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |