def getLink(data):
    return {
        "id": str(data["_id"]),
        "sublink": str(data["sublink"]),
        "redirectTo": str(data["redirectTo"]),
    }