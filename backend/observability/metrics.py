from prometheus_client import Counter

REQUEST_COUNTER = Counter(
    "requests_total",
    "Total requests",
)
