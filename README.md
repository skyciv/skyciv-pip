# What is this?

A fast way to interact with the SkyCiv API.

## Usage

`pip3 install skyciv`

then...

### Import

```py
import skyciv
```

## Options

**The options object is optional and** takes:

* *version* - _2 | 3_ (Defaults to 3)
* *http_or_https* - _http | https_ (Defaults to https)

## Methods

### `skyciv.request(apiObject, callback?, options?)`
Make a request to the SkyCiv API. The callback function receives the parsed response.

```py
skyciv_response = skyciv.request(api_object, options)
# Do something with the response
```

## API Object
Visit the [API docs](https://skyciv.com/api/v3/docs/getting-started) for instructions on how to create a SkyCiv API object.

## Changelog

| Version  | Breaking          | Description     |
| :---     | :---              | :---            |
| 1.0.1    | false             | • Changed `skyciv.request()` to print msg if SkyCiv returns error rather than throw an exception |
| 1.0.0    | -                 | Initial release |