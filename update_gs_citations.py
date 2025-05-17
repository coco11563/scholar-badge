import json
from scholarly import scholarly

# 你的 Google Scholar 用户ID
USER_ID = "YGwukbUAAAAJ"

def fetch_citations(user_id):
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["indices"])
    citations = author["citedby"]
    return citations

def update_badge_json(citations, filepath="gs_data_shieldsio.json"):
    badge = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citations),
        "color": "9cf",
        "logo": "Google Scholar"
    }
    with open(filepath, "w") as f:
        json.dump(badge, f, indent=2)

if __name__ == "__main__":
    try:
        citations = fetch_citations(USER_ID)
        update_badge_json(citations)
        print(f"Updated badge to {citations} citations.")
    except Exception as e:
        print(f"Error updating badge: {e}")
