from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Mac Calculator API",
    root_path="",
    root_path_in_servers=True
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "Server is running"}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])