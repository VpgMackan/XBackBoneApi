# XBackBoneApi Python Wrapper

This project is a Python wrapper for the XBackBone API. It provides a simple way to interact with the API using Python. It doesn't support all the API endpoints, but it does support a few since I just made it for my personal use. If you want to add more endpoints feel free to make a pull request.

## Installation

You can install this package using pip:

```shell
pip install git+https://github.com/VpgMackan/XBackBoneApi
```

## Usage

First, import the XBackBoneApi class:

```python
from xbackboneapi import XBackBoneApi
```

Then, create an instance of the class, passing your API token, the base URL of the XBackBone API and your session cookie (optional but required for most routes) as parameters:

```python
api = XBackBoneApi('your-token', 'https://your-xbackbone-instance.com', session_cookie='session-cookie')
```

Now you can use the methods of the `XBackBoneApi` class to interact with the API.

If a more in-depth explanation of the methods is needed you can look at the docstrings in the code. Optionally you can look at the xbackboneapi.py file.

### Upload an image

The upload_image method requires a path to the image you want to upload. It will return a response from the API.

```python
response = api.upload_image('path/to/your/image.png')
```

The response should look something like this:

```json
{
  "message": "OK",
  "version": "3.6.3",
  "url": "https://cdn.example.com/PATHTOIMAGE.png"
}
```

### Get home data

This function will scrape the home page of your xbackbone instance and return the data.

```python
home_data = api.get_home_data()
```

### Add a tag

This function will add a tag to a media item. To get the media ID you can use the get_latest_id function. This will only work if the image you want to tag is the latest image you have uploaded.

```python
response = api.add_tag('your-tag', 'media-id')
```

### Get the latest ID

This function will scrape the home page of your xbackbone instance and return the latest media id. This function uses the get_home_data function.

```python
latest_id = api.get_latest_id()
```

## Dependencies

This package depends on the `requests`, `lxml` and `typing` packages.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
