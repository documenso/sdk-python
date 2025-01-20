<!-- Start SDK Example Usage [usage] -->
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