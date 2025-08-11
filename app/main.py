from fastapi import FastAPI
from app.hello.hello_router import router as hello_router

app = FastAPI()

# Include the hello router
app.include_router(hello_router)

@app.get("/")
async def root():
    return {"message": "Root endpoint working"}
