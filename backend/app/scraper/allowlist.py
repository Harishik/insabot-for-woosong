from urllib.parse import urlparse

ALLOWED_DOMAINS = {
    "english.wsu.ac.kr",
    "engforeign.wsu.ac.kr",
    "dorm.wsu.ac.kr",
    "wkli.wsu.ac.kr",
}

EXCLUDED_PATH_KEYWORDS = {
    "logout",
    "login",
    "admin",
    "member",
    "private",
}

SEED_URLS = [
    "https://english.wsu.ac.kr/main/index.jsp",
    "https://english.wsu.ac.kr/page/index.jsp?code=eng0206",
    "https://english.wsu.ac.kr/page/index.jsp?code=eng0302",
    "https://english.wsu.ac.kr/page/index.jsp?code=eng040403a",
    "https://english.wsu.ac.kr/page/index.jsp?code=eng050101a",
    "https://engforeign.wsu.ac.kr/proc/engforeign_event.jsp",
    "https://dorm.wsu.ac.kr/main/",
    "https://wkli.wsu.ac.kr/",
]


def is_allowed_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    hostname = (parsed.hostname or "").lower()
    if hostname not in ALLOWED_DOMAINS:
        return False
    lowered_path = parsed.path.lower()
    return not any(keyword in lowered_path for keyword in EXCLUDED_PATH_KEYWORDS)
