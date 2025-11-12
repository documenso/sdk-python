# Folders
(*folders*)

## Overview

### Available Operations

* [find](#find) - Find folders
* [create](#create) - Create new folder
* [update](#update) - Update folder
* [delete](#delete) - Delete folder

## find

Find folders based on a search criteria

### Example Usage

<!-- UsageSnippet language="python" operationID="folder-findFolders" method="get" path="/folder" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.folders.find()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `query`                                                                                             | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | The search query.                                                                                   |
| `page`                                                                                              | *Optional[float]*                                                                                   | :heavy_minus_sign:                                                                                  | The pagination page number, starts at 1.                                                            |
| `per_page`                                                                                          | *Optional[float]*                                                                                   | :heavy_minus_sign:                                                                                  | The number of items per page.                                                                       |
| `parent_id`                                                                                         | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `type`                                                                                              | [Optional[models.FolderFindFoldersQueryParamType]](../../models/folderfindfoldersqueryparamtype.md) | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.FolderFindFoldersResponse](../../models/folderfindfoldersresponse.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.FolderFindFoldersBadRequestError     | 400                                         | application/json                            |
| models.FolderFindFoldersUnauthorizedError   | 401                                         | application/json                            |
| models.FolderFindFoldersForbiddenError      | 403                                         | application/json                            |
| models.FolderFindFoldersNotFoundError       | 404                                         | application/json                            |
| models.FolderFindFoldersInternalServerError | 500                                         | application/json                            |
| models.APIError                             | 4XX, 5XX                                    | \*/\*                                       |

## create

Creates a new folder in your team

### Example Usage

<!-- UsageSnippet language="python" operationID="folder-createFolder" method="post" path="/folder/create" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.folders.create(name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `name`                                                                                          | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `parent_id`                                                                                     | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `type`                                                                                          | [Optional[models.FolderCreateFolderTypeRequest]](../../models/foldercreatefoldertyperequest.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.FolderCreateFolderResponse](../../models/foldercreatefolderresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.FolderCreateFolderBadRequestError     | 400                                          | application/json                             |
| models.FolderCreateFolderUnauthorizedError   | 401                                          | application/json                             |
| models.FolderCreateFolderForbiddenError      | 403                                          | application/json                             |
| models.FolderCreateFolderInternalServerError | 500                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## update

Updates an existing folder

### Example Usage

<!-- UsageSnippet language="python" operationID="folder-updateFolder" method="post" path="/folder/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.folders.update(folder_id="<id>", data={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `folder_id`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `data`                                                                  | [models.FolderUpdateFolderData](../../models/folderupdatefolderdata.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.FolderUpdateFolderResponse](../../models/folderupdatefolderresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.FolderUpdateFolderBadRequestError     | 400                                          | application/json                             |
| models.FolderUpdateFolderUnauthorizedError   | 401                                          | application/json                             |
| models.FolderUpdateFolderForbiddenError      | 403                                          | application/json                             |
| models.FolderUpdateFolderInternalServerError | 500                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## delete

Deletes an existing folder

### Example Usage

<!-- UsageSnippet language="python" operationID="folder-deleteFolder" method="post" path="/folder/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.folders.delete(folder_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FolderDeleteFolderResponse](../../models/folderdeletefolderresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.FolderDeleteFolderBadRequestError     | 400                                          | application/json                             |
| models.FolderDeleteFolderUnauthorizedError   | 401                                          | application/json                             |
| models.FolderDeleteFolderForbiddenError      | 403                                          | application/json                             |
| models.FolderDeleteFolderInternalServerError | 500                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |