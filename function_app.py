import azure.functions as func
import logging

import json
from urllib.parse import urlparse, parse_qs

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

"""
# Example 1: string splitting on comma
Parse query parameters as comma-separated list by splitting the string on ','

Accepts:
comma-separated list in one parameter (non-standard)
/articles?id=151.010.001,151.010.002,151.010.003

concetanated parameters
/articles?id=151.010.001?id=151.010.002?id=151.010.003

Note: Trailing comma or no ids results in additional 'empty' value (can be filtered out)
/articles?id=151.010.001 -> ["151.010.001", ""]
/articles?id= -> [""]
/articles= -> [""]

"""
@app.route(route="ex1/articles",
           methods=('GET',))
def http_get_articles_split(req: func.HttpRequest) -> func.HttpResponse: 
    # Get 'id' param or default to empty string
    article_param = req.params.get("id", "")
    logging.info(f"article_id query param \"{article_param}\", {type(article_param)}")

    # split string on comma
    articles = article_param.split(",")
    logging.info(f"articles list {articles}, {type(articles)}")

    # remove duplicates
    articles = list(set(articles))

    return func.HttpResponse(json.dumps({
        "articles": articles
    }))

"""
# Example 2: parse with urllib
use urllib to parse urls and query strings

concetanated parameters
/articles?id=151.010.001?id=151.010.002?id=151.010.003

Note: Requires 'urllib' package"
pip install urllib
"""
@app.route(route="ex2/articles",
           methods=('GET',))
def http_get_articles_urllib(req: func.HttpRequest) -> func.HttpResponse: 
    # use urllib to parse query params from url
    query_params = parse_qs(urlparse(req.url).query)
    logging.info(f"quary parameters {query_params}, {type(query_params)}")

    # get article ids from query params or default to empty list
    articles = query_params.get("id", [])
    logging.info(f"articles list {articles}, {type(articles)}")

    # remove duplicates
    articles = list(set(articles))

    return func.HttpResponse(json.dumps({
        "articles": articles
    }))