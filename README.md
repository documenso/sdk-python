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
* [Overview](#documenso-python-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [Authentication](#authentication)
  * [Document creation example](#document-creation-example)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- No Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```
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


### [documents](docs/sdks/documents/README.md)

* [find](docs/sdks/documents/README.md#find) - Find documents
* [get](docs/sdks/documents/README.md#get) - Get document
* [create_v0](docs/sdks/documents/README.md#create_v0) - Create document
* [update](docs/sdks/documents/README.md#update) - Update document
* [delete](docs/sdks/documents/README.md#delete) - Delete document
* [move_to_team](docs/sdks/documents/README.md#move_to_team) - Move document
* [distribute](docs/sdks/documents/README.md#distribute) - Distribute document
* [redistribute](docs/sdks/documents/README.md#redistribute) - Redistribute document
* [duplicate](docs/sdks/documents/README.md#duplicate) - Duplicate document

#### [documents.fields](docs/sdks/fields/README.md)

* [get](docs/sdks/fields/README.md#get) - Get document field
* [create](docs/sdks/fields/README.md#create) - Create document field
* [create_many](docs/sdks/fields/README.md#create_many) - Create document fields
* [update](docs/sdks/fields/README.md#update) - Update document field
* [update_many](docs/sdks/fields/README.md#update_many) - Update document fields
* [delete](docs/sdks/fields/README.md#delete) - Delete document field

#### [documents.recipients](docs/sdks/recipients/README.md)

* [get](docs/sdks/recipients/README.md#get) - Get document recipient
* [create](docs/sdks/recipients/README.md#create) - Create document recipient
* [create_many](docs/sdks/recipients/README.md#create_many) - Create document recipients
* [update](docs/sdks/recipients/README.md#update) - Update document recipient
* [update_many](docs/sdks/recipients/README.md#update_many) - Update document recipients
* [delete](docs/sdks/recipients/README.md#delete) - Delete document recipient

### [templates](docs/sdks/templates/README.md)

* [find](docs/sdks/templates/README.md#find) - Find templates
* [get](docs/sdks/templates/README.md#get) - Get template
* [update](docs/sdks/templates/README.md#update) - Update template
* [duplicate](docs/sdks/templates/README.md#duplicate) - Duplicate template
* [delete](docs/sdks/templates/README.md#delete) - Delete template
* [use](docs/sdks/templates/README.md#use) - Use template
* [move_to_team](docs/sdks/templates/README.md#move_to_team) - Move template

#### [templates.direct_link](docs/sdks/directlink/README.md)

* [create](docs/sdks/directlink/README.md#create) - Create direct link
* [delete](docs/sdks/directlink/README.md#delete) - Delete direct link
* [toggle](docs/sdks/directlink/README.md#toggle) - Toggle direct link

#### [templates.fields](docs/sdks/documensofields/README.md)

* [create](docs/sdks/documensofields/README.md#create) - Create template field
* [get](docs/sdks/documensofields/README.md#get) - Get template field
* [create_many](docs/sdks/documensofields/README.md#create_many) - Create template fields
* [update](docs/sdks/documensofields/README.md#update) - Update template field
* [update_many](docs/sdks/documensofields/README.md#update_many) - Update template fields
* [delete](docs/sdks/documensofields/README.md#delete) - Delete template field

#### [templates.recipients](docs/sdks/documensorecipients/README.md)

* [get](docs/sdks/documensorecipients/README.md#get) - Get template recipient
* [create](docs/sdks/documensorecipients/README.md#create) - Create template recipient
* [create_many](docs/sdks/documensorecipients/README.md#create_many) - Create template recipients
* [update](docs/sdks/documensorecipients/README.md#update) - Update template recipient
* [update_many](docs/sdks/documensorecipients/README.md#update_many) - Update template recipients
* [delete](docs/sdks/documensorecipients/README.md#delete) - Delete template recipient

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import documenso_sdk
from documenso_sdk import Documenso
from documenso_sdk.utils import BackoffStrategy, RetryConfig
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find(order_by_direction=documenso_sdk.OrderByDirection.DESC,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import documenso_sdk
from documenso_sdk import Documenso
from documenso_sdk.utils import BackoffStrategy, RetryConfig
import os

with Documenso(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find(order_by_direction=documenso_sdk.OrderByDirection.DESC)

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

| Error Type                      | Status Code | Content Type     |
| ------------------------------- | ----------- | ---------------- |
| models.ErrorBADREQUEST          | 400         | application/json |
| models.ErrorNOTFOUND            | 404         | application/json |
| models.ERRORINTERNALSERVERERROR | 500         | application/json |
| models.APIError                 | 4XX, 5XX    | \*/\*            |

### Example

```python
import documenso_sdk
from documenso_sdk import Documenso, models
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:
    res = None
    try:

        res = documenso.documents.find(order_by_direction=documenso_sdk.OrderByDirection.DESC)

        # Handle response
        print(res)

    except models.ErrorBADREQUEST as e:
        # handle e.data: models.ErrorBADREQUESTData
        raise(e)
    except models.ErrorNOTFOUND as e:
        # handle e.data: models.ErrorNOTFOUNDData
        raise(e)
    except models.ERRORINTERNALSERVERERROR as e:
        # handle e.data: models.ERRORINTERNALSERVERERRORData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- No Server Selection [server] -->
<!-- No Custom HTTP Client [http-client] -->

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
