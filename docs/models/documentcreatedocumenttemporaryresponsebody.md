# DocumentCreateDocumentTemporaryResponseBody

Successful response


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `document`                                                                           | [models.Document](../models/document.md)                                             | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `upload_url`                                                                         | *str*                                                                                | :heavy_check_mark:                                                                   | The URL to upload the document PDF to. Use a PUT request with the file via form-data |