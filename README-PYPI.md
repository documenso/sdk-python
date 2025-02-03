<img src="https://github.com/documenso/documenso/assets/13398220/a643571f-0239-46a6-a73e-6bef38d1228b" alt="Documenso Logo">

&nbsp;

<div align="center">
    <a href="https://www.speakeasy.com/?utm_source=documenso-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

## Documenso Python SDK

A SDK for seamless integration with Documenso v2 API.

The full Documenso API can be viewed here (**todo**), which includes examples.

## ⚠️ Warning

Documenso v2 API and SDKs are currently in beta. There may be to breaking changes.

To keep updated, please follow the discussions and issues here:
- Discussion -> Todo
- Breaking change alerts -> Todo
<!-- No Summary [summary] -->

## Table of Contents
<!-- $toc-max-depth=2 -->
* [Overview](https://github.com/documenso/sdk-python/blob/master/#documenso-python-sdk)
  * [SDK Installation](https://github.com/documenso/sdk-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/documenso/sdk-python/blob/master/#ide-support)
  * [Authentication](https://github.com/documenso/sdk-python/blob/master/#authentication)
  * [Document creation example](https://github.com/documenso/sdk-python/blob/master/#document-creation-example)
  * [Available Resources and Operations](https://github.com/documenso/sdk-python/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/documenso/sdk-python/blob/master/#retries)
  * [Error Handling](https://github.com/documenso/sdk-python/blob/master/#error-handling)
  * [Debugging](https://github.com/documenso/sdk-python/blob/master/#debugging)
* [Development](https://github.com/documenso/sdk-python/blob/master/#development)
  * [Maturity](https://github.com/documenso/sdk-python/blob/master/#maturity)
  * [Contributions](https://github.com/documenso/sdk-python/blob/master/#contributions)

<!-- No Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/documenso/sdk-python.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/documenso/sdk-python.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from documenso_sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "documenso_sdk",
# ]
# ///

from documenso_sdk import Documenso

sdk = Documenso(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

## Authentication

To use the SDK, you will need a Documenso API key which can be created [here](https://docs.documenso.com/developers/public-api/authentication#creating-an-api-key
).

```python
import documenso_sdk
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:
```
<!-- No Authentication [security] -->

## Document creation example

Currently creating a document involves two steps:

1. Create the document
2. Upload the PDF

This is a temporary measure, in the near future prior to the full release we will merge these two tasks into one request. 

Here is a full example of the document creation process which you can copy and run.

Note that the function is temporarily called `createV0`, which will be replaced by `create` once we resolve the 2 step workaround.

```python
# Todo
```
<!-- No SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [documents](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md)

* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#find) - Find documents
* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#get) - Get document
* [create_v0](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#create_v0) - Create document
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#update) - Update document
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#delete) - Delete document
* [move_to_team](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#move_to_team) - Move document
* [distribute](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#distribute) - Distribute document
* [redistribute](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#redistribute) - Redistribute document
* [duplicate](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#duplicate) - Duplicate document

#### [documents.fields](https://github.com/documenso/sdk-python/blob/master/docs/sdks/fields/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/fields/README.md#get) - Get document field
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/fields/README.md#create) - Create document field
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/fields/README.md#create_many) - Create document fields
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/fields/README.md#update) - Update document field
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/fields/README.md#update_many) - Update document fields
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/fields/README.md#delete) - Delete document field

#### [documents.recipients](https://github.com/documenso/sdk-python/blob/master/docs/sdks/recipients/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/recipients/README.md#get) - Get document recipient
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/recipients/README.md#create) - Create document recipient
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/recipients/README.md#create_many) - Create document recipients
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/recipients/README.md#update) - Update document recipient
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/recipients/README.md#update_many) - Update document recipients
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/recipients/README.md#delete) - Delete document recipient

### [templates](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md)

* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#find) - Find templates
* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#get) - Get template
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#update) - Update template
* [duplicate](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#duplicate) - Duplicate template
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#delete) - Delete template
* [use](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#use) - Use template
* [move_to_team](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#move_to_team) - Move template

#### [templates.direct_link](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlink/README.md)

* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlink/README.md#create) - Create direct link
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlink/README.md#delete) - Delete direct link
* [toggle](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlink/README.md#toggle) - Toggle direct link

#### [templates.fields](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensofields/README.md)

* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensofields/README.md#create) - Create template field
* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensofields/README.md#get) - Get template field
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensofields/README.md#create_many) - Create template fields
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensofields/README.md#update) - Update template field
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensofields/README.md#update_many) - Update template fields
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensofields/README.md#delete) - Delete template field

#### [templates.recipients](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensorecipients/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensorecipients/README.md#get) - Get template recipient
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensorecipients/README.md#create) - Create template recipient
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensorecipients/README.md#create_many) - Create template recipients
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensorecipients/README.md#update) - Update template recipient
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensorecipients/README.md#update_many) - Update template recipients
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documensorecipients/README.md#delete) - Delete template recipient

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from documenso_sdk import Documenso
from documenso_sdk.utils import BackoffStrategy, RetryConfig
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from documenso_sdk import Documenso
from documenso_sdk.utils import BackoffStrategy, RetryConfig
import os

with Documenso(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `find_async` method may raise the following exceptions:

| Error Type                                                   | Status Code | Content Type     |
| ------------------------------------------------------------ | ----------- | ---------------- |
| models.DocumentFindDocumentsDocumentsResponseBody            | 400         | application/json |
| models.DocumentFindDocumentsDocumentsResponseResponseBody    | 404         | application/json |
| models.DocumentFindDocumentsDocumentsResponse500ResponseBody | 500         | application/json |
| models.APIError                                              | 4XX, 5XX    | \*/\*            |

### Example

```python
from documenso_sdk import Documenso, models
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:
    res = None
    try:

        res = documenso.documents.find()

        # Handle response
        print(res)

    except models.DocumentFindDocumentsDocumentsResponseBody as e:
        # handle e.data: models.DocumentFindDocumentsDocumentsResponseBodyData
        raise(e)
    except models.DocumentFindDocumentsDocumentsResponseResponseBody as e:
        # handle e.data: models.DocumentFindDocumentsDocumentsResponseResponseBodyData
        raise(e)
    except models.DocumentFindDocumentsDocumentsResponse500ResponseBody as e:
        # handle e.data: models.DocumentFindDocumentsDocumentsResponse500ResponseBodyData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- No Server Selection [server] -->
<!-- No Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Documenso` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from documenso_sdk import Documenso
import os
def main():
    with Documenso(
        api_key=os.getenv("DOCUMENSO_API_KEY", ""),
    ) as documenso:
        # Rest of application here...


# Or when using async:
async def amain():
    async with Documenso(
        api_key=os.getenv("DOCUMENSO_API_KEY", ""),
    ) as documenso:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from documenso_sdk import Documenso
import logging

logging.basicConfig(level=logging.DEBUG)
s = Documenso(debug_logger=logging.getLogger("documenso_sdk"))
```

You can also enable a default debug logger by setting an environment variable `DOCUMENSO_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=documenso-sdk&utm_campaign=python)
