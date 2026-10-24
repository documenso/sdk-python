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

- [Overview](#documenso-python-sdk)
  - [SDK Installation](#sdk-installation)
  - [IDE Support](#ide-support)
  - [Authentication](#authentication)
  - [Document creation example](#document-creation-example)
  - [Available Resources and Operations](#available-resources-and-operations)
  - [Retries](#retries)
  - [Error Handling](#error-handling)
  - [Debugging](#debugging)
- [Development](#development)
  - [Maturity](#maturity)
  - [Contributions](#contributions)

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
# requires-python = ">=3.10"
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

### [~~Document~~](docs/sdks/documentsdk/README.md)

* [~~document_get_many~~](docs/sdks/documentsdk/README.md#document_get_many) - Get multiple documents :warning: **Deprecated**
* [~~document_download~~](docs/sdks/documentsdk/README.md#document_download) - Download document (beta) :warning: **Deprecated**

### [~~Documents~~](docs/sdks/documents/README.md)

* [~~get~~](docs/sdks/documents/README.md#get) - Get document :warning: **Deprecated**
* [~~find~~](docs/sdks/documents/README.md#find) - Find documents :warning: **Deprecated**
* [~~create~~](docs/sdks/documents/README.md#create) - Create document :warning: **Deprecated**
* [~~update~~](docs/sdks/documents/README.md#update) - Update document :warning: **Deprecated**
* [~~delete~~](docs/sdks/documents/README.md#delete) - Delete document :warning: **Deprecated**
* [~~duplicate~~](docs/sdks/documents/README.md#duplicate) - Duplicate document :warning: **Deprecated**
* [~~distribute~~](docs/sdks/documents/README.md#distribute) - Distribute document :warning: **Deprecated**
* [~~redistribute~~](docs/sdks/documents/README.md#redistribute) - Redistribute document :warning: **Deprecated**
* [~~download~~](docs/sdks/documents/README.md#download) - Download document :warning: **Deprecated**
* [~~create_v0~~](docs/sdks/documents/README.md#create_v0) - Create document :warning: **Deprecated**

#### [~~Documents.Attachments~~](docs/sdks/documentsattachments/README.md)

* [~~create~~](docs/sdks/documentsattachments/README.md#create) - Create attachment :warning: **Deprecated**
* [~~update~~](docs/sdks/documentsattachments/README.md#update) - Update attachment :warning: **Deprecated**
* [~~delete~~](docs/sdks/documentsattachments/README.md#delete) - Delete attachment :warning: **Deprecated**
* [~~find~~](docs/sdks/documentsattachments/README.md#find) - Find attachments :warning: **Deprecated**

#### [~~Documents.Fields~~](docs/sdks/documentsfields/README.md)

* [~~get~~](docs/sdks/documentsfields/README.md#get) - Get document field :warning: **Deprecated**
* [~~create~~](docs/sdks/documentsfields/README.md#create) - Create document field :warning: **Deprecated**
* [~~create_many~~](docs/sdks/documentsfields/README.md#create_many) - Create document fields :warning: **Deprecated**
* [~~update~~](docs/sdks/documentsfields/README.md#update) - Update document field :warning: **Deprecated**
* [~~update_many~~](docs/sdks/documentsfields/README.md#update_many) - Update document fields :warning: **Deprecated**
* [~~delete~~](docs/sdks/documentsfields/README.md#delete) - Delete document field :warning: **Deprecated**

#### [~~Documents.Recipients~~](docs/sdks/documentsrecipients/README.md)

* [~~get~~](docs/sdks/documentsrecipients/README.md#get) - Get document recipient :warning: **Deprecated**
* [~~create~~](docs/sdks/documentsrecipients/README.md#create) - Create document recipient :warning: **Deprecated**
* [~~create_many~~](docs/sdks/documentsrecipients/README.md#create_many) - Create document recipients :warning: **Deprecated**
* [~~update~~](docs/sdks/documentsrecipients/README.md#update) - Update document recipient :warning: **Deprecated**
* [~~update_many~~](docs/sdks/documentsrecipients/README.md#update_many) - Update document recipients :warning: **Deprecated**
* [~~delete~~](docs/sdks/documentsrecipients/README.md#delete) - Delete document recipient :warning: **Deprecated**

### [Embedding](docs/sdks/embedding/README.md)

* [embedding_presign_create_embedding_presign_token](docs/sdks/embedding/README.md#embedding_presign_create_embedding_presign_token) - Create embedding presign token
* [embedding_presign_verify_embedding_presign_token](docs/sdks/embedding/README.md#embedding_presign_verify_embedding_presign_token) - Verify embedding presign token

### [Envelope](docs/sdks/envelope/README.md)

* [envelope_find](docs/sdks/envelope/README.md#envelope_find) - Find envelopes
* [envelope_audit_log_find](docs/sdks/envelope/README.md#envelope_audit_log_find) - Get envelope audit logs
* [envelope_audit_log_download_pdf](docs/sdks/envelope/README.md#envelope_audit_log_download_pdf) - Download envelope audit log PDF
* [envelope_certificate_download_pdf](docs/sdks/envelope/README.md#envelope_certificate_download_pdf) - Download envelope certificate PDF
* [envelope_get_many](docs/sdks/envelope/README.md#envelope_get_many) - Get multiple envelopes
* [envelope_cancel](docs/sdks/envelope/README.md#envelope_cancel) - Cancel envelope

### [EnvelopeRecipients](docs/sdks/enveloperecipients/README.md)

* [envelope_recipient_reject_on_behalf_of](docs/sdks/enveloperecipients/README.md#envelope_recipient_reject_on_behalf_of) - Reject envelope recipient on behalf of

### [Envelopes](docs/sdks/envelopes/README.md)

* [get](docs/sdks/envelopes/README.md#get) - Get envelope
* [create](docs/sdks/envelopes/README.md#create) - Create envelope
* [use](docs/sdks/envelopes/README.md#use) - Use envelope
* [update](docs/sdks/envelopes/README.md#update) - Update envelope
* [delete](docs/sdks/envelopes/README.md#delete) - Delete envelope
* [duplicate](docs/sdks/envelopes/README.md#duplicate) - Duplicate envelope
* [distribute](docs/sdks/envelopes/README.md#distribute) - Distribute envelope
* [redistribute](docs/sdks/envelopes/README.md#redistribute) - Redistribute envelope

#### [Envelopes.Attachments](docs/sdks/envelopesattachments/README.md)

* [find](docs/sdks/envelopesattachments/README.md#find) - Find attachments
* [create](docs/sdks/envelopesattachments/README.md#create) - Create attachment
* [update](docs/sdks/envelopesattachments/README.md#update) - Update attachment
* [delete](docs/sdks/envelopesattachments/README.md#delete) - Delete attachment

#### [Envelopes.Fields](docs/sdks/envelopesfields/README.md)

* [get](docs/sdks/envelopesfields/README.md#get) - Get envelope field
* [create_many](docs/sdks/envelopesfields/README.md#create_many) - Create envelope fields
* [update_many](docs/sdks/envelopesfields/README.md#update_many) - Update envelope fields
* [delete](docs/sdks/envelopesfields/README.md#delete) - Delete envelope field

#### [Envelopes.Items](docs/sdks/items/README.md)

* [create_many](docs/sdks/items/README.md#create_many) - Create envelope items
* [update_many](docs/sdks/items/README.md#update_many) - Update envelope items
* [delete](docs/sdks/items/README.md#delete) - Delete envelope item
* [download](docs/sdks/items/README.md#download) - Download an envelope item

#### [Envelopes.Recipients](docs/sdks/envelopesrecipients/README.md)

* [get](docs/sdks/envelopesrecipients/README.md#get) - Get envelope recipient
* [create_many](docs/sdks/envelopesrecipients/README.md#create_many) - Create envelope recipients
* [update_many](docs/sdks/envelopesrecipients/README.md#update_many) - Update envelope recipients
* [delete](docs/sdks/envelopesrecipients/README.md#delete) - Delete envelope recipient

### [Folders](docs/sdks/folders/README.md)

* [find](docs/sdks/folders/README.md#find) - Find folders
* [create](docs/sdks/folders/README.md#create) - Create new folder
* [update](docs/sdks/folders/README.md#update) - Update folder
* [delete](docs/sdks/folders/README.md#delete) - Delete folder

### [~~Template~~](docs/sdks/templatesdk/README.md)

* [~~template_get_many~~](docs/sdks/templatesdk/README.md#template_get_many) - Get multiple templates :warning: **Deprecated**
* [~~template_create_template_temporary~~](docs/sdks/templatesdk/README.md#template_create_template_temporary) - Create template :warning: **Deprecated**

### [~~Templates~~](docs/sdks/templates/README.md)

* [~~find~~](docs/sdks/templates/README.md#find) - Find templates :warning: **Deprecated**
* [~~get~~](docs/sdks/templates/README.md#get) - Get template :warning: **Deprecated**
* [~~create~~](docs/sdks/templates/README.md#create) - Create template :warning: **Deprecated**
* [~~update~~](docs/sdks/templates/README.md#update) - Update template :warning: **Deprecated**
* [~~duplicate~~](docs/sdks/templates/README.md#duplicate) - Duplicate template :warning: **Deprecated**
* [~~delete~~](docs/sdks/templates/README.md#delete) - Delete template :warning: **Deprecated**
* [~~use~~](docs/sdks/templates/README.md#use) - Use template :warning: **Deprecated**

#### [~~Templates.DirectLink~~](docs/sdks/directlinksdk/README.md)

* [~~create~~](docs/sdks/directlinksdk/README.md#create) - Create direct link :warning: **Deprecated**
* [~~delete~~](docs/sdks/directlinksdk/README.md#delete) - Delete direct link :warning: **Deprecated**
* [~~toggle~~](docs/sdks/directlinksdk/README.md#toggle) - Toggle direct link :warning: **Deprecated**

#### [~~Templates.Fields~~](docs/sdks/templatesfields/README.md)

* [~~create~~](docs/sdks/templatesfields/README.md#create) - Create template field :warning: **Deprecated**
* [~~get~~](docs/sdks/templatesfields/README.md#get) - Get template field :warning: **Deprecated**
* [~~create_many~~](docs/sdks/templatesfields/README.md#create_many) - Create template fields :warning: **Deprecated**
* [~~update~~](docs/sdks/templatesfields/README.md#update) - Update template field :warning: **Deprecated**
* [~~update_many~~](docs/sdks/templatesfields/README.md#update_many) - Update template fields :warning: **Deprecated**
* [~~delete~~](docs/sdks/templatesfields/README.md#delete) - Delete template field :warning: **Deprecated**

#### [~~Templates.Recipients~~](docs/sdks/templatesrecipients/README.md)

* [~~get~~](docs/sdks/templatesrecipients/README.md#get) - Get template recipient :warning: **Deprecated**
* [~~create~~](docs/sdks/templatesrecipients/README.md#create) - Create template recipient :warning: **Deprecated**
* [~~create_many~~](docs/sdks/templatesrecipients/README.md#create_many) - Create template recipients :warning: **Deprecated**
* [~~update~~](docs/sdks/templatesrecipients/README.md#update) - Update template recipient :warning: **Deprecated**
* [~~update_many~~](docs/sdks/templatesrecipients/README.md#update_many) - Update template recipients :warning: **Deprecated**
* [~~delete~~](docs/sdks/templatesrecipients/README.md#delete) - Delete template recipient :warning: **Deprecated**

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

[`DocumensoError`](./src/documenso_sdk/models/documensoerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

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
* [`DocumensoError`](./src/documenso_sdk/models/documensoerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (382)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`DocumensoError`](./src/documenso_sdk/models/documensoerror.py)**:
* [`EnvelopeGetBadRequestError`](./src/documenso_sdk/models/envelopegetbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeCreateBadRequestError`](./src/documenso_sdk/models/envelopecreatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeUseBadRequestError`](./src/documenso_sdk/models/envelopeusebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeUpdateBadRequestError`](./src/documenso_sdk/models/envelopeupdatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeDeleteBadRequestError`](./src/documenso_sdk/models/envelopedeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeDuplicateBadRequestError`](./src/documenso_sdk/models/envelopeduplicatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeDistributeBadRequestError`](./src/documenso_sdk/models/envelopedistributebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeRedistributeBadRequestError`](./src/documenso_sdk/models/enveloperedistributebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientRejectOnBehalfOfBadRequestError`](./src/documenso_sdk/models/enveloperecipientrejectonbehalfofbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeFindBadRequestError`](./src/documenso_sdk/models/envelopefindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogFindBadRequestError`](./src/documenso_sdk/models/envelopeauditlogfindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogDownloadPdfBadRequestError`](./src/documenso_sdk/models/envelopeauditlogdownloadpdfbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeCertificateDownloadPdfBadRequestError`](./src/documenso_sdk/models/envelopecertificatedownloadpdfbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeGetManyBadRequestError`](./src/documenso_sdk/models/envelopegetmanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeCancelBadRequestError`](./src/documenso_sdk/models/envelopecancelbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentGetBadRequestError`](./src/documenso_sdk/models/documentgetbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentFindBadRequestError`](./src/documenso_sdk/models/documentfindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentCreateBadRequestError`](./src/documenso_sdk/models/documentcreatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentUpdateBadRequestError`](./src/documenso_sdk/models/documentupdatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentDeleteBadRequestError`](./src/documenso_sdk/models/documentdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentDuplicateBadRequestError`](./src/documenso_sdk/models/documentduplicatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentDistributeBadRequestError`](./src/documenso_sdk/models/documentdistributebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentRedistributeBadRequestError`](./src/documenso_sdk/models/documentredistributebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadBadRequestError`](./src/documenso_sdk/models/documentdownloadbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentCreateDocumentTemporaryBadRequestError`](./src/documenso_sdk/models/documentcreatedocumenttemporarybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentGetManyBadRequestError`](./src/documenso_sdk/models/documentgetmanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadBetaBadRequestError`](./src/documenso_sdk/models/documentdownloadbetabadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateFindTemplatesBadRequestError`](./src/documenso_sdk/models/templatefindtemplatesbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateGetTemplateByIDBadRequestError`](./src/documenso_sdk/models/templategettemplatebyidbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateBadRequestError`](./src/documenso_sdk/models/templatecreatetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateUpdateTemplateBadRequestError`](./src/documenso_sdk/models/templateupdatetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateDuplicateTemplateBadRequestError`](./src/documenso_sdk/models/templateduplicatetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateDeleteTemplateBadRequestError`](./src/documenso_sdk/models/templatedeletetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateCreateDocumentFromTemplateBadRequestError`](./src/documenso_sdk/models/templatecreatedocumentfromtemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FolderFindFoldersBadRequestError`](./src/documenso_sdk/models/folderfindfoldersbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FolderCreateFolderBadRequestError`](./src/documenso_sdk/models/foldercreatefolderbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FolderUpdateFolderBadRequestError`](./src/documenso_sdk/models/folderupdatefolderbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FolderDeleteFolderBadRequestError`](./src/documenso_sdk/models/folderdeletefolderbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateGetManyBadRequestError`](./src/documenso_sdk/models/templategetmanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateTemporaryBadRequestError`](./src/documenso_sdk/models/templatecreatetemplatetemporarybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenBadRequestError`](./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokenbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenBadRequestError`](./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokenbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentFindBadRequestError`](./src/documenso_sdk/models/envelopeattachmentfindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentCreateBadRequestError`](./src/documenso_sdk/models/envelopeattachmentcreatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentUpdateBadRequestError`](./src/documenso_sdk/models/envelopeattachmentupdatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentDeleteBadRequestError`](./src/documenso_sdk/models/envelopeattachmentdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemCreateManyBadRequestError`](./src/documenso_sdk/models/envelopeitemcreatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemUpdateManyBadRequestError`](./src/documenso_sdk/models/envelopeitemupdatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDeleteBadRequestError`](./src/documenso_sdk/models/envelopeitemdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDownloadBadRequestError`](./src/documenso_sdk/models/envelopeitemdownloadbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientGetBadRequestError`](./src/documenso_sdk/models/enveloperecipientgetbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientCreateManyBadRequestError`](./src/documenso_sdk/models/enveloperecipientcreatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientUpdateManyBadRequestError`](./src/documenso_sdk/models/enveloperecipientupdatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientDeleteBadRequestError`](./src/documenso_sdk/models/enveloperecipientdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldGetBadRequestError`](./src/documenso_sdk/models/envelopefieldgetbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldCreateManyBadRequestError`](./src/documenso_sdk/models/envelopefieldcreatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldUpdateManyBadRequestError`](./src/documenso_sdk/models/envelopefieldupdatemanybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldDeleteBadRequestError`](./src/documenso_sdk/models/envelopefielddeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentCreateBadRequestError`](./src/documenso_sdk/models/documentattachmentcreatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentUpdateBadRequestError`](./src/documenso_sdk/models/documentattachmentupdatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentDeleteBadRequestError`](./src/documenso_sdk/models/documentattachmentdeletebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentFindBadRequestError`](./src/documenso_sdk/models/documentattachmentfindbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldGetDocumentFieldBadRequestError`](./src/documenso_sdk/models/fieldgetdocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldCreateDocumentFieldBadRequestError`](./src/documenso_sdk/models/fieldcreatedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldCreateDocumentFieldsBadRequestError`](./src/documenso_sdk/models/fieldcreatedocumentfieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldUpdateDocumentFieldBadRequestError`](./src/documenso_sdk/models/fieldupdatedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldUpdateDocumentFieldsBadRequestError`](./src/documenso_sdk/models/fieldupdatedocumentfieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldDeleteDocumentFieldBadRequestError`](./src/documenso_sdk/models/fielddeletedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientGetDocumentRecipientBadRequestError`](./src/documenso_sdk/models/recipientgetdocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientCreateDocumentRecipientBadRequestError`](./src/documenso_sdk/models/recipientcreatedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientCreateDocumentRecipientsBadRequestError`](./src/documenso_sdk/models/recipientcreatedocumentrecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateDocumentRecipientBadRequestError`](./src/documenso_sdk/models/recipientupdatedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateDocumentRecipientsBadRequestError`](./src/documenso_sdk/models/recipientupdatedocumentrecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientDeleteDocumentRecipientBadRequestError`](./src/documenso_sdk/models/recipientdeletedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldCreateTemplateFieldBadRequestError`](./src/documenso_sdk/models/fieldcreatetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldGetTemplateFieldBadRequestError`](./src/documenso_sdk/models/fieldgettemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldCreateTemplateFieldsBadRequestError`](./src/documenso_sdk/models/fieldcreatetemplatefieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldUpdateTemplateFieldBadRequestError`](./src/documenso_sdk/models/fieldupdatetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldUpdateTemplateFieldsBadRequestError`](./src/documenso_sdk/models/fieldupdatetemplatefieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`FieldDeleteTemplateFieldBadRequestError`](./src/documenso_sdk/models/fielddeletetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientGetTemplateRecipientBadRequestError`](./src/documenso_sdk/models/recipientgettemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientCreateTemplateRecipientBadRequestError`](./src/documenso_sdk/models/recipientcreatetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientCreateTemplateRecipientsBadRequestError`](./src/documenso_sdk/models/recipientcreatetemplaterecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateTemplateRecipientBadRequestError`](./src/documenso_sdk/models/recipientupdatetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateTemplateRecipientsBadRequestError`](./src/documenso_sdk/models/recipientupdatetemplaterecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`RecipientDeleteTemplateRecipientBadRequestError`](./src/documenso_sdk/models/recipientdeletetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateDirectLinkBadRequestError`](./src/documenso_sdk/models/templatecreatetemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateDeleteTemplateDirectLinkBadRequestError`](./src/documenso_sdk/models/templatedeletetemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`TemplateToggleTemplateDirectLinkBadRequestError`](./src/documenso_sdk/models/templatetoggletemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 89 methods.*
* [`EnvelopeGetUnauthorizedError`](./src/documenso_sdk/models/envelopegetunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeCreateUnauthorizedError`](./src/documenso_sdk/models/envelopecreateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeUseUnauthorizedError`](./src/documenso_sdk/models/envelopeuseunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeUpdateUnauthorizedError`](./src/documenso_sdk/models/envelopeupdateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeDeleteUnauthorizedError`](./src/documenso_sdk/models/envelopedeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeDuplicateUnauthorizedError`](./src/documenso_sdk/models/envelopeduplicateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeDistributeUnauthorizedError`](./src/documenso_sdk/models/envelopedistributeunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeRedistributeUnauthorizedError`](./src/documenso_sdk/models/enveloperedistributeunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientRejectOnBehalfOfUnauthorizedError`](./src/documenso_sdk/models/enveloperecipientrejectonbehalfofunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeFindUnauthorizedError`](./src/documenso_sdk/models/envelopefindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogFindUnauthorizedError`](./src/documenso_sdk/models/envelopeauditlogfindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogDownloadPdfUnauthorizedError`](./src/documenso_sdk/models/envelopeauditlogdownloadpdfunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeCertificateDownloadPdfUnauthorizedError`](./src/documenso_sdk/models/envelopecertificatedownloadpdfunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeGetManyUnauthorizedError`](./src/documenso_sdk/models/envelopegetmanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeCancelUnauthorizedError`](./src/documenso_sdk/models/envelopecancelunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentGetUnauthorizedError`](./src/documenso_sdk/models/documentgetunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentFindUnauthorizedError`](./src/documenso_sdk/models/documentfindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentCreateUnauthorizedError`](./src/documenso_sdk/models/documentcreateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentUpdateUnauthorizedError`](./src/documenso_sdk/models/documentupdateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentDeleteUnauthorizedError`](./src/documenso_sdk/models/documentdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentDuplicateUnauthorizedError`](./src/documenso_sdk/models/documentduplicateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentDistributeUnauthorizedError`](./src/documenso_sdk/models/documentdistributeunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentRedistributeUnauthorizedError`](./src/documenso_sdk/models/documentredistributeunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadUnauthorizedError`](./src/documenso_sdk/models/documentdownloadunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentCreateDocumentTemporaryUnauthorizedError`](./src/documenso_sdk/models/documentcreatedocumenttemporaryunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentGetManyUnauthorizedError`](./src/documenso_sdk/models/documentgetmanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadBetaUnauthorizedError`](./src/documenso_sdk/models/documentdownloadbetaunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateFindTemplatesUnauthorizedError`](./src/documenso_sdk/models/templatefindtemplatesunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateGetTemplateByIDUnauthorizedError`](./src/documenso_sdk/models/templategettemplatebyidunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateUnauthorizedError`](./src/documenso_sdk/models/templatecreatetemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateUpdateTemplateUnauthorizedError`](./src/documenso_sdk/models/templateupdatetemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateDuplicateTemplateUnauthorizedError`](./src/documenso_sdk/models/templateduplicatetemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateDeleteTemplateUnauthorizedError`](./src/documenso_sdk/models/templatedeletetemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateCreateDocumentFromTemplateUnauthorizedError`](./src/documenso_sdk/models/templatecreatedocumentfromtemplateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FolderFindFoldersUnauthorizedError`](./src/documenso_sdk/models/folderfindfoldersunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FolderCreateFolderUnauthorizedError`](./src/documenso_sdk/models/foldercreatefolderunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FolderUpdateFolderUnauthorizedError`](./src/documenso_sdk/models/folderupdatefolderunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FolderDeleteFolderUnauthorizedError`](./src/documenso_sdk/models/folderdeletefolderunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateGetManyUnauthorizedError`](./src/documenso_sdk/models/templategetmanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateTemporaryUnauthorizedError`](./src/documenso_sdk/models/templatecreatetemplatetemporaryunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenUnauthorizedError`](./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokenunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenUnauthorizedError`](./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokenunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentFindUnauthorizedError`](./src/documenso_sdk/models/envelopeattachmentfindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentCreateUnauthorizedError`](./src/documenso_sdk/models/envelopeattachmentcreateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentUpdateUnauthorizedError`](./src/documenso_sdk/models/envelopeattachmentupdateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentDeleteUnauthorizedError`](./src/documenso_sdk/models/envelopeattachmentdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemCreateManyUnauthorizedError`](./src/documenso_sdk/models/envelopeitemcreatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemUpdateManyUnauthorizedError`](./src/documenso_sdk/models/envelopeitemupdatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDeleteUnauthorizedError`](./src/documenso_sdk/models/envelopeitemdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDownloadUnauthorizedError`](./src/documenso_sdk/models/envelopeitemdownloadunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientGetUnauthorizedError`](./src/documenso_sdk/models/enveloperecipientgetunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientCreateManyUnauthorizedError`](./src/documenso_sdk/models/enveloperecipientcreatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientUpdateManyUnauthorizedError`](./src/documenso_sdk/models/enveloperecipientupdatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientDeleteUnauthorizedError`](./src/documenso_sdk/models/enveloperecipientdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldGetUnauthorizedError`](./src/documenso_sdk/models/envelopefieldgetunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldCreateManyUnauthorizedError`](./src/documenso_sdk/models/envelopefieldcreatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldUpdateManyUnauthorizedError`](./src/documenso_sdk/models/envelopefieldupdatemanyunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldDeleteUnauthorizedError`](./src/documenso_sdk/models/envelopefielddeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentCreateUnauthorizedError`](./src/documenso_sdk/models/documentattachmentcreateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentUpdateUnauthorizedError`](./src/documenso_sdk/models/documentattachmentupdateunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentDeleteUnauthorizedError`](./src/documenso_sdk/models/documentattachmentdeleteunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentFindUnauthorizedError`](./src/documenso_sdk/models/documentattachmentfindunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldGetDocumentFieldUnauthorizedError`](./src/documenso_sdk/models/fieldgetdocumentfieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldCreateDocumentFieldUnauthorizedError`](./src/documenso_sdk/models/fieldcreatedocumentfieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldCreateDocumentFieldsUnauthorizedError`](./src/documenso_sdk/models/fieldcreatedocumentfieldsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldUpdateDocumentFieldUnauthorizedError`](./src/documenso_sdk/models/fieldupdatedocumentfieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldUpdateDocumentFieldsUnauthorizedError`](./src/documenso_sdk/models/fieldupdatedocumentfieldsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldDeleteDocumentFieldUnauthorizedError`](./src/documenso_sdk/models/fielddeletedocumentfieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientGetDocumentRecipientUnauthorizedError`](./src/documenso_sdk/models/recipientgetdocumentrecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientCreateDocumentRecipientUnauthorizedError`](./src/documenso_sdk/models/recipientcreatedocumentrecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientCreateDocumentRecipientsUnauthorizedError`](./src/documenso_sdk/models/recipientcreatedocumentrecipientsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateDocumentRecipientUnauthorizedError`](./src/documenso_sdk/models/recipientupdatedocumentrecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateDocumentRecipientsUnauthorizedError`](./src/documenso_sdk/models/recipientupdatedocumentrecipientsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientDeleteDocumentRecipientUnauthorizedError`](./src/documenso_sdk/models/recipientdeletedocumentrecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldCreateTemplateFieldUnauthorizedError`](./src/documenso_sdk/models/fieldcreatetemplatefieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldGetTemplateFieldUnauthorizedError`](./src/documenso_sdk/models/fieldgettemplatefieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldCreateTemplateFieldsUnauthorizedError`](./src/documenso_sdk/models/fieldcreatetemplatefieldsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldUpdateTemplateFieldUnauthorizedError`](./src/documenso_sdk/models/fieldupdatetemplatefieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldUpdateTemplateFieldsUnauthorizedError`](./src/documenso_sdk/models/fieldupdatetemplatefieldsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`FieldDeleteTemplateFieldUnauthorizedError`](./src/documenso_sdk/models/fielddeletetemplatefieldunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientGetTemplateRecipientUnauthorizedError`](./src/documenso_sdk/models/recipientgettemplaterecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientCreateTemplateRecipientUnauthorizedError`](./src/documenso_sdk/models/recipientcreatetemplaterecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientCreateTemplateRecipientsUnauthorizedError`](./src/documenso_sdk/models/recipientcreatetemplaterecipientsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateTemplateRecipientUnauthorizedError`](./src/documenso_sdk/models/recipientupdatetemplaterecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateTemplateRecipientsUnauthorizedError`](./src/documenso_sdk/models/recipientupdatetemplaterecipientsunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`RecipientDeleteTemplateRecipientUnauthorizedError`](./src/documenso_sdk/models/recipientdeletetemplaterecipientunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateDirectLinkUnauthorizedError`](./src/documenso_sdk/models/templatecreatetemplatedirectlinkunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateDeleteTemplateDirectLinkUnauthorizedError`](./src/documenso_sdk/models/templatedeletetemplatedirectlinkunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`TemplateToggleTemplateDirectLinkUnauthorizedError`](./src/documenso_sdk/models/templatetoggletemplatedirectlinkunauthorizederror.py): Authorization not provided. Status code `401`. Applicable to 1 of 89 methods.*
* [`EnvelopeGetForbiddenError`](./src/documenso_sdk/models/envelopegetforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeCreateForbiddenError`](./src/documenso_sdk/models/envelopecreateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeUseForbiddenError`](./src/documenso_sdk/models/envelopeuseforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeUpdateForbiddenError`](./src/documenso_sdk/models/envelopeupdateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeDeleteForbiddenError`](./src/documenso_sdk/models/envelopedeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeDuplicateForbiddenError`](./src/documenso_sdk/models/envelopeduplicateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeDistributeForbiddenError`](./src/documenso_sdk/models/envelopedistributeforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeRedistributeForbiddenError`](./src/documenso_sdk/models/enveloperedistributeforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientRejectOnBehalfOfForbiddenError`](./src/documenso_sdk/models/enveloperecipientrejectonbehalfofforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeFindForbiddenError`](./src/documenso_sdk/models/envelopefindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogFindForbiddenError`](./src/documenso_sdk/models/envelopeauditlogfindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogDownloadPdfForbiddenError`](./src/documenso_sdk/models/envelopeauditlogdownloadpdfforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeCertificateDownloadPdfForbiddenError`](./src/documenso_sdk/models/envelopecertificatedownloadpdfforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeGetManyForbiddenError`](./src/documenso_sdk/models/envelopegetmanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeCancelForbiddenError`](./src/documenso_sdk/models/envelopecancelforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentGetForbiddenError`](./src/documenso_sdk/models/documentgetforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentFindForbiddenError`](./src/documenso_sdk/models/documentfindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentCreateForbiddenError`](./src/documenso_sdk/models/documentcreateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentUpdateForbiddenError`](./src/documenso_sdk/models/documentupdateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentDeleteForbiddenError`](./src/documenso_sdk/models/documentdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentDuplicateForbiddenError`](./src/documenso_sdk/models/documentduplicateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentDistributeForbiddenError`](./src/documenso_sdk/models/documentdistributeforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentRedistributeForbiddenError`](./src/documenso_sdk/models/documentredistributeforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadForbiddenError`](./src/documenso_sdk/models/documentdownloadforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentCreateDocumentTemporaryForbiddenError`](./src/documenso_sdk/models/documentcreatedocumenttemporaryforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentGetManyForbiddenError`](./src/documenso_sdk/models/documentgetmanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadBetaForbiddenError`](./src/documenso_sdk/models/documentdownloadbetaforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateFindTemplatesForbiddenError`](./src/documenso_sdk/models/templatefindtemplatesforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateGetTemplateByIDForbiddenError`](./src/documenso_sdk/models/templategettemplatebyidforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateForbiddenError`](./src/documenso_sdk/models/templatecreatetemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateUpdateTemplateForbiddenError`](./src/documenso_sdk/models/templateupdatetemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateDuplicateTemplateForbiddenError`](./src/documenso_sdk/models/templateduplicatetemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateDeleteTemplateForbiddenError`](./src/documenso_sdk/models/templatedeletetemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateCreateDocumentFromTemplateForbiddenError`](./src/documenso_sdk/models/templatecreatedocumentfromtemplateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FolderFindFoldersForbiddenError`](./src/documenso_sdk/models/folderfindfoldersforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FolderCreateFolderForbiddenError`](./src/documenso_sdk/models/foldercreatefolderforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FolderUpdateFolderForbiddenError`](./src/documenso_sdk/models/folderupdatefolderforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FolderDeleteFolderForbiddenError`](./src/documenso_sdk/models/folderdeletefolderforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateGetManyForbiddenError`](./src/documenso_sdk/models/templategetmanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateTemporaryForbiddenError`](./src/documenso_sdk/models/templatecreatetemplatetemporaryforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenForbiddenError`](./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokenforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenForbiddenError`](./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokenforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentFindForbiddenError`](./src/documenso_sdk/models/envelopeattachmentfindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentCreateForbiddenError`](./src/documenso_sdk/models/envelopeattachmentcreateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentUpdateForbiddenError`](./src/documenso_sdk/models/envelopeattachmentupdateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentDeleteForbiddenError`](./src/documenso_sdk/models/envelopeattachmentdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemCreateManyForbiddenError`](./src/documenso_sdk/models/envelopeitemcreatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemUpdateManyForbiddenError`](./src/documenso_sdk/models/envelopeitemupdatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDeleteForbiddenError`](./src/documenso_sdk/models/envelopeitemdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDownloadForbiddenError`](./src/documenso_sdk/models/envelopeitemdownloadforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientGetForbiddenError`](./src/documenso_sdk/models/enveloperecipientgetforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientCreateManyForbiddenError`](./src/documenso_sdk/models/enveloperecipientcreatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientUpdateManyForbiddenError`](./src/documenso_sdk/models/enveloperecipientupdatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientDeleteForbiddenError`](./src/documenso_sdk/models/enveloperecipientdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldGetForbiddenError`](./src/documenso_sdk/models/envelopefieldgetforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldCreateManyForbiddenError`](./src/documenso_sdk/models/envelopefieldcreatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldUpdateManyForbiddenError`](./src/documenso_sdk/models/envelopefieldupdatemanyforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldDeleteForbiddenError`](./src/documenso_sdk/models/envelopefielddeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentCreateForbiddenError`](./src/documenso_sdk/models/documentattachmentcreateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentUpdateForbiddenError`](./src/documenso_sdk/models/documentattachmentupdateforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentDeleteForbiddenError`](./src/documenso_sdk/models/documentattachmentdeleteforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentFindForbiddenError`](./src/documenso_sdk/models/documentattachmentfindforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldGetDocumentFieldForbiddenError`](./src/documenso_sdk/models/fieldgetdocumentfieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldCreateDocumentFieldForbiddenError`](./src/documenso_sdk/models/fieldcreatedocumentfieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldCreateDocumentFieldsForbiddenError`](./src/documenso_sdk/models/fieldcreatedocumentfieldsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldUpdateDocumentFieldForbiddenError`](./src/documenso_sdk/models/fieldupdatedocumentfieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldUpdateDocumentFieldsForbiddenError`](./src/documenso_sdk/models/fieldupdatedocumentfieldsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldDeleteDocumentFieldForbiddenError`](./src/documenso_sdk/models/fielddeletedocumentfieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientGetDocumentRecipientForbiddenError`](./src/documenso_sdk/models/recipientgetdocumentrecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientCreateDocumentRecipientForbiddenError`](./src/documenso_sdk/models/recipientcreatedocumentrecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientCreateDocumentRecipientsForbiddenError`](./src/documenso_sdk/models/recipientcreatedocumentrecipientsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateDocumentRecipientForbiddenError`](./src/documenso_sdk/models/recipientupdatedocumentrecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateDocumentRecipientsForbiddenError`](./src/documenso_sdk/models/recipientupdatedocumentrecipientsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientDeleteDocumentRecipientForbiddenError`](./src/documenso_sdk/models/recipientdeletedocumentrecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldCreateTemplateFieldForbiddenError`](./src/documenso_sdk/models/fieldcreatetemplatefieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldGetTemplateFieldForbiddenError`](./src/documenso_sdk/models/fieldgettemplatefieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldCreateTemplateFieldsForbiddenError`](./src/documenso_sdk/models/fieldcreatetemplatefieldsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldUpdateTemplateFieldForbiddenError`](./src/documenso_sdk/models/fieldupdatetemplatefieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldUpdateTemplateFieldsForbiddenError`](./src/documenso_sdk/models/fieldupdatetemplatefieldsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`FieldDeleteTemplateFieldForbiddenError`](./src/documenso_sdk/models/fielddeletetemplatefieldforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientGetTemplateRecipientForbiddenError`](./src/documenso_sdk/models/recipientgettemplaterecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientCreateTemplateRecipientForbiddenError`](./src/documenso_sdk/models/recipientcreatetemplaterecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientCreateTemplateRecipientsForbiddenError`](./src/documenso_sdk/models/recipientcreatetemplaterecipientsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateTemplateRecipientForbiddenError`](./src/documenso_sdk/models/recipientupdatetemplaterecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateTemplateRecipientsForbiddenError`](./src/documenso_sdk/models/recipientupdatetemplaterecipientsforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`RecipientDeleteTemplateRecipientForbiddenError`](./src/documenso_sdk/models/recipientdeletetemplaterecipientforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateDirectLinkForbiddenError`](./src/documenso_sdk/models/templatecreatetemplatedirectlinkforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateDeleteTemplateDirectLinkForbiddenError`](./src/documenso_sdk/models/templatedeletetemplatedirectlinkforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`TemplateToggleTemplateDirectLinkForbiddenError`](./src/documenso_sdk/models/templatetoggletemplatedirectlinkforbiddenerror.py): Insufficient access. Status code `403`. Applicable to 1 of 89 methods.*
* [`EnvelopeGetNotFoundError`](./src/documenso_sdk/models/envelopegetnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeFindNotFoundError`](./src/documenso_sdk/models/envelopefindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogFindNotFoundError`](./src/documenso_sdk/models/envelopeauditlogfindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogDownloadPdfNotFoundError`](./src/documenso_sdk/models/envelopeauditlogdownloadpdfnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeCertificateDownloadPdfNotFoundError`](./src/documenso_sdk/models/envelopecertificatedownloadpdfnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`DocumentGetNotFoundError`](./src/documenso_sdk/models/documentgetnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`DocumentFindNotFoundError`](./src/documenso_sdk/models/documentfindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadNotFoundError`](./src/documenso_sdk/models/documentdownloadnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadBetaNotFoundError`](./src/documenso_sdk/models/documentdownloadbetanotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`TemplateFindTemplatesNotFoundError`](./src/documenso_sdk/models/templatefindtemplatesnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`TemplateGetTemplateByIDNotFoundError`](./src/documenso_sdk/models/templategettemplatebyidnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`FolderFindFoldersNotFoundError`](./src/documenso_sdk/models/folderfindfoldersnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentFindNotFoundError`](./src/documenso_sdk/models/envelopeattachmentfindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDownloadNotFoundError`](./src/documenso_sdk/models/envelopeitemdownloadnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientGetNotFoundError`](./src/documenso_sdk/models/enveloperecipientgetnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldGetNotFoundError`](./src/documenso_sdk/models/envelopefieldgetnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentFindNotFoundError`](./src/documenso_sdk/models/documentattachmentfindnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`FieldGetDocumentFieldNotFoundError`](./src/documenso_sdk/models/fieldgetdocumentfieldnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`RecipientGetDocumentRecipientNotFoundError`](./src/documenso_sdk/models/recipientgetdocumentrecipientnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`FieldGetTemplateFieldNotFoundError`](./src/documenso_sdk/models/fieldgettemplatefieldnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`RecipientGetTemplateRecipientNotFoundError`](./src/documenso_sdk/models/recipientgettemplaterecipientnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 89 methods.*
* [`EnvelopeGetInternalServerError`](./src/documenso_sdk/models/envelopegetinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeCreateInternalServerError`](./src/documenso_sdk/models/envelopecreateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeUseInternalServerError`](./src/documenso_sdk/models/envelopeuseinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeUpdateInternalServerError`](./src/documenso_sdk/models/envelopeupdateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeDeleteInternalServerError`](./src/documenso_sdk/models/envelopedeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeDuplicateInternalServerError`](./src/documenso_sdk/models/envelopeduplicateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeDistributeInternalServerError`](./src/documenso_sdk/models/envelopedistributeinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeRedistributeInternalServerError`](./src/documenso_sdk/models/enveloperedistributeinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientRejectOnBehalfOfInternalServerError`](./src/documenso_sdk/models/enveloperecipientrejectonbehalfofinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeFindInternalServerError`](./src/documenso_sdk/models/envelopefindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogFindInternalServerError`](./src/documenso_sdk/models/envelopeauditlogfindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeAuditLogDownloadPdfInternalServerError`](./src/documenso_sdk/models/envelopeauditlogdownloadpdfinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeCertificateDownloadPdfInternalServerError`](./src/documenso_sdk/models/envelopecertificatedownloadpdfinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeGetManyInternalServerError`](./src/documenso_sdk/models/envelopegetmanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeCancelInternalServerError`](./src/documenso_sdk/models/envelopecancelinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentGetInternalServerError`](./src/documenso_sdk/models/documentgetinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentFindInternalServerError`](./src/documenso_sdk/models/documentfindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentCreateInternalServerError`](./src/documenso_sdk/models/documentcreateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentUpdateInternalServerError`](./src/documenso_sdk/models/documentupdateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentDeleteInternalServerError`](./src/documenso_sdk/models/documentdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentDuplicateInternalServerError`](./src/documenso_sdk/models/documentduplicateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentDistributeInternalServerError`](./src/documenso_sdk/models/documentdistributeinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentRedistributeInternalServerError`](./src/documenso_sdk/models/documentredistributeinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadInternalServerError`](./src/documenso_sdk/models/documentdownloadinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentCreateDocumentTemporaryInternalServerError`](./src/documenso_sdk/models/documentcreatedocumenttemporaryinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentGetManyInternalServerError`](./src/documenso_sdk/models/documentgetmanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentDownloadBetaInternalServerError`](./src/documenso_sdk/models/documentdownloadbetainternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateFindTemplatesInternalServerError`](./src/documenso_sdk/models/templatefindtemplatesinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateGetTemplateByIDInternalServerError`](./src/documenso_sdk/models/templategettemplatebyidinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateInternalServerError`](./src/documenso_sdk/models/templatecreatetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateUpdateTemplateInternalServerError`](./src/documenso_sdk/models/templateupdatetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateDuplicateTemplateInternalServerError`](./src/documenso_sdk/models/templateduplicatetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateDeleteTemplateInternalServerError`](./src/documenso_sdk/models/templatedeletetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateCreateDocumentFromTemplateInternalServerError`](./src/documenso_sdk/models/templatecreatedocumentfromtemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FolderFindFoldersInternalServerError`](./src/documenso_sdk/models/folderfindfoldersinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FolderCreateFolderInternalServerError`](./src/documenso_sdk/models/foldercreatefolderinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FolderUpdateFolderInternalServerError`](./src/documenso_sdk/models/folderupdatefolderinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FolderDeleteFolderInternalServerError`](./src/documenso_sdk/models/folderdeletefolderinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateGetManyInternalServerError`](./src/documenso_sdk/models/templategetmanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateTemporaryInternalServerError`](./src/documenso_sdk/models/templatecreatetemplatetemporaryinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenInternalServerError`](./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokeninternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenInternalServerError`](./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokeninternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentFindInternalServerError`](./src/documenso_sdk/models/envelopeattachmentfindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentCreateInternalServerError`](./src/documenso_sdk/models/envelopeattachmentcreateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentUpdateInternalServerError`](./src/documenso_sdk/models/envelopeattachmentupdateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeAttachmentDeleteInternalServerError`](./src/documenso_sdk/models/envelopeattachmentdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemCreateManyInternalServerError`](./src/documenso_sdk/models/envelopeitemcreatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemUpdateManyInternalServerError`](./src/documenso_sdk/models/envelopeitemupdatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDeleteInternalServerError`](./src/documenso_sdk/models/envelopeitemdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeItemDownloadInternalServerError`](./src/documenso_sdk/models/envelopeitemdownloadinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientGetInternalServerError`](./src/documenso_sdk/models/enveloperecipientgetinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientCreateManyInternalServerError`](./src/documenso_sdk/models/enveloperecipientcreatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientUpdateManyInternalServerError`](./src/documenso_sdk/models/enveloperecipientupdatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeRecipientDeleteInternalServerError`](./src/documenso_sdk/models/enveloperecipientdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldGetInternalServerError`](./src/documenso_sdk/models/envelopefieldgetinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldCreateManyInternalServerError`](./src/documenso_sdk/models/envelopefieldcreatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldUpdateManyInternalServerError`](./src/documenso_sdk/models/envelopefieldupdatemanyinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`EnvelopeFieldDeleteInternalServerError`](./src/documenso_sdk/models/envelopefielddeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentCreateInternalServerError`](./src/documenso_sdk/models/documentattachmentcreateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentUpdateInternalServerError`](./src/documenso_sdk/models/documentattachmentupdateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentDeleteInternalServerError`](./src/documenso_sdk/models/documentattachmentdeleteinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`DocumentAttachmentFindInternalServerError`](./src/documenso_sdk/models/documentattachmentfindinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldGetDocumentFieldInternalServerError`](./src/documenso_sdk/models/fieldgetdocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldCreateDocumentFieldInternalServerError`](./src/documenso_sdk/models/fieldcreatedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldCreateDocumentFieldsInternalServerError`](./src/documenso_sdk/models/fieldcreatedocumentfieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldUpdateDocumentFieldInternalServerError`](./src/documenso_sdk/models/fieldupdatedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldUpdateDocumentFieldsInternalServerError`](./src/documenso_sdk/models/fieldupdatedocumentfieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldDeleteDocumentFieldInternalServerError`](./src/documenso_sdk/models/fielddeletedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientGetDocumentRecipientInternalServerError`](./src/documenso_sdk/models/recipientgetdocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientCreateDocumentRecipientInternalServerError`](./src/documenso_sdk/models/recipientcreatedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientCreateDocumentRecipientsInternalServerError`](./src/documenso_sdk/models/recipientcreatedocumentrecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateDocumentRecipientInternalServerError`](./src/documenso_sdk/models/recipientupdatedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateDocumentRecipientsInternalServerError`](./src/documenso_sdk/models/recipientupdatedocumentrecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientDeleteDocumentRecipientInternalServerError`](./src/documenso_sdk/models/recipientdeletedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldCreateTemplateFieldInternalServerError`](./src/documenso_sdk/models/fieldcreatetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldGetTemplateFieldInternalServerError`](./src/documenso_sdk/models/fieldgettemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldCreateTemplateFieldsInternalServerError`](./src/documenso_sdk/models/fieldcreatetemplatefieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldUpdateTemplateFieldInternalServerError`](./src/documenso_sdk/models/fieldupdatetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldUpdateTemplateFieldsInternalServerError`](./src/documenso_sdk/models/fieldupdatetemplatefieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`FieldDeleteTemplateFieldInternalServerError`](./src/documenso_sdk/models/fielddeletetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientGetTemplateRecipientInternalServerError`](./src/documenso_sdk/models/recipientgettemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientCreateTemplateRecipientInternalServerError`](./src/documenso_sdk/models/recipientcreatetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientCreateTemplateRecipientsInternalServerError`](./src/documenso_sdk/models/recipientcreatetemplaterecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateTemplateRecipientInternalServerError`](./src/documenso_sdk/models/recipientupdatetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientUpdateTemplateRecipientsInternalServerError`](./src/documenso_sdk/models/recipientupdatetemplaterecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`RecipientDeleteTemplateRecipientInternalServerError`](./src/documenso_sdk/models/recipientdeletetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateCreateTemplateDirectLinkInternalServerError`](./src/documenso_sdk/models/templatecreatetemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateDeleteTemplateDirectLinkInternalServerError`](./src/documenso_sdk/models/templatedeletetemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`TemplateToggleTemplateDirectLinkInternalServerError`](./src/documenso_sdk/models/templatetoggletemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 89 methods.*
* [`ResponseValidationError`](./src/documenso_sdk/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
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
