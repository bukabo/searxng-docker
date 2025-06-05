import requests


def search_searxng(query, base_url="http://localhost:8080", limit=5):
    """
    Простой запрос к локальному экземпляру SearXNG

    :param query: Поисковый запрос
    :param base_url: Базовый URL SearXNG (по умолчанию http://localhost:8080)
    :param limit: Количество возвращаемых результатов
    :return: Список результатов поиска
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json',
        # 'base_url': 'http://localhost:8080'
    }
    params = {
        'q': query,
        'format': 'json',
        'pageno': 1,
        'language': 'ru',
        'safesearch': '0',
        'categories': 'general',
        'time_range': '',
        'limit': limit
    }

    try:
        response = requests.post(f"{base_url}/search", params=params)
        response.raise_for_status()
        return response.json().get('results', [])
        # return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []


# Пример использования
if __name__ == "__main__":
    results = search_searxng("что такое Python", limit=1)

    print(f"Найдено результатов: {len(results)}")
    for i, result in enumerate(results, 1):
        print(f"\nРезультат {i}:")
        print(f"Заголовок: {result.get('title', 'N/A')}")
        print(f"URL: {result.get('url', 'N/A')}")
        print(f"Описание: {result.get('content', 'N/A')[:200]}...")
        print(f"Источник: {result.get('engine', 'N/A')}")