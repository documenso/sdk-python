# Embedding
(*embedding*)

## Overview

### Available Operations

* [embedding_presign_create_embedding_presign_token](#embedding_presign_create_embedding_presign_token) - Create embedding presign token
* [embedding_presign_verify_embedding_presign_token](#embedding_presign_verify_embedding_presign_token) - Verify embedding presign token

## embedding_presign_create_embedding_presign_token

Creates a presign token for embedding operations with configurable expiration time

### Example Usage

<!-- UsageSnippet language="python" operationID="embeddingPresign-createEmbeddingPresignToken" method="post" path="/embedding/create-presign-token" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.embedding.embedding_presign_create_embedding_presign_token(expires_in=60)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `expires_in`                                                        | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Expiration time in minutes (default: 60, max: 10,080)               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EmbeddingPresignCreateEmbeddingPresignTokenResponse](../../models/embeddingpresigncreateembeddingpresigntokenresponse.md)**

### Errors

| Error Type                                                            | Status Code                                                           | Content Type                                                          |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| models.EmbeddingPresignCreateEmbeddingPresignTokenBadRequestError     | 400                                                                   | application/json                                                      |
| models.EmbeddingPresignCreateEmbeddingPresignTokenInternalServerError | 500                                                                   | application/json                                                      |
| models.APIError                                                       | 4XX, 5XX                                                              | \*/\*                                                                 |

## embedding_presign_verify_embedding_presign_token

Verifies a presign token for embedding operations and returns the associated API token

### Example Usage

<!-- UsageSnippet language="python" operationID="embeddingPresign-verifyEmbeddingPresignToken" method="post" path="/embedding/verify-presign-token" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.embedding.embedding_presign_verify_embedding_presign_token(token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The presign token to verify                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EmbeddingPresignVerifyEmbeddingPresignTokenResponse](../../models/embeddingpresignverifyembeddingpresigntokenresponse.md)**

### Errors

| Error Type                                                            | Status Code                                                           | Content Type                                                          |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| models.EmbeddingPresignVerifyEmbeddingPresignTokenBadRequestError     | 400                                                                   | application/json                                                      |
| models.EmbeddingPresignVerifyEmbeddingPresignTokenInternalServerError | 500                                                                   | application/json                                                      |
| models.APIError                                                       | 4XX, 5XX                                                              | \*/\*                                                                 |