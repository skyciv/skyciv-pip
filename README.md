# What is this?

A fast way to interact with the SkyCiv API using Python 3.

## Usage

`pip3 install skyciv`

then...

```
>>> import skyciv

>>> data = {...} // [See API documentation](https://skyciv.com/api/v3)

>>> options = {
    version: 3,
    http_or_https: 'https'
}

>>> results = skyciv.request(data, options)
```

## Data

The data parameter is required and take the JSON object that describes your model and the functions you would like to run. [See API documentation](https://skyciv.com/api/v3)

## Options

The options parameter is optional and takes and object containing two keys:

* *version* - _1 | 2 | 3_ (Defaults to 3)
* *http_or_https* - _http | https_ (Defaults to https)