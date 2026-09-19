# EnvelopeRecipients

## Overview

### Available Operations

* [envelope_recipient_reject_on_behalf_of](#envelope_recipient_reject_on_behalf_of) - Reject envelope recipient on behalf of

## envelope_recipient_reject_on_behalf_of

Records a rejection on behalf of a recipient. Use this when a recipient has declined to sign outside of the platform. The rejection is flagged as external in the document audit log. By default the action is attributed to the API user; supply `actAsEmail` to attribute it to a specific team member.

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-recipient-rejectOnBehalfOf" method="post" path="/envelope/recipient/{recipientId}/reject" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelope_recipients.envelope_recipient_reject_on_behalf_of(recipient_id=51.94, envelope_id="<id>", reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | The ID of the recipient to reject the document on behalf of.        |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reason`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `act_as_email`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeRecipientRejectOnBehalfOfResponse](../../models/enveloperecipientrejectonbehalfofresponse.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| models.EnvelopeRecipientRejectOnBehalfOfBadRequestError     | 400                                                         | application/json                                            |
| models.EnvelopeRecipientRejectOnBehalfOfUnauthorizedError   | 401                                                         | application/json                                            |
| models.EnvelopeRecipientRejectOnBehalfOfForbiddenError      | 403                                                         | application/json                                            |
| models.EnvelopeRecipientRejectOnBehalfOfInternalServerError | 500                                                         | application/json                                            |
| models.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |