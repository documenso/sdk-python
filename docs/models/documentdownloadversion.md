# DocumentDownloadVersion

The version of the document to download. "signed" returns the completed document with signatures, "original" returns the original uploaded document.

## Example Usage

```python
from documenso_sdk.models import DocumentDownloadVersion

value = DocumentDownloadVersion.ORIGINAL
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `ORIGINAL` | original   |
| `SIGNED`   | signed     |