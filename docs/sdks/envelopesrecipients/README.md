# Envelopes.Recipients

## Overview

### Available Operations

* [get](#get) - Get envelope recipient
* [create_many](#create_many) - Create envelope recipients
* [update_many](#update_many) - Update envelope recipients
* [delete](#delete) - Delete envelope recipient

## get

Returns an envelope recipient given an ID

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-recipient-get" method="get" path="/envelope/recipient/{recipientId}" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.recipients.get(recipient_id=8771.72)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeRecipientGetResponse](../../models/enveloperecipientgetresponse.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.EnvelopeRecipientGetBadRequestError     | 400                                            | application/json                               |
| models.EnvelopeRecipientGetUnauthorizedError   | 401                                            | application/json                               |
| models.EnvelopeRecipientGetForbiddenError      | 403                                            | application/json                               |
| models.EnvelopeRecipientGetNotFoundError       | 404                                            | application/json                               |
| models.EnvelopeRecipientGetInternalServerError | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## create_many

Create multiple recipients for an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-recipient-createMany" method="post" path="/envelope/recipient/create-many" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.recipients.create_many(envelope_id="<id>", data=[
        {
            "email": "Ed16@yahoo.com",
            "name": "<value>",
            "role": documenso_sdk.EnvelopeRecipientCreateManyRoleRequest.SIGNER,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `envelope_id`                                                                                                 | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `data`                                                                                                        | List[[models.EnvelopeRecipientCreateManyDataRequest](../../models/enveloperecipientcreatemanydatarequest.md)] | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.EnvelopeRecipientCreateManyResponse](../../models/enveloperecipientcreatemanyresponse.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.EnvelopeRecipientCreateManyBadRequestError     | 400                                                   | application/json                                      |
| models.EnvelopeRecipientCreateManyUnauthorizedError   | 401                                                   | application/json                                      |
| models.EnvelopeRecipientCreateManyForbiddenError      | 403                                                   | application/json                                      |
| models.EnvelopeRecipientCreateManyInternalServerError | 500                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## update_many

Update multiple recipients for an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-recipient-updateMany" method="post" path="/envelope/recipient/update-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.recipients.update_many(envelope_id="<id>", data=[
        {
            "id": 8894.57,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `envelope_id`                                                                                                 | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `data`                                                                                                        | List[[models.EnvelopeRecipientUpdateManyDataRequest](../../models/enveloperecipientupdatemanydatarequest.md)] | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.EnvelopeRecipientUpdateManyResponse](../../models/enveloperecipientupdatemanyresponse.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.EnvelopeRecipientUpdateManyBadRequestError     | 400                                                   | application/json                                      |
| models.EnvelopeRecipientUpdateManyUnauthorizedError   | 401                                                   | application/json                                      |
| models.EnvelopeRecipientUpdateManyForbiddenError      | 403                                                   | application/json                                      |
| models.EnvelopeRecipientUpdateManyInternalServerError | 500                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## delete

Delete an envelope recipient

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-recipient-delete" method="post" path="/envelope/recipient/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.recipients.delete(recipient_id=4834.93)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeRecipientDeleteResponse](../../models/enveloperecipientdeleteresponse.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.EnvelopeRecipientDeleteBadRequestError     | 400                                               | application/json                                  |
| models.EnvelopeRecipientDeleteUnauthorizedError   | 401                                               | application/json                                  |
| models.EnvelopeRecipientDeleteForbiddenError      | 403                                               | application/json                                  |
| models.EnvelopeRecipientDeleteInternalServerError | 500                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |