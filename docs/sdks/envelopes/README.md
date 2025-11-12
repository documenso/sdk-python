# Envelopes
(*envelopes*)

## Overview

### Available Operations

* [get](#get) - Get envelope
* [create](#create) - Create envelope
* [use](#use) - Use envelope
* [update](#update) - Update envelope
* [delete](#delete) - Delete envelope
* [duplicate](#duplicate) - Duplicate envelope
* [distribute](#distribute) - Distribute envelope
* [redistribute](#redistribute) - Redistribute envelope

## get

Returns an envelope given an ID

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-get" method="get" path="/envelope/{envelopeId}" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.get(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeGetResponse](../../models/envelopegetresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.EnvelopeGetBadRequestError     | 400                                   | application/json                      |
| models.EnvelopeGetUnauthorizedError   | 401                                   | application/json                      |
| models.EnvelopeGetForbiddenError      | 403                                   | application/json                      |
| models.EnvelopeGetNotFoundError       | 404                                   | application/json                      |
| models.EnvelopeGetInternalServerError | 500                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## create

Create an envelope using form data.

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-create" method="post" path="/envelope/create" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.create(payload={
        "title": "<value>",
        "type": documenso_sdk.EnvelopeCreateType.TEMPLATE,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `payload`                                                             | [models.EnvelopeCreatePayload](../../models/envelopecreatepayload.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `files`                                                               | List[[models.EnvelopeCreateFile](../../models/envelopecreatefile.md)] | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.EnvelopeCreateResponse](../../models/envelopecreateresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.EnvelopeCreateBadRequestError     | 400                                      | application/json                         |
| models.EnvelopeCreateUnauthorizedError   | 401                                      | application/json                         |
| models.EnvelopeCreateForbiddenError      | 403                                      | application/json                         |
| models.EnvelopeCreateInternalServerError | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## use

Create a document envelope from a template envelope. Upload custom files to replace the template PDFs and map them to specific envelope items using identifiers.

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-use" method="post" path="/envelope/use" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.use(payload={
        "envelope_id": "<id>",
        "recipients": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payload`                                                           | [models.EnvelopeUsePayload](../../models/envelopeusepayload.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `files`                                                             | List[[models.EnvelopeUseFile](../../models/envelopeusefile.md)]     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeUseResponse](../../models/envelopeuseresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.EnvelopeUseBadRequestError     | 400                                   | application/json                      |
| models.EnvelopeUseUnauthorizedError   | 401                                   | application/json                      |
| models.EnvelopeUseForbiddenError      | 403                                   | application/json                      |
| models.EnvelopeUseInternalServerError | 500                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## update

Update envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-update" method="post" path="/envelope/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.update(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `envelope_id`                                                             | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `data`                                                                    | [Optional[models.EnvelopeUpdateData]](../../models/envelopeupdatedata.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `meta`                                                                    | [Optional[models.EnvelopeUpdateMeta]](../../models/envelopeupdatemeta.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.EnvelopeUpdateResponse](../../models/envelopeupdateresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.EnvelopeUpdateBadRequestError     | 400                                      | application/json                         |
| models.EnvelopeUpdateUnauthorizedError   | 401                                      | application/json                         |
| models.EnvelopeUpdateForbiddenError      | 403                                      | application/json                         |
| models.EnvelopeUpdateInternalServerError | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## delete

Delete envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-delete" method="post" path="/envelope/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.delete(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeDeleteResponse](../../models/envelopedeleteresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.EnvelopeDeleteBadRequestError     | 400                                      | application/json                         |
| models.EnvelopeDeleteUnauthorizedError   | 401                                      | application/json                         |
| models.EnvelopeDeleteForbiddenError      | 403                                      | application/json                         |
| models.EnvelopeDeleteInternalServerError | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## duplicate

Duplicate an envelope with all its settings

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-duplicate" method="post" path="/envelope/duplicate" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.duplicate(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeDuplicateResponse](../../models/envelopeduplicateresponse.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.EnvelopeDuplicateBadRequestError     | 400                                         | application/json                            |
| models.EnvelopeDuplicateUnauthorizedError   | 401                                         | application/json                            |
| models.EnvelopeDuplicateForbiddenError      | 403                                         | application/json                            |
| models.EnvelopeDuplicateInternalServerError | 500                                         | application/json                            |
| models.APIError                             | 4XX, 5XX                                    | \*/\*                                       |

## distribute

Send the envelope to recipients based on your distribution method

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-distribute" method="post" path="/envelope/distribute" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.distribute(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `envelope_id`                                                                     | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `meta`                                                                            | [Optional[models.EnvelopeDistributeMeta]](../../models/envelopedistributemeta.md) | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EnvelopeDistributeResponse](../../models/envelopedistributeresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.EnvelopeDistributeBadRequestError     | 400                                          | application/json                             |
| models.EnvelopeDistributeUnauthorizedError   | 401                                          | application/json                             |
| models.EnvelopeDistributeForbiddenError      | 403                                          | application/json                             |
| models.EnvelopeDistributeInternalServerError | 500                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## redistribute

Redistribute the envelope to the provided recipients who have not actioned the envelope. Will use the distribution method set in the envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-redistribute" method="post" path="/envelope/redistribute" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.redistribute(envelope_id="<id>", recipients=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `recipients`                                                        | List[*float*]                                                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeRedistributeResponse](../../models/enveloperedistributeresponse.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.EnvelopeRedistributeBadRequestError     | 400                                            | application/json                               |
| models.EnvelopeRedistributeUnauthorizedError   | 401                                            | application/json                               |
| models.EnvelopeRedistributeForbiddenError      | 403                                            | application/json                               |
| models.EnvelopeRedistributeInternalServerError | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |