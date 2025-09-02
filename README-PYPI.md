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


### [documents](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md)

* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#update) - Update document
* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#find) - Find documents
* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#get) - Get document
* [create_v0](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#create_v0) - Create document
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#delete) - Delete document
* [distribute](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#distribute) - Distribute document
* [redistribute](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#redistribute) - Redistribute document
* [duplicate](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documents/README.md#duplicate) - Duplicate document

#### [documents.fields](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#get) - Get document field
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#create) - Create document field
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#create_many) - Create document fields
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#update) - Update document field
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#update_many) - Update document fields
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsfields/README.md#delete) - Delete document field

#### [documents.recipients](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#get) - Get document recipient
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#create) - Create document recipient
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#create_many) - Create document recipients
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#update) - Update document recipient
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#update_many) - Update document recipients
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/documentsrecipients/README.md#delete) - Delete document recipient

### [embedding](https://github.com/documenso/sdk-python/blob/master/docs/sdks/embedding/README.md)

* [embedding_presign_create_embedding_presign_token](https://github.com/documenso/sdk-python/blob/master/docs/sdks/embedding/README.md#embedding_presign_create_embedding_presign_token) - Create embedding presign token
* [embedding_presign_verify_embedding_presign_token](https://github.com/documenso/sdk-python/blob/master/docs/sdks/embedding/README.md#embedding_presign_verify_embedding_presign_token) - Verify embedding presign token

### [templates](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md)

* [find](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#find) - Find templates
* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#get) - Get template
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#update) - Update template
* [duplicate](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#duplicate) - Duplicate template
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#delete) - Delete template
* [use](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templates/README.md#use) - Use template

#### [templates.direct_link](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlinksdk/README.md)

* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlinksdk/README.md#create) - Create direct link
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlinksdk/README.md#delete) - Delete direct link
* [toggle](https://github.com/documenso/sdk-python/blob/master/docs/sdks/directlinksdk/README.md#toggle) - Toggle direct link

#### [templates.fields](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md)

* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#create) - Create template field
* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#get) - Get template field
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#create_many) - Create template fields
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#update) - Update template field
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#update_many) - Update template fields
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesfields/README.md#delete) - Delete template field

#### [templates.recipients](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md)

* [get](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#get) - Get template recipient
* [create](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#create) - Create template recipient
* [create_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#create_many) - Create template recipients
* [update](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#update) - Update template recipient
* [update_many](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#update_many) - Update template recipients
* [delete](https://github.com/documenso/sdk-python/blob/master/docs/sdks/templatesrecipients/README.md#delete) - Delete template recipient

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

    res = documenso.documents.update(document_id=9701.92,
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

    res = documenso.documents.update(document_id=9701.92)

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

        res = documenso.documents.update(document_id=9701.92)

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
        if isinstance(e, models.DocumentUpdateDocumentBadRequestError):
            print(e.data.message)  # str
            print(e.data.code)  # str
            print(e.data.issues)  # Optional[List[documenso_sdk.DocumentUpdateDocumentBadRequestIssue]]
```

### Error Classes
**Primary error:**
* [`DocumensoError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documensoerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (99)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`DocumensoError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documensoerror.py)**:
* [`DocumentUpdateDocumentBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentupdatedocumentbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`DocumentFindDocumentsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentfinddocumentsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`DocumentGetDocumentWithDetailsByIDBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetdocumentwithdetailsbyidbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`DocumentCreateDocumentTemporaryBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreatedocumenttemporarybadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`DocumentDeleteDocumentBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdeletedocumentbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`DocumentSendDocumentBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentsenddocumentbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`DocumentResendDocumentBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentresenddocumentbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`DocumentDuplicateDocumentBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentduplicatedocumentbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateFindTemplatesBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatefindtemplatesbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateGetTemplateByIDBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategettemplatebyidbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateUpdateTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateupdatetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateDuplicateTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateduplicatetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateDeleteTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateCreateDocumentFromTemplateBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatedocumentfromtemplatebadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokenbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokenbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldGetDocumentFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgetdocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldCreateDocumentFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldCreateDocumentFieldsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldUpdateDocumentFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldUpdateDocumentFieldsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldDeleteDocumentFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletedocumentfieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientGetDocumentRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgetdocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientCreateDocumentRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientCreateDocumentRecipientsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientUpdateDocumentRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientUpdateDocumentRecipientsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientDeleteDocumentRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletedocumentrecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldCreateTemplateFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldGetTemplateFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgettemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldCreateTemplateFieldsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldUpdateTemplateFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldUpdateTemplateFieldsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`FieldDeleteTemplateFieldBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletetemplatefieldbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientGetTemplateRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgettemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientCreateTemplateRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientCreateTemplateRecipientsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientUpdateTemplateRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientUpdateTemplateRecipientsBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientsbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`RecipientDeleteTemplateRecipientBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletetemplaterecipientbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateCreateTemplateDirectLinkBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateDeleteTemplateDirectLinkBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`TemplateToggleTemplateDirectLinkBadRequestError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatetoggletemplatedirectlinkbadrequesterror.py): Invalid input data. Status code `400`. Applicable to 1 of 43 methods.*
* [`DocumentFindDocumentsNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentfinddocumentsnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 43 methods.*
* [`DocumentGetDocumentWithDetailsByIDNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetdocumentwithdetailsbyidnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 43 methods.*
* [`TemplateFindTemplatesNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatefindtemplatesnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 43 methods.*
* [`TemplateGetTemplateByIDNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategettemplatebyidnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 43 methods.*
* [`FieldGetDocumentFieldNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgetdocumentfieldnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 43 methods.*
* [`RecipientGetDocumentRecipientNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgetdocumentrecipientnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 43 methods.*
* [`FieldGetTemplateFieldNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgettemplatefieldnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 43 methods.*
* [`RecipientGetTemplateRecipientNotFoundError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgettemplaterecipientnotfounderror.py): Not found. Status code `404`. Applicable to 1 of 43 methods.*
* [`DocumentUpdateDocumentInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentupdatedocumentinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`DocumentFindDocumentsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentfinddocumentsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`DocumentGetDocumentWithDetailsByIDInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentgetdocumentwithdetailsbyidinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`DocumentCreateDocumentTemporaryInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentcreatedocumenttemporaryinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`DocumentDeleteDocumentInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentdeletedocumentinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`DocumentSendDocumentInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentsenddocumentinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`DocumentResendDocumentInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentresenddocumentinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`DocumentDuplicateDocumentInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/documentduplicatedocumentinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateFindTemplatesInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatefindtemplatesinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateGetTemplateByIDInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templategettemplatebyidinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateUpdateTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateupdatetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateDuplicateTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templateduplicatetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateDeleteTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateCreateDocumentFromTemplateInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatedocumentfromtemplateinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`EmbeddingPresignCreateEmbeddingPresignTokenInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresigncreateembeddingpresigntokeninternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`EmbeddingPresignVerifyEmbeddingPresignTokenInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/embeddingpresignverifyembeddingpresigntokeninternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldGetDocumentFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgetdocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldCreateDocumentFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldCreateDocumentFieldsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatedocumentfieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldUpdateDocumentFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldUpdateDocumentFieldsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatedocumentfieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldDeleteDocumentFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletedocumentfieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientGetDocumentRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgetdocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientCreateDocumentRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientCreateDocumentRecipientsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatedocumentrecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientUpdateDocumentRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientUpdateDocumentRecipientsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatedocumentrecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientDeleteDocumentRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletedocumentrecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldCreateTemplateFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldGetTemplateFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldgettemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldCreateTemplateFieldsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldcreatetemplatefieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldUpdateTemplateFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldUpdateTemplateFieldsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fieldupdatetemplatefieldsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`FieldDeleteTemplateFieldInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/fielddeletetemplatefieldinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientGetTemplateRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientgettemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientCreateTemplateRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientCreateTemplateRecipientsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientcreatetemplaterecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientUpdateTemplateRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientUpdateTemplateRecipientsInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientupdatetemplaterecipientsinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`RecipientDeleteTemplateRecipientInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/recipientdeletetemplaterecipientinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateCreateTemplateDirectLinkInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatecreatetemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateDeleteTemplateDirectLinkInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatedeletetemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
* [`TemplateToggleTemplateDirectLinkInternalServerError`](https://github.com/documenso/sdk-python/blob/master/./src/documenso_sdk/models/templatetoggletemplatedirectlinkinternalservererror.py): Internal server error. Status code `500`. Applicable to 1 of 43 methods.*
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
    server_url="https://app.documenso.com/api/v2-beta",
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.update(document_id=9701.92)

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
