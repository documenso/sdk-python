# Documents
(*documents*)

## Overview

### Available Operations

* [update](#update) - Update document
* [find](#find) - Find documents
* [get](#get) - Get document
* [create_v0](#create_v0) - Create document
* [delete](#delete) - Delete document
* [distribute](#distribute) - Distribute document
* [redistribute](#redistribute) - Redistribute document
* [duplicate](#duplicate) - Duplicate document

## update

Update document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-updateDocument" method="post" path="/document/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.update(document_id=9701.92)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `document_id`                                                                             | *float*                                                                                   | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `data`                                                                                    | [Optional[models.DocumentUpdateDocumentData]](../../models/documentupdatedocumentdata.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `meta`                                                                                    | [Optional[models.DocumentUpdateDocumentMeta]](../../models/documentupdatedocumentmeta.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.DocumentUpdateDocumentResponse](../../models/documentupdatedocumentresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.DocumentUpdateDocumentBadRequestError     | 400                                              | application/json                                 |
| models.DocumentUpdateDocumentInternalServerError | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## find

Find documents based on a search criteria

### Example Usage

<!-- UsageSnippet language="python" operationID="document-findDocuments" method="get" path="/document" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find(order_by_direction=documenso_sdk.OrderByDirection.DESC)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `query`                                                               | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | The search query.                                                     |
| `page`                                                                | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | The pagination page number, starts at 1.                              |
| `per_page`                                                            | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | The number of items per page.                                         |
| `template_id`                                                         | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | Filter documents by the template ID used to create it.                |
| `source`                                                              | [Optional[models.QueryParamSource]](../../models/queryparamsource.md) | :heavy_minus_sign:                                                    | Filter documents by how it was created.                               |
| `status`                                                              | [Optional[models.QueryParamStatus]](../../models/queryparamstatus.md) | :heavy_minus_sign:                                                    | Filter documents by the current status                                |
| `folder_id`                                                           | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Filter documents by folder ID                                         |
| `order_by_column`                                                     | [Optional[models.OrderByColumn]](../../models/orderbycolumn.md)       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `order_by_direction`                                                  | [Optional[models.OrderByDirection]](../../models/orderbydirection.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.DocumentFindDocumentsResponse](../../models/documentfinddocumentsresponse.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.DocumentFindDocumentsBadRequestError     | 400                                             | application/json                                |
| models.DocumentFindDocumentsNotFoundError       | 404                                             | application/json                                |
| models.DocumentFindDocumentsInternalServerError | 500                                             | application/json                                |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## get

Returns a document given an ID

### Example Usage

<!-- UsageSnippet language="python" operationID="document-getDocumentWithDetailsById" method="get" path="/document/{documentId}" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.get(document_id=7491.86)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `folder_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter documents by folder ID                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentGetDocumentWithDetailsByIDResponse](../../models/documentgetdocumentwithdetailsbyidresponse.md)**

### Errors

| Error Type                                                   | Status Code                                                  | Content Type                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| models.DocumentGetDocumentWithDetailsByIDBadRequestError     | 400                                                          | application/json                                             |
| models.DocumentGetDocumentWithDetailsByIDNotFoundError       | 404                                                          | application/json                                             |
| models.DocumentGetDocumentWithDetailsByIDInternalServerError | 500                                                          | application/json                                             |
| models.APIError                                              | 4XX, 5XX                                                     | \*/\*                                                        |

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
| `title`                                                                                                                                       | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The title of the document.                                                                                                                    |
| `external_id`                                                                                                                                 | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The external ID of the document.                                                                                                              |
| `visibility`                                                                                                                                  | [Optional[models.DocumentCreateDocumentTemporaryVisibilityRequest]](../../models/documentcreatedocumenttemporaryvisibilityrequest.md)         | :heavy_minus_sign:                                                                                                                            | The visibility of the document.                                                                                                               |
| `global_access_auth`                                                                                                                          | List[[models.DocumentCreateDocumentTemporaryGlobalAccessAuthRequest](../../models/documentcreatedocumenttemporaryglobalaccessauthrequest.md)] | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `global_action_auth`                                                                                                                          | List[[models.DocumentCreateDocumentTemporaryGlobalActionAuthRequest](../../models/documentcreatedocumenttemporaryglobalactionauthrequest.md)] | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `form_values`                                                                                                                                 | Dict[str, [models.FormValuesRequest](../../models/formvaluesrequest.md)]                                                                      | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `recipients`                                                                                                                                  | List[[models.DocumentCreateDocumentTemporaryRecipientRequest](../../models/documentcreatedocumenttemporaryrecipientrequest.md)]               | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `meta`                                                                                                                                        | [Optional[models.DocumentCreateDocumentTemporaryMeta]](../../models/documentcreatedocumenttemporarymeta.md)                                   | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.DocumentCreateDocumentTemporaryResponse](../../models/documentcreatedocumenttemporaryresponse.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| models.DocumentCreateDocumentTemporaryBadRequestError     | 400                                                       | application/json                                          |
| models.DocumentCreateDocumentTemporaryInternalServerError | 500                                                       | application/json                                          |
| models.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## delete

Delete document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-deleteDocument" method="post" path="/document/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.delete(document_id=4054.62)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentDeleteDocumentResponse](../../models/documentdeletedocumentresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.DocumentDeleteDocumentBadRequestError     | 400                                              | application/json                                 |
| models.DocumentDeleteDocumentInternalServerError | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## distribute

Send the document out to recipients based on your distribution method

### Example Usage

<!-- UsageSnippet language="python" operationID="document-sendDocument" method="post" path="/document/distribute" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.distribute(document_id=7930.82)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `document_id`                                                                         | *float*                                                                               | :heavy_check_mark:                                                                    | The ID of the document to send.                                                       |
| `meta`                                                                                | [Optional[models.DocumentSendDocumentMeta]](../../models/documentsenddocumentmeta.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.DocumentSendDocumentResponse](../../models/documentsenddocumentresponse.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.DocumentSendDocumentBadRequestError     | 400                                            | application/json                               |
| models.DocumentSendDocumentInternalServerError | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## redistribute

Redistribute the document to the provided recipients who have not actioned the document. Will use the distribution method set in the document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-resendDocument" method="post" path="/document/redistribute" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.redistribute(document_id=2824.22, recipients=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `recipients`                                                        | List[*float*]                                                       | :heavy_check_mark:                                                  | The IDs of the recipients to redistribute the document to.          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentResendDocumentResponse](../../models/documentresenddocumentresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.DocumentResendDocumentBadRequestError     | 400                                              | application/json                                 |
| models.DocumentResendDocumentInternalServerError | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## duplicate

Duplicate document

### Example Usage

<!-- UsageSnippet language="python" operationID="document-duplicateDocument" method="post" path="/document/duplicate" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.duplicate(document_id=309.05)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentDuplicateDocumentResponse](../../models/documentduplicatedocumentresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.DocumentDuplicateDocumentBadRequestError     | 400                                                 | application/json                                    |
| models.DocumentDuplicateDocumentInternalServerError | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |