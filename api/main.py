from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from api.configurations import collection
from api.schemas import getLink
from fastapi.responses import RedirectResponse
import shortuuid


app = FastAPI()

class URL(BaseModel):
    website_URL: str

@app.get("/")
def read_root():
    return {"message": "URL shortner is working"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.post("/shorturl")
def shortURL(new_url: URL):
    originalURL = new_url.website_URL
    subLink = str(shortuuid.ShortUUID().random(length=8))
    data = collection.insert_one({"sublink": subLink, "redirectTo": originalURL})
    print(data.inserted_id)
    return {"shorturl": "https://rbly.vercel.app/"+subLink}

@app.get("/getAllUrls")
def getAllData():
    allUrls = []
    datas = collection.find()
    for data in datas:
        allUrls.append(getLink(data))
    return {"allUrls": allUrls}

@app.get("/{url_id}")
def redirectUser(url_id: str):
    data = (collection.find_one({"sublink": url_id}))
    
    if data:
        isValidCode = getLink(data)
        return RedirectResponse(url=isValidCode['redirectTo'])
    else :
        return {"status_code": 400, "message": "Invalid URL"}
    
