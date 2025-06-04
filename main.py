from langchain.utilities import SearxSearchWrapper

# Replace with your SearXNG instance URL
searx_host = "http://localhost:8080"

# Create a SearxSearchWrapper instance
s = SearxSearchWrapper(searx_host=searx_host)

# Perform a search
results = s.run("what is a large language model?")
print(results)