# Envelope

## Overview

### Available Operations

* [envelope_find](#envelope_find) - Find envelopes
* [envelope_audit_log_find](#envelope_audit_log_find) - Get envelope audit logs
* [envelope_get_many](#envelope_get_many) - Get multiple envelopes

## envelope_find

Find envelopes based on search criteria

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-find" method="get" path="/envelope" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelope.envelope_find(order_by_direction=documenso_sdk.EnvelopeFindOrderByDirection.DESC)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `query`                                                                                       | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | The search query.                                                                             |
| `page`                                                                                        | *Optional[float]*                                                                             | :heavy_minus_sign:                                                                            | The pagination page number, starts at 1.                                                      |
| `per_page`                                                                                    | *Optional[float]*                                                                             | :heavy_minus_sign:                                                                            | The number of items per page.                                                                 |
| `type`                                                                                        | [Optional[models.EnvelopeFindQueryParamType]](../../models/envelopefindqueryparamtype.md)     | :heavy_minus_sign:                                                                            | Filter envelopes by type (DOCUMENT or TEMPLATE).                                              |
| `template_id`                                                                                 | *Optional[float]*                                                                             | :heavy_minus_sign:                                                                            | Filter envelopes by the template ID used to create it.                                        |
| `source`                                                                                      | [Optional[models.EnvelopeFindQueryParamSource]](../../models/envelopefindqueryparamsource.md) | :heavy_minus_sign:                                                                            | Filter envelopes by how it was created.                                                       |
| `status`                                                                                      | [Optional[models.EnvelopeFindQueryParamStatus]](../../models/envelopefindqueryparamstatus.md) | :heavy_minus_sign:                                                                            | Filter envelopes by the current status.                                                       |
| `folder_id`                                                                                   | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | Filter envelopes by folder ID.                                                                |
| `order_by_column`                                                                             | [Optional[models.EnvelopeFindOrderByColumn]](../../models/envelopefindorderbycolumn.md)       | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `order_by_direction`                                                                          | [Optional[models.EnvelopeFindOrderByDirection]](../../models/envelopefindorderbydirection.md) | :heavy_minus_sign:                                                                            | Sort direction.                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.EnvelopeFindResponse](../../models/envelopefindresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.EnvelopeFindBadRequestError     | 400                                    | application/json                       |
| models.EnvelopeFindUnauthorizedError   | 401                                    | application/json                       |
| models.EnvelopeFindForbiddenError      | 403                                    | application/json                       |
| models.EnvelopeFindNotFoundError       | 404                                    | application/json                       |
| models.EnvelopeFindInternalServerError | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## envelope_audit_log_find

Find audit logs based on a search criteria

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-auditLog-find" method="get" path="/envelope/{envelopeId}/audit-log" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelope.envelope_audit_log_find(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `envelope_id`                                                                                                 | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Envelope ID                                                                                                   |
| `page`                                                                                                        | *Optional[float]*                                                                                             | :heavy_minus_sign:                                                                                            | The pagination page number, starts at 1.                                                                      |
| `per_page`                                                                                                    | *Optional[float]*                                                                                             | :heavy_minus_sign:                                                                                            | The number of items per page.                                                                                 |
| `order_by_column`                                                                                             | [Optional[models.EnvelopeAuditLogFindOrderByColumn]](../../models/envelopeauditlogfindorderbycolumn.md)       | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `order_by_direction`                                                                                          | [Optional[models.EnvelopeAuditLogFindOrderByDirection]](../../models/envelopeauditlogfindorderbydirection.md) | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.EnvelopeAuditLogFindResponse](../../models/envelopeauditlogfindresponse.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.EnvelopeAuditLogFindBadRequestError     | 400                                            | application/json                               |
| models.EnvelopeAuditLogFindUnauthorizedError   | 401                                            | application/json                               |
| models.EnvelopeAuditLogFindForbiddenError      | 403                                            | application/json                               |
| models.EnvelopeAuditLogFindNotFoundError       | 404                                            | application/json                               |
| models.EnvelopeAuditLogFindInternalServerError | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## envelope_get_many

Retrieve multiple envelopes by their IDs

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-getMany" method="post" path="/envelope/get-many" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelope.envelope_get_many(ids={
        "type": documenso_sdk.TypeEnvelopeID.ENVELOPE_ID,
        "ids": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | [models.Ids](../../models/ids.md)                                   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeGetManyResponse](../../models/envelopegetmanyresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| models.EnvelopeGetManyBadRequestError     | 400                                       | application/json                          |
| models.EnvelopeGetManyUnauthorizedError   | 401                                       | application/json                          |
| models.EnvelopeGetManyForbiddenError      | 403                                       | application/json                          |
| models.EnvelopeGetManyInternalServerError | 500                                       | application/json                          |
| models.APIError                           | 4XX, 5XX                                  | \*/\*                                     |