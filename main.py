from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message": "This is the root of the API"}