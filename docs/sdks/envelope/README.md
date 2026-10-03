# Envelope

## Overview

### Available Operations

* [envelope_find](#envelope_find) - Find envelopes
* [envelope_audit_log_find](#envelope_audit_log_find) - Get envelope audit logs
* [envelope_audit_log_download_pdf](#envelope_audit_log_download_pdf) - Download envelope audit log PDF
* [envelope_certificate_download_pdf](#envelope_certificate_download_pdf) - Download envelope certificate PDF
* [envelope_get_many](#envelope_get_many) - Get multiple envelopes
* [envelope_cancel](#envelope_cancel) - Cancel envelope

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

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `query`                                                                                               | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | The search query.                                                                                     |
| `page`                                                                                                | *Optional[float]*                                                                                     | :heavy_minus_sign:                                                                                    | The pagination page number, starts at 1.                                                              |
| `per_page`                                                                                            | *Optional[float]*                                                                                     | :heavy_minus_sign:                                                                                    | The number of items per page.                                                                         |
| `type`                                                                                                | [Optional[models.EnvelopeFindQueryParamType]](../../models/envelopefindqueryparamtype.md)             | :heavy_minus_sign:                                                                                    | Filter envelopes by type (DOCUMENT or TEMPLATE).                                                      |
| `template_id`                                                                                         | *Optional[float]*                                                                                     | :heavy_minus_sign:                                                                                    | Filter envelopes by the template ID used to create it.                                                |
| `source`                                                                                              | [Optional[models.EnvelopeFindQueryParamSource]](../../models/envelopefindqueryparamsource.md)         | :heavy_minus_sign:                                                                                    | Filter envelopes by how it was created.                                                               |
| `status`                                                                                              | [Optional[models.EnvelopeFindQueryParamStatus]](../../models/envelopefindqueryparamstatus.md)         | :heavy_minus_sign:                                                                                    | Filter envelopes by the current status.                                                               |
| `has_expired_recipients`                                                                              | [Optional[models.EnvelopeFindHasExpiredRecipients]](../../models/envelopefindhasexpiredrecipients.md) | :heavy_minus_sign:                                                                                    | Filter for envelopes that have at least one recipient whose signing link has expired.                 |
| `folder_id`                                                                                           | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Filter envelopes by folder ID.                                                                        |
| `order_by_column`                                                                                     | [Optional[models.EnvelopeFindOrderByColumn]](../../models/envelopefindorderbycolumn.md)               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `order_by_direction`                                                                                  | [Optional[models.EnvelopeFindOrderByDirection]](../../models/envelopefindorderbydirection.md)         | :heavy_minus_sign:                                                                                    | Sort direction.                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

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

## envelope_audit_log_download_pdf

Download the audit log for a document as a PDF.

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-auditLog-downloadPdf" method="get" path="/envelope/{envelopeId}/audit-log/download" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelope.envelope_audit_log_download_pdf(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the envelope to download the audit log for.               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeAuditLogDownloadPdfResponse](../../models/envelopeauditlogdownloadpdfresponse.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.EnvelopeAuditLogDownloadPdfBadRequestError     | 400                                                   | application/json                                      |
| models.EnvelopeAuditLogDownloadPdfUnauthorizedError   | 401                                                   | application/json                                      |
| models.EnvelopeAuditLogDownloadPdfForbiddenError      | 403                                                   | application/json                                      |
| models.EnvelopeAuditLogDownloadPdfNotFoundError       | 404                                                   | application/json                                      |
| models.EnvelopeAuditLogDownloadPdfInternalServerError | 500                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## envelope_certificate_download_pdf

Download the signing certificate for a completed document as a PDF.

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-certificate-downloadPdf" method="get" path="/envelope/{envelopeId}/certificate/download" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelope.envelope_certificate_download_pdf(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The ID of the envelope to download the certificate for.             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeCertificateDownloadPdfResponse](../../models/envelopecertificatedownloadpdfresponse.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| models.EnvelopeCertificateDownloadPdfBadRequestError     | 400                                                      | application/json                                         |
| models.EnvelopeCertificateDownloadPdfUnauthorizedError   | 401                                                      | application/json                                         |
| models.EnvelopeCertificateDownloadPdfForbiddenError      | 403                                                      | application/json                                         |
| models.EnvelopeCertificateDownloadPdfNotFoundError       | 404                                                      | application/json                                         |
| models.EnvelopeCertificateDownloadPdfInternalServerError | 500                                                      | application/json                                         |
| models.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |

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

## envelope_cancel

Cancel envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-cancel" method="post" path="/envelope/cancel" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelope.envelope_cancel(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeCancelResponse](../../models/envelopecancelresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.EnvelopeCancelBadRequestError     | 400                                      | application/json                         |
| models.EnvelopeCancelUnauthorizedError   | 401                                      | application/json                         |
| models.EnvelopeCancelForbiddenError      | 403                                      | application/json                         |
| models.EnvelopeCancelInternalServerError | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |