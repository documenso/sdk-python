# Envelopes.Items

## Overview

### Available Operations

* [create_many](#create_many) - Create envelope items
* [update_many](#update_many) - Update envelope items
* [delete](#delete) - Delete envelope item
* [download](#download) - Download an envelope item

## create_many

Create multiple envelope items for an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-item-createMany" method="post" path="/envelope/item/create-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.items.create_many(payload={
        "envelope_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `payload`                                                                             | [models.EnvelopeItemCreateManyPayload](../../models/envelopeitemcreatemanypayload.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `files`                                                                               | List[[models.EnvelopeItemCreateManyFile](../../models/envelopeitemcreatemanyfile.md)] | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.EnvelopeItemCreateManyResponse](../../models/envelopeitemcreatemanyresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.EnvelopeItemCreateManyBadRequestError     | 400                                              | application/json                                 |
| models.EnvelopeItemCreateManyUnauthorizedError   | 401                                              | application/json                                 |
| models.EnvelopeItemCreateManyForbiddenError      | 403                                              | application/json                                 |
| models.EnvelopeItemCreateManyInternalServerError | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## update_many

Update multiple envelope items for an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-item-updateMany" method="post" path="/envelope/item/update-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.items.update_many(envelope_id="<id>", data=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `envelope_id`                                                                                       | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `data`                                                                                              | List[[models.EnvelopeItemUpdateManyDataRequest](../../models/envelopeitemupdatemanydatarequest.md)] | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.EnvelopeItemUpdateManyResponse](../../models/envelopeitemupdatemanyresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.EnvelopeItemUpdateManyBadRequestError     | 400                                              | application/json                                 |
| models.EnvelopeItemUpdateManyUnauthorizedError   | 401                                              | application/json                                 |
| models.EnvelopeItemUpdateManyForbiddenError      | 403                                              | application/json                                 |
| models.EnvelopeItemUpdateManyInternalServerError | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## delete

Delete an envelope item from an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-item-delete" method="post" path="/envelope/item/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.items.delete(envelope_id="<id>", envelope_item_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `envelope_item_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeItemDeleteResponse](../../models/envelopeitemdeleteresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.EnvelopeItemDeleteBadRequestError     | 400                                          | application/json                             |
| models.EnvelopeItemDeleteUnauthorizedError   | 401                                          | application/json                             |
| models.EnvelopeItemDeleteForbiddenError      | 403                                          | application/json                             |
| models.EnvelopeItemDeleteInternalServerError | 500                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## download

Download an envelope item by its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-item-download" method="get" path="/envelope/item/{envelopeItemId}/download" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.items.download(envelope_item_id="<id>", version=documenso_sdk.EnvelopeItemDownloadVersion.SIGNED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `envelope_item_id`                                                                                                                                        | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The ID of the envelope item to download.                                                                                                                  |
| `version`                                                                                                                                                 | [Optional[models.EnvelopeItemDownloadVersion]](../../models/envelopeitemdownloadversion.md)                                                               | :heavy_minus_sign:                                                                                                                                        | The version of the envelope item to download. "signed" returns the completed document with signatures, "original" returns the original uploaded document. |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |

### Response

**[models.EnvelopeItemDownloadResponse](../../models/envelopeitemdownloadresponse.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.EnvelopeItemDownloadBadRequestError     | 400                                            | application/json                               |
| models.EnvelopeItemDownloadUnauthorizedError   | 401                                            | application/json                               |
| models.EnvelopeItemDownloadForbiddenError      | 403                                            | application/json                               |
| models.EnvelopeItemDownloadNotFoundError       | 404                                            | application/json                               |
| models.EnvelopeItemDownloadInternalServerError | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |