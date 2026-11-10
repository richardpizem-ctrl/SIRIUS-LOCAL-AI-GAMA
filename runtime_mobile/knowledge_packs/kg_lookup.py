import unicodedata


def lookup_school_relation(pack_manager, entity_id: int, relation_id: int) -> list[dict]:
    kg = pack_manager.get_entry("gama_school_kg", "kg.school.sk")
    if kg is None or kg.get("schema_version") != 1:
        raise ValueError("Školský KG chýba alebo má nepodporovanú verziu.")

    return [
        {
            "target_id": edge["target"],
            "answer": kg["entities"][str(edge["target"])],
            "source": kg["sources"][str(edge["provenance"])],
        }
        for edge in kg["graph"]["edges"]
        if edge["source"] == entity_id and edge["rel"] == relation_id
    ]


def normalize(text: str) -> str:
    return unicodedata.normalize("NFC", text.casefold())


def without_accents(text: str) -> str:
    return "".join(
        char for char in unicodedata.normalize("NFD", normalize(text))
        if not unicodedata.combining(char)
    )


def parse_school_question(text: str):
    if not isinstance(text, str):
        return None

    parts = text.strip().rstrip("?").split(maxsplit=2)
    if len(parts) == 3 and without_accents(" ".join(parts[:2])) == "co vytvara":
        return parts[2], parts[1]
    return None


def query_school_graph(pack_manager, entity: str, relation: str) -> dict:
    kg = pack_manager.get_entry("gama_school_kg", "kg.school.sk")
    if kg is None or kg.get("schema_version") != 1:
        return {"status": "error", "reason": "school_kg_unavailable"}

    form = normalize(entity)
    ids = kg["lexicon"].get(form)
    if ids is None:
        ids = sorted({
            entity_id
            for alias, candidates in kg["lexicon"].items()
            if without_accents(alias) == without_accents(form)
            for entity_id in candidates
        })

    if len(ids) > 1:
        return {"status": "ambiguous", "candidates": [
            kg["entities"][str(entity_id)] for entity_id in ids
        ]}

    relation_ids = [
        int(key) for key, label in kg["relations"].items()
        if without_accents(label) == without_accents(relation)
    ]
    if not ids or len(relation_ids) != 1:
        return {"status": "not_found", "entity": entity, "relation": relation}

    matches = lookup_school_relation(pack_manager, ids[0], relation_ids[0])
    return {"status": "ok" if matches else "not_found", "results": matches}
