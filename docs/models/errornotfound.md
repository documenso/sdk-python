# ErrorNOTFOUND

The error information


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `message`                                                            | *str*                                                                | :heavy_check_mark:                                                   | The error message                                                    | Not found                                                            |
| `code`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The error code                                                       | NOT_FOUND                                                            |
| `issues`                                                             | List[[models.ErrorNOTFOUNDIssues](../models/errornotfoundissues.md)] | :heavy_minus_sign:                                                   | An array of issues that were responsible for the error               | []                                                                   |