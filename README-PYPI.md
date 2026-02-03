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

The full Documenso API can be viewed [here](https://openapi.documenso.com/), which includes examples.

## ⚠️ Warning

Documenso v2 API and SDKs are currently in beta. There may be to breaking changes.

To keep updated, please follow the discussions here:

- [Feedback](https://github.com/documenso/documenso/discussions/1611)
- [Breaking change alerts](https://github.com/documenso/documenso/discussions/1612)
<!-- No Summary [summary] -->

## Table of Contents

<!-- $toc-max-depth=2 -->

- [Overview](https://github.com/documenso/sdk-python/blob/master/#documenso-python-sdk)
  - [SDK Installation](https://github.com/documenso/sdk-python/blob/master/#sdk-installation)
  - [IDE Support](https://github.com/documenso/sdk-python/blob/master/#ide-support)
  - [Authentication](https://github.com/documenso/sdk-python/blob/master/#authentication)
  - [Document creation example](https://github.com/documenso/sdk-python/blob/master/#document-creation-example)
  - [Available Resources and Operations](https://github.com/documenso/sdk-python/blob/master/#available-resources-and-operations)
  - [Retries](https://github.com/documenso/sdk-python/blob/master/#retries)
  - [Error Handling](https://github.com/documenso/sdk-python/blob/master/#error-handling)
  - [Debugging](https://github.com/documenso/sdk-python/blob/master/#debugging)
- [Development](https://github.com/documenso/sdk-python/blob/master/#development)
  - [Maturity](https://github.com/documenso/sdk-python/blob/master/#maturity)
  - [Contributions](https://github.com/documenso/sdk-python/blob/master/#contributions)

<!-- No Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add documenso_sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install documenso_sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add documenso_sdk
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

To use the SDK, you will need a Documenso API key which can be created [here](https://docs.documenso.com/developers/public-api/authentication#creating-an-api-key).

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

Note that the function is temporarily called `create_v0`, which will be replaced by `create` once we resolve the 2 step workaround.

```python
from documenso_sdk import Documenso
import os
import requests

def upload_file_to_presigned_url(file_path: str, upload_url: str):
  """Upload a file to a pre-signed URL."""
  with open(file_path, 'rb') as file:
      file_content = file.read()

  response = requests.put(
      upload_url,
      data=file_content,
      headers={"Content-Type": "application/octet-stream"}
  )

  if not response.ok:
      raise Exception(f"Upload failed with status: {response.status_code}")

async def main():
  with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
  ) as documenso:

    # Create document with recipients and fields
    create_document_response = documenso.documents.create_v0(
      title="Document title",
      recipients=[
        {
          "email": "example@documenso.com",
          "name": "Example Doe",
          "role": "SIGNER",
          "fields": [
            {
              "type": "SIGNATURE",
              "pageNumber": 1,
              "pageX": 10,
              "pageY": 10,
              "width": 10,
              "height": 10
            },
              {
                "type": "INITIALS",
                "pageNumber": 1,
                "pageX": 20,
                "pageY": 20,
                "width": 10,
                "height": 10
            }
          ]
        },
        {
          "email": "admin@documenso.com",
          "name": "Admin Doe",
          "role": "APPROVER",
          "fields": [
            {
              "type": "SIGNATURE",
              "pageNumber": 1,
              "pageX": 10,
              "pageY": 50,
              "width": 10,
              "height": 10
            }
          ]
        }
      ],
      meta={
        "timezone": "Australia/Melbourne",
        "dateFormat": "MM/dd/yyyy hh:mm a",
        "language": "de",
        "subject": "Email subject",
        "message": "Email message",
        "emailSettings": {
            "recipientRemoved": False
        }
      }
    )

    # Upload the PDF file
    upload_file_to_presigned_url("./demo.pdf", create_document_response.upload_url)


if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
```

<!-- No SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Document](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsdk/README.md)

* [document_get_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsdk/README.md#document_get_many) - Get multiple documents
* [document_download](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsdk/README.md#document_download) - Download document (beta)

### [Documents](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#get) - Get document
* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#find) - Find documents
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#create) - Create document
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#update) - Update document
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#delete) - Delete document
* [duplicate](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#duplicate) - Duplicate document
* [distribute](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#distribute) - Distribute document
* [redistribute](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#redistribute) - Redistribute document
* [download](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#download) - Download document
* [create_v0](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#create_v0) - Create document

#### [Documents.Attachments](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsattachments/README.md)

* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsattachments/README.md#create) - Create attachment
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsattachments/README.md#update) - Update attachment
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsattachments/README.md#delete) - Delete attachment
* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsattachments/README.md#find) - Find attachments

#### [Documents.Fields](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#get) - Get document field
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#create) - Create document field
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#create_many) - Create document fields
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#update) - Update document field
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#update_many) - Update document fields
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#delete) - Delete document field

#### [Documents.Recipients](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#get) - Get document recipient
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#create) - Create document recipient
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#create_many) - Create document recipients
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#update) - Update document recipient
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#update_many) - Update document recipients
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#delete) - Delete document recipient

### [Embedding](https://github.com/documenso/sdk-python/blob/master/docs/sdks/embedding/README.md)

* [embedding_presign_create_embedding_presign_token](https://github.com/documenso/sdk-python/blob/master/docs/sdks/embedding/README.md#embedding_presign_create_embedding_presign_token) - Create embedding presign token
* [embedding_presign_verify_embedding_presign_token](https://github.com/documenso/sdk-python/blob/master/docs/sdks/embedding/README.md#embedding_presign_verify_embedding_presign_token) - Verify embedding presign token

### [Envelope](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelope/README.md)

* [envelope_find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelope/README.md#envelope_find) - Find envelopes
* [envelope_audit_log_find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelope/README.md#envelope_audit_log_find) - Get envelope audit logs
* [envelope_get_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelope/README.md#envelope_get_many) - Get multiple envelopes

### [Envelopes](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md#get) - Get envelope
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md#create) - Create envelope
* [use](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md#use) - Use envelope
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md#update) - Update envelope
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md#delete) - Delete envelope
* [duplicate](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md#duplicate) - Duplicate envelope
* [distribute](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md#distribute) - Distribute envelope
* [redistribute](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopes/README.md#redistribute) - Redistribute envelope

#### [Envelopes.Attachments](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesattachments/README.md)

* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesattachments/README.md#find) - Find attachments
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesattachments/README.md#create) - Create attachment
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesattachments/README.md#update) - Update attachment
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesattachments/README.md#delete) - Delete attachment

#### [Envelopes.Fields](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesfields/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesfields/README.md#get) - Get envelope field
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesfields/README.md#create_many) - Create envelope fields
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesfields/README.md#update_many) - Update envelope fields
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesfields/README.md#delete) - Delete envelope field

#### [Envelopes.Items](https://github.com/documenso/sdk-python/blob/master/docs/sdks/items/README.md)

* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/items/README.md#create_many) - Create envelope items
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/items/README.md#update_many) - Update envelope items
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/items/README.md#delete) - Delete envelope item
* [download](https://github.com/documenso/sdk-python/blob/master/docs/sdks/items/README.md#download) - Download an envelope item

#### [Envelopes.Recipients](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesrecipients/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesrecipients/README.md#get) - Get envelope recipient
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesrecipients/README.md#create_many) - Create envelope recipients
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesrecipients/README.md#update_many) - Update envelope recipients
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/envelopesrecipients/README.md#delete) - Delete envelope recipient

### [Folders](https://github.com/documenso/sdk-python/blob/master/docs/sdks/folders/README.md)

* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/folders/README.md#find) - Find folders
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/folders/README.md#create) - Create new folder
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/folders/README.md#update) - Update folder
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/folders/README.md#delete) - Delete folder

### [Template](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesdk/README.md)

* [template_get_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesdk/README.md#template_get_many) - Get multiple templates
* [template_create_template_temporary](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesdk/README.md#template_create_template_temporary) - Create template

### [Templates](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md)

* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#find) - Find templates
* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#get) - Get template
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#create) - Create template
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#update) - Update template
* [duplicate](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#duplicate) - Duplicate template
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#delete) - Delete template
* [use](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#use) - Use template

#### [Templates.DirectLink](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlinksdk/README.md)

* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlinksdk/README.md#create) - Create direct link
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlinksdk/README.md#delete) - Delete direct link
* [toggle](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlinksdk/README.md#toggle) - Toggle direct link

#### [Templates.Fields](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md)

* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#create) - Create template field
* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#get) - Get template field
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#create_many) - Create template fields
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#update) - Update template field
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#update_many) - Update template fields
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#delete) - Delete template field

#### [Templates.Recipients](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#get) - Get template recipient
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#create) - Create template recipient
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#create_many) - Create template recipients
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#update) - Update template recipient
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#update_many) - Update template recipients
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#delete) - Delete template recipient

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

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
<!-- End File uploads [file-upload] -->

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

    res = documenso.envelopes.get(envelope_id="<id>",
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

    res = documenso.envelopes.get(envelope_id="<id>")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`DocumensoError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documensoerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/documenso/sdk-python/blob/master/#error-classes). |

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

        res = documenso.envelopes.get(envelope_id="<id>")

        # Handle response
        print(res)


    except models.DocumensoError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.EnvelopeGetBadRequestError):
            print(e.data.message)  # str
            print(e.data.code)  # str
            print(e.data.issues)  # Optional[List[documenso_sdk.EnvelopeGetBadRequestIssue]]
```

### Error Classes
**Primary error:**
* [`DocumensoError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documensoerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (364)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`DocumensoError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documensoerror.py)**:
* [`EnvelopeGetBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeCreateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopecreatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeUseBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeusebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeUpdateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeupdatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeDeleteBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopedeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeDuplicateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeduplicatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeDistributeBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopedistributebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeRedistributeBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperedistributebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeFindBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeAuditLogFindBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeauditlogfindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeGetManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetmanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentGetBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentFindBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentfindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentCreateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentUpdateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentupdatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentDeleteBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentDuplicateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentduplicatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentDistributeBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdistributebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentRedistributeBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentredistributebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentCreateDocumentTemporaryBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreatedocumenttemporarybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentGetManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetmanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadBetaBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadbetabadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateFindTemplatesBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatefindtemplatesbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateGetTemplateByIDBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategettemplatebyidbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateUpdateTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateupdatetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateDuplicateTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateduplicatetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateDeleteTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateCreateDocumentFromTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatedocumentfromtemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FolderFindFoldersBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderfindfoldersbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FolderCreateFolderBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/foldercreatefolderbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FolderUpdateFolderBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderupdatefolderbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FolderDeleteFolderBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderdeletefolderbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateGetManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategetmanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateTemporaryBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatetemporarybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokenbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokenbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentFindBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentfindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentCreateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentcreatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentUpdateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentupdatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentDeleteBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemCreateManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemcreatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemUpdateManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemupdatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDeleteBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDownloadBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdownloadbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientGetBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientgetbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientCreateManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientcreatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientUpdateManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientupdatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientDeleteBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldGetBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldgetbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldCreateManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldcreatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldUpdateManyBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldupdatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldDeleteBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefielddeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentCreateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentcreatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentUpdateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentupdatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentDeleteBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentFindBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentfindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldGetDocumentFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgetdocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldCreateDocumentFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldCreateDocumentFieldsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldUpdateDocumentFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldUpdateDocumentFieldsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldDeleteDocumentFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientGetDocumentRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgetdocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientCreateDocumentRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientCreateDocumentRecipientsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateDocumentRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateDocumentRecipientsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientDeleteDocumentRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldCreateTemplateFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldGetTemplateFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgettemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldCreateTemplateFieldsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldUpdateTemplateFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldUpdateTemplateFieldsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`FieldDeleteTemplateFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientGetTemplateRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgettemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientCreateTemplateRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientCreateTemplateRecipientsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateTemplateRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateTemplateRecipientsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`RecipientDeleteTemplateRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateDirectLinkBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateDeleteTemplateDirectLinkBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`TemplateToggleTemplateDirectLinkBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatetoggletemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 85 methods.*
* [`EnvelopeGetUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeCreateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopecreateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeUseUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeuseunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeUpdateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeupdateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeDeleteUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopedeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeDuplicateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeduplicateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeDistributeUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopedistributeunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeRedistributeUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperedistributeunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeFindUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeAuditLogFindUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeauditlogfindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeGetManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetmanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentGetUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentFindUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentfindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentCreateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentUpdateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentupdateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentDeleteUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentDuplicateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentduplicateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentDistributeUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdistributeunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentRedistributeUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentredistributeunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentCreateDocumentTemporaryUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreatedocumenttemporaryunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentGetManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetmanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadBetaUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadbetaunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateFindTemplatesUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatefindtemplatesunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateGetTemplateByIDUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategettemplatebyidunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateUpdateTemplateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateupdatetemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateDuplicateTemplateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateduplicatetemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateDeleteTemplateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateCreateDocumentFromTemplateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatedocumentfromtemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FolderFindFoldersUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderfindfoldersunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FolderCreateFolderUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/foldercreatefolderunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FolderUpdateFolderUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderupdatefolderunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FolderDeleteFolderUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderdeletefolderunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateGetManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategetmanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateTemporaryUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatetemporaryunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokenunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokenunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentFindUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentfindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentCreateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentcreateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentUpdateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentupdateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentDeleteUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemCreateManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemcreatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemUpdateManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemupdatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDeleteUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDownloadUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdownloadunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientGetUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientgetunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientCreateManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientcreatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientUpdateManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientupdatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientDeleteUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldGetUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldgetunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldCreateManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldcreatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldUpdateManyUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldupdatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldDeleteUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefielddeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentCreateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentcreateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentUpdateUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentupdateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentDeleteUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentFindUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentfindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldGetDocumentFieldUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgetdocumentfieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldCreateDocumentFieldUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldCreateDocumentFieldsUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldUpdateDocumentFieldUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldUpdateDocumentFieldsUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldDeleteDocumentFieldUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletedocumentfieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientGetDocumentRecipientUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgetdocumentrecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientCreateDocumentRecipientUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientCreateDocumentRecipientsUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateDocumentRecipientUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateDocumentRecipientsUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientDeleteDocumentRecipientUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletedocumentrecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldCreateTemplateFieldUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldGetTemplateFieldUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgettemplatefieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldCreateTemplateFieldsUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldUpdateTemplateFieldUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldUpdateTemplateFieldsUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`FieldDeleteTemplateFieldUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletetemplatefieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientGetTemplateRecipientUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgettemplaterecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientCreateTemplateRecipientUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientCreateTemplateRecipientsUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateTemplateRecipientUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateTemplateRecipientsUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`RecipientDeleteTemplateRecipientUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletetemplaterecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateDirectLinkUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatedirectlinkunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateDeleteTemplateDirectLinkUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplatedirectlinkunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`TemplateToggleTemplateDirectLinkUnauthorizedError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatetoggletemplatedirectlinkunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 85 methods.*
* [`EnvelopeGetForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeCreateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopecreateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeUseForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeuseforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeUpdateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeupdateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeDeleteForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopedeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeDuplicateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeduplicateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeDistributeForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopedistributeforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeRedistributeForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperedistributeforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeFindForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeAuditLogFindForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeauditlogfindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeGetManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetmanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentGetForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentFindForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentfindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentCreateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentUpdateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentupdateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentDeleteForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentDuplicateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentduplicateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentDistributeForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdistributeforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentRedistributeForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentredistributeforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentCreateDocumentTemporaryForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreatedocumenttemporaryforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentGetManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetmanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadBetaForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadbetaforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateFindTemplatesForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatefindtemplatesforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateGetTemplateByIDForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategettemplatebyidforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateUpdateTemplateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateupdatetemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateDuplicateTemplateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateduplicatetemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateDeleteTemplateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateCreateDocumentFromTemplateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatedocumentfromtemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FolderFindFoldersForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderfindfoldersforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FolderCreateFolderForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/foldercreatefolderforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FolderUpdateFolderForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderupdatefolderforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FolderDeleteFolderForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderdeletefolderforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateGetManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategetmanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateTemporaryForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatetemporaryforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokenforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokenforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentFindForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentfindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentCreateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentcreateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentUpdateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentupdateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentDeleteForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemCreateManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemcreatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemUpdateManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemupdatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDeleteForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDownloadForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdownloadforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientGetForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientgetforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientCreateManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientcreatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientUpdateManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientupdatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientDeleteForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldGetForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldgetforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldCreateManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldcreatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldUpdateManyForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldupdatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldDeleteForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefielddeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentCreateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentcreateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentUpdateForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentupdateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentDeleteForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentFindForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentfindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldGetDocumentFieldForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgetdocumentfieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldCreateDocumentFieldForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldCreateDocumentFieldsForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldUpdateDocumentFieldForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldUpdateDocumentFieldsForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldDeleteDocumentFieldForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletedocumentfieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientGetDocumentRecipientForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgetdocumentrecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientCreateDocumentRecipientForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientCreateDocumentRecipientsForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateDocumentRecipientForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateDocumentRecipientsForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientDeleteDocumentRecipientForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletedocumentrecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldCreateTemplateFieldForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldGetTemplateFieldForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgettemplatefieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldCreateTemplateFieldsForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldUpdateTemplateFieldForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldUpdateTemplateFieldsForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`FieldDeleteTemplateFieldForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletetemplatefieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientGetTemplateRecipientForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgettemplaterecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientCreateTemplateRecipientForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientCreateTemplateRecipientsForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateTemplateRecipientForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateTemplateRecipientsForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`RecipientDeleteTemplateRecipientForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletetemplaterecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateDirectLinkForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatedirectlinkforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateDeleteTemplateDirectLinkForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplatedirectlinkforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`TemplateToggleTemplateDirectLinkForbiddenError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatetoggletemplatedirectlinkforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 85 methods.*
* [`EnvelopeGetNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`EnvelopeFindNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`EnvelopeAuditLogFindNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeauditlogfindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`DocumentGetNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`DocumentFindNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentfindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadBetaNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadbetanotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`TemplateFindTemplatesNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatefindtemplatesnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`TemplateGetTemplateByIDNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategettemplatebyidnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`FolderFindFoldersNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderfindfoldersnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentFindNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentfindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDownloadNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdownloadnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientGetNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientgetnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldGetNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldgetnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentFindNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentfindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`FieldGetDocumentFieldNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgetdocumentfieldnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`RecipientGetDocumentRecipientNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgetdocumentrecipientnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`FieldGetTemplateFieldNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgettemplatefieldnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`RecipientGetTemplateRecipientNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgettemplaterecipientnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 85 methods.*
* [`EnvelopeGetInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeCreateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopecreateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeUseInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeuseinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeUpdateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeupdateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeDeleteInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopedeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeDuplicateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeduplicateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeDistributeInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopedistributeinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeRedistributeInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperedistributeinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeFindInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeAuditLogFindInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeauditlogfindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeGetManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopegetmanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentGetInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentFindInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentfindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentCreateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentUpdateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentupdateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentDeleteInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentDuplicateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentduplicateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentDistributeInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdistributeinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentRedistributeInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentredistributeinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentCreateDocumentTemporaryInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreatedocumenttemporaryinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentGetManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetmanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentDownloadBetaInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdownloadbetainternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateFindTemplatesInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatefindtemplatesinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateGetTemplateByIDInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategettemplatebyidinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateUpdateTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateupdatetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateDuplicateTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateduplicatetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateDeleteTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateCreateDocumentFromTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatedocumentfromtemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FolderFindFoldersInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderfindfoldersinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FolderCreateFolderInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/foldercreatefolderinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FolderUpdateFolderInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderupdatefolderinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FolderDeleteFolderInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/folderdeletefolderinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateGetManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategetmanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateTemporaryInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatetemporaryinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokeninternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokeninternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentFindInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentfindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentCreateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentcreateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentUpdateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentupdateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeAttachmentDeleteInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeattachmentdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemCreateManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemcreatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemUpdateManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemupdatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDeleteInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeItemDownloadInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopeitemdownloadinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientGetInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientgetinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientCreateManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientcreatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientUpdateManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientupdatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeRecipientDeleteInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/enveloperecipientdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldGetInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldgetinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldCreateManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldcreatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldUpdateManyInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefieldupdatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`EnvelopeFieldDeleteInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/envelopefielddeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentCreateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentcreateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentUpdateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentupdateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentDeleteInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`DocumentAttachmentFindInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentattachmentfindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldGetDocumentFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgetdocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldCreateDocumentFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldCreateDocumentFieldsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldUpdateDocumentFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldUpdateDocumentFieldsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldDeleteDocumentFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientGetDocumentRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgetdocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientCreateDocumentRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientCreateDocumentRecipientsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateDocumentRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateDocumentRecipientsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientDeleteDocumentRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldCreateTemplateFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldGetTemplateFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgettemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldCreateTemplateFieldsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldUpdateTemplateFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldUpdateTemplateFieldsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`FieldDeleteTemplateFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientGetTemplateRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgettemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientCreateTemplateRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientCreateTemplateRecipientsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateTemplateRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientUpdateTemplateRecipientsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`RecipientDeleteTemplateRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateCreateTemplateDirectLinkInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateDeleteTemplateDirectLinkInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`TemplateToggleTemplateDirectLinkInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatetoggletemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 85 methods.*
* [`ResponseValidationError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/documenso/sdk-python/blob/master/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from documenso_sdk import Documenso
import os


with Documenso(
    server_url="https://app.documenso.com/api/v2",
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.get(envelope_id="<id>")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

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
