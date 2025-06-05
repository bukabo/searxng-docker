from langchain.utilities import SearxSearchWrapper

# Replace with your SearXNG instance URL
searx_host = "http://localhost:8080"

# Create a SearxSearchWrapper instance
s = SearxSearchWrapper(searx_host=searx_host, unsecure=False)

# Perform a search
results = s.run("что такое llm?")
print(results)