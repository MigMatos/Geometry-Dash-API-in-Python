# Geometry Dash API (in python)

> [!WARNING]
> This GD API will no longer have support, in case of errors or bugs you will have to resolve them on your own.

**Clean JSON from Geometry Dash API (write in python)**

You can add GDPS in `api/settings.json`  (You can put optional `gjp2` for `2.2 GDPS` for search profile/level requests and configure in `api/gd_target_api.py`)

## ✨ Features:
- Demonlist
- Platform levels
- Custom settings
- Search levels
- Search profiles
- Youtube downloads
- Send messages

**Example for search profile** 

```python
import asyncio
from api.gd_target_api import get_search_profile

json_data = asyncio.run(get_search_profile(profile="obeygdbot",server="robtop"))
print(json_data)
```
> [!NOTE]
> You can view more examples in [server.py file](https://github.com/MigMatos/Geometry-Dash-API-in-Python/blob/main/server.py)
