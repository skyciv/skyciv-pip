import json
import http.client as httplib

def request(data, options={}):
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

    stringified_data = json.dumps(data, separators=(",", ":"))

    conn.request("POST", "/v" + str(version), stringified_data, headers)

    raw_res = conn.getresponse()
    res_data = raw_res.read()
    conn.close()

    parsed_res = json.loads(res_data)

    if (parsed_res["response"]["status"] == 0):
        return parsed_res
    else:
        raise Exception("Unsuccessful solve with message: " + parsed_res["response"]["msg"])
