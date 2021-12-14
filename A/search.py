top_50_sites_list = ["google", "youtube", "amazon", "facebook", "google.co.in", "flipkart", "wikipedia", "canva", "instagram", "microsoft", "amazon.com", "yahoo", "whatsapp", "indiatimes", "zoom", "hdfcbank", "zerodha", "linkedin", "hotstar", "office", "netflix", "live", "icicibank", "twitter", "stackoverflow","primevideo", "reddit", "onlinesbi", "godaddy", "myshopify", "moneycontrol", "grammarly", "microsoftonline", "adobe", "irctc", "freepik", "indiamart", "manoramaonline", "naukri", "wordpress", "bing", "cricbuzz", "tradingview", "ndtv", "zoho", "tumblr", "indeed", "amazonaws", "smallpdf", "myntra"]


import webbrowser
from time import sleep


for t in top_50_sites_list:
    webbrowser.open("https://google.com/search?q=search+on+"+t)

    sleep(10)


