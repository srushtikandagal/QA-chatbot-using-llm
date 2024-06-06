from vecDBManager import client

collection_name = "BookData"

chunks = client.collections.get(collection_name)
response = chunks.generate.near_text(
    query="history of git",
    limit=3,
    grouped_task="Summarize the key information here in bullet points"
)

print(response.generated)