# TemplateFindTemplatesRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `query`                                                        | *Optional[str]*                                                | :heavy_minus_sign:                                             | The search query.                                              |
| `page`                                                         | *Optional[float]*                                              | :heavy_minus_sign:                                             | The pagination page number, starts at 1.                       |
| `per_page`                                                     | *Optional[float]*                                              | :heavy_minus_sign:                                             | The number of items per page.                                  |
| `type`                                                         | [Optional[models.QueryParamType]](../models/queryparamtype.md) | :heavy_minus_sign:                                             | Filter templates by type.                                      |