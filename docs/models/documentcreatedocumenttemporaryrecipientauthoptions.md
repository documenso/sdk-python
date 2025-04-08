# DocumentCreateDocumentTemporaryRecipientAuthOptions


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `access_auth`                                                                 | [Nullable[models.DocumentAccessAuth]](../models/documentaccessauth.md)        | :heavy_check_mark:                                                            | The type of authentication required for the recipient to access the document. |
| `action_auth`                                                                 | [Nullable[models.DocumentActionAuth]](../models/documentactionauth.md)        | :heavy_check_mark:                                                            | The type of authentication required for the recipient to sign the document.   |