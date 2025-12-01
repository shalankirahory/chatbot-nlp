/*
"""
Filename: script.js
Author: Shalanki Rahory
Date: 2025-12-01
Version: 1.0
Description: This script is chatbot NLP Project JavaScript script used in Linux.
"""
# License: MIT License
# Contact: srahory2001@gmail.com
*/

async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (message === "") return;

    addMessage(message, "user-msg");
    input.value = "";

    const response = await fetch(`http://127.0.0.1:8000/chat?q=${message}`);
    const data = await response.json();

    addMessage(data.reply, "bot-msg");
}

function addMessage(text, className) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = className;
    msg.innerText = text;
    chatBox.appendChild(msg);

    chatBox.scrollTop = chatBox.scrollHeight;
}
