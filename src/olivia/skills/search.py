"""Wikipedia lookups + multi-engine web search / open commands."""

import re
import webbrowser

from olivia.core.speech import sp, speak

# Search-engine URL templates keyed by trigger word. {q} = url query.
SEARCH_ENGINES = {
    "youtube": "https://www.youtube.com/results?search_query={q}",
    "duckduckgo": "https://duckduckgo.com/?q={q}",
    "bing": "https://www.bing.com/search?q={q}",
    "yahoo": "https://search.yahoo.com/search?p={q}",
    "wikipedia": "https://www.wikipedia.org/search-redirect.php?search={q}",
    "wiktionary": "https://en.wiktionary.org/wiki/{q}",
    "wikiquote": "https://en.wikiquote.org/wiki/{q}",
    "wikisource": "https://en.wikisource.org/wiki/{q}",
    "wikibooks": "https://en.wikibooks.org/wiki/{q}",
    "wikinews": "https://en.wikinews.org/wiki/{q}",
    "wikidata": "https://www.wikidata.org/wiki/{q}",
    "wikiversity": "https://en.wikiversity.org/wiki/{q}",
    "wikispecies": "https://species.wikimedia.org/wiki/{q}",
    "wikimedia": "https://commons.wikimedia.org/wiki/{q}",
    "wikivoyage": "https://en.wikivoyage.org/wiki/{q}",
    "stackoverflow": "https://stackoverflow.com/search?q={q}",
    "quora": "https://www.quora.com/search?q={q}",
    "coursera": "https://www.coursera.org/search?query={q}",
    "edx": "https://www.edx.org/search?query={q}",
    "udemy": "https://www.udemy.com/search/?q={q}",
    "udacity": "https://www.udacity.com/course/search?query={q}",
    "amazon": "https://www.amazon.in/s?k={q}",
    "flipkart": "https://www.flipkart.com/search?q={q}",
    "snapdeal": "https://www.snapdeal.com/search?keyword={q}",
    "shopclues": "https://www.shopclues.com/search?q={q}",
    "myntra": "https://www.myntra.com/search?q={q}",
    "jabong": "https://www.jabong.com/search?q={q}",
    "paytm": "https://paytm.com/shop/search?q={q}",
    "ebay": "https://www.ebay.com/sch/i.html?_nkw={q}",
    "facebook": "https://www.facebook.com/search/top/?q={q}",
    "instagram": "https://www.instagram.com/explore/tags/{q}",
    "twitter": "https://twitter.com/search?q={q}",
    "linkedin": "https://www.linkedin.com/search/results/index/?keywords={q}",
    "snapchat": "https://www.snapchat.com/search/{q}",
    "vimeo": "https://vimeo.com/search?q={q}",
    "dailymotion": "https://www.dailymotion.com/search/{q}",
    "twitch": "https://www.twitch.tv/search?q={q}",
    "netflix": "https://www.netflix.com/search?q={q}",
    "hulu": "https://www.hulu.com/search?q={q}",
    "disney": "https://disney.go.com/search?q={q}",
    "hbo": "https://www.hbo.com/search?q={q}",
    "hotstar": "https://www.hotstar.com/search?q={q}",
    "spotify": "https://open.spotify.com/search/{q}",
    "soundcloud": "https://soundcloud.com/search?q={q}",
    "tidal": "https://tidal.com/search?q={q}",
}

# Sites the 'open <site>' command launches directly.
OPEN_SITES = {
    "firefox": "https://www.mozilla.org/en-US/firefox/new/",
    "facebook": "https://www.facebook.com/",
    "whatsapp": "https://web.whatsapp.com/",
    "instagram": "https://www.instagram.com/",
    "twitter": "https://twitter.com/",
    "linkedin": "https://www.linkedin.com/",
    "pinterest": "https://www.pinterest.com/",
    "quora": "https://www.quora.com/",
    "amazon": "https://www.amazon.in/",
    "ebay": "https://www.ebay.com/",
    "netflix": "https://www.netflix.com/",
    "spotify": "https://open.spotify.com/",
    "snapchat": "https://www.snapchat.com/",
    "stack overflow": "https://www.stackoverflow.com/",
    "flipkart": "https://www.flipkart.com/",
    "hackerearth": "https://www.hackerearth.com/",
    "bing": "https://www.bing.com/",
    "duckduckgo": "https://duckduckgo.com/",
    "github": "https://www.github.com/",
    "wikipedia": "https://www.wikipedia.org/",
}


def tell_me_about(query):
    """Speak the first 500 chars of a Wikipedia page (from 'tell me about X')."""
    import wikipedia

    m = re.search("tell me about (.*)", query)
    if not m:
        return
    try:
        page = wikipedia.page(m.group(1))
        sp(page.content[:500])
    except Exception as e:
        speak(str(e))


def who_is(query):
    """Speak a 2-sentence Wikipedia summary (from 'who is X')."""
    import wikipedia

    m = re.search("who is (.*)", query)
    if not m:
        return
    summary = wikipedia.summary(m.group(1), sentences=2)
    speak("According to Wikipedia")
    print(summary)
    speak(summary)


def search(query):
    """Route a 'search ...' command to the matching engine, default Google."""
    sp("Searching ...")
    q = query.replace("search ", "").replace(" on ", "")
    for name, template in SEARCH_ENGINES.items():
        if name in q:
            q = q.replace(name, "").strip()
            webbrowser.open(template.format(q=q))
            return
    if "google" in q:
        q = q.replace("google", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={q}&sourceid=olivia")


def open_site(query):
    """Route an 'open <site>' command; unknown terms go to DuckDuckGo."""
    q = query.replace("open", "")
    for name, url in OPEN_SITES.items():
        if name in q:
            speak(f"{name} is opening")
            webbrowser.open(url)
            return
    if "reddit" in q:
        m = re.search("reddit (.*)", q)
        url = "https://www.reddit.com/"
        if m:
            url += "r/" + m.group(1).strip()
        webbrowser.open(url)
        sp("The Reddit content has been opened for you Sir.")
        return
    webbrowser.open(f"https://duckduckgo.com/?q=%21+{q.strip()}&ia=olivia")


def google_fallback(query):
    """Open a plain Google search for an unrecognized query."""
    webbrowser.open(f"https://www.google.com/search?q={query}&sourceid=olivia")
