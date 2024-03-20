# pyfunc-queryparams
Azure functions app for testing how passing arrays as query parameters can be handled in http triggers. Using the v2 Python runtime, tested using python 3.11.8

## Standard method
Passing the query parameter multiple times in the same url leads to the parameters being concatenated into an array:

``/articles?id=100.111.002&id=100.112.221&id=100.152.072&id=100.172.050``

returns a list of 4 articles
- 100.111.002
- 100.112.221
- 100.152.072
- 100.172.050

Azure provides native support handling this in the HttpRequest class, but concatenates all entries to a comma-separated string. This means the entries need to be manually casted to a list. Alternatively, python's **urllib** module can be used to parse the url and querystring, bypassing Azure's handling by acting directly on the url.

## Alternative
Because Azure's implementation requires that the querystring be manually split, a single parameter containing a comma-separated string of entries can be passed:

``/articles?id=100.111.002,100.112.221,100.152.072,100.172.050``

This provides the same result, but requires that the string is manually split into a list. This method is not generally accepted and cannot be used with urllib.

> Note: Handling the query parameters as a comma-separated list can lead to problems if the parameters contain commas (e.g. €736,00 / 1,000,000 / {"id":"100.112.222","model":"HGC 10 S 20"})
