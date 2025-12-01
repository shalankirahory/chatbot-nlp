#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: predict.py
Author: Shalanki Rahory
Date: 2025-12-01
Version: 1.0
Description: This script is chatbot NLP Project python script used in Linux.
"""
# License: MIT License
# Contact: srahory2001@gmail.com

import json, random, pickle
from preprocess import clean_text

model = pickle.load(open("../model/chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("../model/vectorizer.pkl", "rb"))
intents = json.load(open("../data/intents.json"))["intents"]

def get_response(user_input):
    clean = clean_text(user_input)
    X = vectorizer.transform([clean])
    intent = model.predict(X)[0]

    for item in intents:
        if item["intent"] == intent:
            return random.choice(item["responses"])
    
    return "I'm sorry, I didn't understand that."
