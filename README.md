# XBackBoneApi Python Wrapper

This project is a Python wrapper for the XBackBone API. It provides a simple way to interact with the API using Python.

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

Then, create an instance of the class, passing your API token and the base URL of the XBackBone API:
```python
api = XBackBoneApi('your-token', 'https://your-xbackbone-instance.com')
```

Now you can use the methods of the `XBackBoneApi` class to interact with the API.

## Upload an image
```python
response = api.upload_image('path/to/your/image.png')
```
## Get home data
```python
home_data = api.get_home_data('your-session-cookie')
```
## Add a tag
```python
response = api.add_tag('your-tag', 'media-id', 'your-session-cookie')
```
## Get the latest ID
```python
latest_id = api.get_latest_id('your-session-cookie')
```
## Dependencies

This package depends on the `requests` and `lxml` libraries.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
