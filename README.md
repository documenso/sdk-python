# documenso_sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *documenso_sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=documenso-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/documenso-inc/api). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Documenso v2 beta API: Subject to breaking changes until v2 is fully released.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [documenso_sdk](#documensosdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

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

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import documenso_sdk
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find(order_by_direction=documenso_sdk.OrderByDirection.DESC)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import documenso_sdk
from documenso_sdk import Documenso
import os

async def main():
    async with Documenso(
        api_key=os.getenv("DOCUMENSO_API_KEY", ""),
    ) as documenso:

        res = await documenso.documents.find_async(order_by_direction=documenso_sdk.OrderByDirection.DESC)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type   | Scheme  | Environment Variable |
| --------- | ------ | ------- | -------------------- |
| `api_key` | apiKey | API key | `DOCUMENSO_API_KEY`  |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import documenso_sdk
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find(order_by_direction=documenso_sdk.OrderByDirection.DESC)

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

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

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import documenso_sdk
from documenso_sdk import Documenso
import os

with Documenso(
    server_url="https://app.documenso.com/api/v2-beta",
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.find(order_by_direction=documenso_sdk.OrderByDirection.DESC)

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from documenso_sdk import Documenso
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Documenso(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from documenso_sdk import Documenso
from documenso_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Documenso(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

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
