from pypdf import PdfReader
from vecDBManager import client

try:
    # ===== define collection =====

    # Using PyPDF2 as a better PDF reader

    try:
        reader = PdfReader("./stephen_hawking_a_brief_history_of_time.pdf")
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        print(text)
    except Exception as e:
        print(f"An error occurred: {e}")

    print(text)
    chunk_size = 5000
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Create an array of objects with text and chunk index
    chunk_objs = [{"text": chunk, "chunk_index": index} for index, chunk in enumerate(chunks)]
    print(chunk_objs)

    # ===== save chunks into BookData collection =====
    book_data = client.collections.get("BookData")
    resp = book_data.data.insert_many(chunk_objs)
    print(resp)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()  # Close client gracefully