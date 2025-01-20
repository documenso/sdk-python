# ErrorBADREQUEST

The error information


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `message`                                              | *str*                                                  | :heavy_check_mark:                                     | The error message                                      | Invalid input data                                     |
| `code`                                                 | *str*                                                  | :heavy_check_mark:                                     | The error code                                         | BAD_REQUEST                                            |
| `issues`                                               | List[[models.Issues](../models/issues.md)]             | :heavy_minus_sign:                                     | An array of issues that were responsible for the error | []                                                     |