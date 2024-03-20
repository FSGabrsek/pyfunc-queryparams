import azure.functions as func
import logging

import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="articles",
           methods=('GET',))
def http_get_article(req: func.HttpRequest) -> func.HttpResponse:
    article_param = req.params.get("id", [])
    logging.debug(f"article_id query param {article_param}")

    articles = article_param if isinstance(article_param, list) else [article_param]
    logging.debug(f"articles list {articles}")

    articles = list(set(articles))

    return func.HttpResponse(json.dumps({
        "articles": articles
    }))