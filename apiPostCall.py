# %%
import requests
response = requests.post( "http://127.0.0.1:5000/" )
response.raise_for_status

# %%
import requests
response = requests.post( "http://127.0.0.1:5000/" )
response.raise_for_status

# %%
import json
json.loads(response.content.decode( "utf-8" ))

# %%
file = { "image" : open( "sample.jpg" , "rb" )}
headers = { "type" : "multipart/image" }

# %%
URL = "http://127.0.0.1:5000"
filter = "contour"

# %%
response = requests.post( f"{URL}/{filter}",headers=headers, files=file)

# %%
response.raise_for_status

# %%
from PIL import Image
import io
image = Image.open(io.BytesIO(response.content))
image.save( "response.jpg" , "JPEG" )
image


