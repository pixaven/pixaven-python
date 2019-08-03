[![Pixaven](media/readme-header.png "Pixaven: GPU-powered Image Processing Platform")](https://www.pixaven.com)

<p align="center">
Pixaven is a modern, GPU-powered image processing API.<br>We transform, enhance, adjust, crop, stylize, filter and watermark your images with blazing speed.
</p>

---
<p align="center">
<strong>The official Python integration for the Pixaven API.</strong><br>
<br>
<img src="https://img.shields.io/pypi/v/pixaven?style=flat&color=success"/>
<img src="https://img.shields.io/pypi/pyversions/pixaven?style=flat&color=success"/>
<img src="https://img.shields.io/snyk/vulnerabilities/github/pixaven/pixaven-python?style=flat&color=success"/>
<img src="https://img.shields.io/github/issues-raw/pixaven/pixaven-python?style=flat&color=success"/>
<img src="https://img.shields.io/pypi/l/pixaven?style=flat&color=success"/>
<img src="https://img.shields.io/twitter/follow/pixaven?label=Follow%20Us&style=flat&color=success&logo=twitter"/>
</p>

---

### Documentation
See the [Pixaven API docs](https://docs.pixaven.com/).


### Installation
```bash
$ pip install pixaven
```

### Quick examples
Pixaven API enables you to provide your images for processing in two ways - by uploading them directly to the API ([Image Upload](https://docs.pixaven.com/requests/image-upload)) or by providing a publicly available image URL ([Image Fetch](https://docs.pixaven.com/requests/image-fetch)).

You may also choose your preferred [response method](https://docs.pixaven.com/introduction#choosing-response-method-and-format) on a per-request basis. By default, the Pixaven API will return a [JSON response](https://docs.pixaven.com/responses/json-response-format) with rich metadata pertaining to input and output images. Alternatively, you can use [binary responses](https://docs.pixaven.com/responses/binary-responses). When enabled, the API will respond with a full binary representation of the resulting (output) image. This Python integration exposes two convenience methods for interacting with binary responses: `.toFile()` and `.toBuffer()`.

#### Image upload
Here is a quick example of uploading a local file for processing. It calls `.toJSON()` at a final step and instructs the API to return a JSON response.

```python
from pixaven import pixaven

# Pass your Pixaven API Key to the constructor
client = pixaven('your-api-key')

# Upload an image from disk, resize it to 100 x 75,
# automatically enhance, and adjust sharpness parameter.
# You'll find the full JSON metadata within the `meta` variable
err, meta = (
    client
        .upload('path/to/input.jpg')
        .resize({
            'width': 100,
            'height': 75
        })
        .auto({
            'enhance': True
        })
        .adjust({
            'unsharp': 10
        })
        .toJSON()
)

if err is not None:
    raise StandardError(err)
```

#### Image fetch
If you already have your source visuals publicly available online, we recommend using Image Fetch by default. That way you only have to send a JSON payload containing image URL and processing steps. This method is also much faster than uploading a full binary representation of the image.

```python
from pixaven import pixaven

# Pass your Pixaven API Key to the constructor
client = pixaven('your-api-key')

# Provide a publicly available image URL with `.fetch()` method,
# apply Gaussian blur using PNG as the output format.
# We'll also use `.toFile()` method and stream the output image to disk
err, meta = (
    client
        .fetch('https://www.website.com/image.jpg')
        .filter({
            'blur': {
                'mode': 'gaussian',
                'value': 10
            }
        })
        .output({
            'format': 'png'
        })
        .toFile('path/to/output.png')
)

if err is not None:
    raise StandardError(err)
```

### License
This software is distributed under the MIT License. See the [LICENSE](LICENSE) file for more information.

<p align="center"><br><br><a href="https://www.pixaven.com"><img src="media/logo-mono-light.png" alt="Pixaven" width="165" height="42"/></a></p>