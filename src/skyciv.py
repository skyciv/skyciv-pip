import json
import http.client as httplib


def request(api_object: dict, options={}):
    """Makes a request to the SkyCiv API using the provided API object and options.

    Args:
        api_object: Your SkyCiv API Object - see docs below for more information.
        options: An optional dictionary with the following parameters
                 - http_or_https: string ("http" | "https"), defaults to "https"
                 - version: integer (2 | 3), defaults to 3

    Return:
        skyciv_response: The return value is a parsed Dictionary.

    Sample:
        options = {"http_or_https": "https"}
        skyciv_response = skyciv.request(api_object, options)
        # Do something with the response

    [SkyCiv API documentation](https://skyciv.com/api/v3/docs/the-request-object)

    """

    port = 8085
    version = 3

    if hasattr(options, "http_or_https"):
        # Validate options
        allowable_ports = ["http", "https"]
        if not any([x in options["http_or_https"] for x in allowable_ports]):
            raise Exception("Invalid argument passed to option http_or_https.")

        # Set port
        if (options["http_or_https"] == "http"):
            port = 8086

        # Set version
        if hasattr(options, "version"):
            version = options["version"]

    headers = {"Content-Type": "application/json"}
    conn = httplib.HTTPSConnection("api.skyciv.com", port)

    # Check if api_object has already been stringified, stringify it if not.
    stringified_data = api_object
    if not isinstance(stringified_data, str):
        stringified_data = json.dumps(api_object, separators=(",", ":"))

    conn.request("POST", "/v" + str(version), stringified_data, headers)

    raw_res = conn.getresponse()
    res_data = raw_res.read()
    conn.close()

    parsed_res = json.loads(res_data)

    if (parsed_res["response"]["status"] != 0):
        print(
            f'Unsuccessful solve with message: {parsed_res["response"]["msg"]}')

    return parsed_res
