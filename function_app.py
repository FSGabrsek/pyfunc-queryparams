import azure.functions as func
import logging

import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

"""
# Example 1: string splitting on comma
Parse query parameters as comma-separated list by splitting the string on ','

Accepts:
comma-separated list in one parameter
/articles?id=151.010.001,151.010.002,151.010.003

concetanated parameters
/articles?id=151.010.001?id=151.010.002?id=151.010.003

Note: Trailing comma results in additional 'empty' value (can be filtered out)
/articles?id=151.010.001 -> ["151.010.001", ""]
"""
@app.route(route="/ex1/articles",
           methods=('GET',))
def http_get_article(req: func.HttpRequest) -> func.HttpResponse: 
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