# EnvelopesFields
(*envelopes.fields*)

## Overview

### Available Operations

* [get](#get) - Get envelope field
* [create_many](#create_many) - Create envelope fields
* [update_many](#update_many) - Update envelope fields
* [delete](#delete) - Delete envelope field

## get

Returns an envelope field given an ID

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-field-get" method="get" path="/envelope/field/{fieldId}" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.fields.get(field_id=6981.76)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `field_id`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeFieldGetResponse](../../models/envelopefieldgetresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.EnvelopeFieldGetBadRequestError     | 400                                        | application/json                           |
| models.EnvelopeFieldGetUnauthorizedError   | 401                                        | application/json                           |
| models.EnvelopeFieldGetForbiddenError      | 403                                        | application/json                           |
| models.EnvelopeFieldGetNotFoundError       | 404                                        | application/json                           |
| models.EnvelopeFieldGetInternalServerError | 500                                        | application/json                           |
| models.APIError                            | 4XX, 5XX                                   | \*/\*                                      |

## create_many

Create multiple fields for an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-field-createMany" method="post" path="/envelope/field/create-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.fields.create_many(envelope_id="<id>", data=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `envelope_id`                                                                                     | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `data`                                                                                            | List[[models.EnvelopeFieldCreateManyDataUnion](../../models/envelopefieldcreatemanydataunion.md)] | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.EnvelopeFieldCreateManyResponse](../../models/envelopefieldcreatemanyresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.EnvelopeFieldCreateManyBadRequestError     | 400                                               | application/json                                  |
| models.EnvelopeFieldCreateManyUnauthorizedError   | 401                                               | application/json                                  |
| models.EnvelopeFieldCreateManyForbiddenError      | 403                                               | application/json                                  |
| models.EnvelopeFieldCreateManyInternalServerError | 500                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## update_many

Update multiple envelope fields for an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-field-updateMany" method="post" path="/envelope/field/update-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.fields.update_many(envelope_id="<id>", data=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `envelope_id`                                                                                     | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `data`                                                                                            | List[[models.EnvelopeFieldUpdateManyDataUnion](../../models/envelopefieldupdatemanydataunion.md)] | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.EnvelopeFieldUpdateManyResponse](../../models/envelopefieldupdatemanyresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.EnvelopeFieldUpdateManyBadRequestError     | 400                                               | application/json                                  |
| models.EnvelopeFieldUpdateManyUnauthorizedError   | 401                                               | application/json                                  |
| models.EnvelopeFieldUpdateManyForbiddenError      | 403                                               | application/json                                  |
| models.EnvelopeFieldUpdateManyInternalServerError | 500                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## delete

Delete an envelope field

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-field-delete" method="post" path="/envelope/field/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.fields.delete(field_id=2481.37)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `field_id`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeFieldDeleteResponse](../../models/envelopefielddeleteresponse.md)**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| models.EnvelopeFieldDeleteBadRequestError     | 400                                           | application/json                              |
| models.EnvelopeFieldDeleteUnauthorizedError   | 401                                           | application/json                              |
| models.EnvelopeFieldDeleteForbiddenError      | 403                                           | application/json                              |
| models.EnvelopeFieldDeleteInternalServerError | 500                                           | application/json                              |
| models.APIError                               | 4XX, 5XX                                      | \*/\*                                         |