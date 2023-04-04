import azure.functions as func
import json
import requests

app = func.FunctionApp()

# NewsAPI endpoint
newsapi_endpoint = "https://newsapi.org/v2/"
# top-headlines
# everything
#

# Google News endpoint
google_news_endpoint = "https://news.google.com/rss"

# NewsAPI API key
API_KEY = "z68EFScoSUGigocjGZcVJw=="
newsapi_key = "1b913c719ac945f2987498fb92740331"

@app.function_name(name="news-pulse-news")
@app.route(route="news") # HTTP Trigger
def new(req: func.HttpRequest) -> func.HttpResponse:
    
    api_key = req.params.get('apiKey')
    if api_key != API_KEY:
        return  func.HttpResponse("Not autenticated", status_code=403)
    
    # meu_dict = {"chave": "valor"}
    # meu_json = json.dumps(meu_dict)
    
    # return meu_json
    
    pagesize = req.params.get('pagesize', 100)
    lang = req.params.get('lang', 'eng')
    
    newsapi_response \
        = requests.get(f"{newsapi_endpoint}everything?apiKey="
                       f"{newsapi_key}&sortBy=popularity"
                       f"&pageSize={pagesize}"
                       f"&sources=blasting-news-br,globo,google-news-br,info-money"
                       f"&language={lang}")

    if newsapi_response.status_code != 200:
        return json.dumps({'error': 'Error'})

    return json.dumps(newsapi_response.json())
    