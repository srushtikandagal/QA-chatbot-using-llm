import weaviate
import weaviate.classes as wvc

client = weaviate.connect_to_wcs(
    cluster_url="ntwk url",
    auth_credentials=weaviate.auth.AuthApiKey("Add ur key"),
    headers={
        "X-OpenAI-Api-Key": "Use your open Api key"
    }
)