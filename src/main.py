from fastapi import FastAPI

app = FastAPI()


@app.get("/common/healthcheck")
def healthcheck():
    return {"status": "ok"}
