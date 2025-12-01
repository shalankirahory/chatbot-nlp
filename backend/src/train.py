#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: train.py
Author: Shalanki Rahory
Date: 2025-12-01
Version: 1.0
Description: This script is chatbot NLP Project python script used in Linux.
"""
# License: MIT License
# Contact: srahory2001@gmail.com

import json, pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from preprocess import clean_text

print("[INFO] Loading dataset...")
with open("../data/intents.json") as f:
    intents = json.load(f)["intents"]

texts, labels = [], []

for item in intents:
    for p in item["patterns"]:
        texts.append(clean_text(p))
        labels.append(item["intent"])

print("[INFO] Vectorizing...")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

print("[INFO] Training model...")
model = LogisticRegression()
model.fit(X, labels)

print("[INFO] Saving model...")
pickle.dump(model, open("../model/chatbot_model.pkl", "wb"))
pickle.dump(vectorizer, open("../model/vectorizer.pkl", "wb"))

print("[SUCCESS] Model trained!")
