#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: preprocess.py
Author: Shalanki Rahory
Date: 2025-12-01
Version: 1.0
Description: This script is chatbot NLP Project python script used in Linux.
"""
# License: MIT License
# Contact: srahory2001@gmail.com

import nltk, string
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
punct = string.punctuation

def clean_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in punct]
    return " ".join(tokens)
