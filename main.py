from fastapi import FastAPI

app = FastAPI()
data_tree = [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}, {"key3": }]

@app.get("/")
async def root():
    return data_tree
