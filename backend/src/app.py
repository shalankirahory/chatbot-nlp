#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: app.py
Author: Shalanki Rahory
Date: 2025-12-01
Version: 1.0
Description: This script is chatbot NLP Project python script used in Linux.
"""
# License: MIT License
# Contact: srahory2001@gmail.com

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from predict import get_response

app = FastAPI(title="Chatbot Backend")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Chatbot API is running"}

@app.get("/chat")
def chat(q: str):
    reply = get_response(q)
    return {"reply": reply}
