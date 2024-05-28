import fastapi
import time
import uvicorn

app = fastapi.FastAPI()

@app.get("/test/{idx}")
def get_response(idx:int):
    time.sleep(1)
    return {"success": True, "data": idx*100}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8765, reload=True)