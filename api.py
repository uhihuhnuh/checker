from flask import Flask, request, jsonify
from colorama import Fore, Style
import pyfiglet
import os

app = Flask(__name__)

# المفتاح الصحيح (يُنصح استخدام متغيرات البيئة)
CORRECT_KEY = os.getenv('SECRET_KEY', 'mzdk97558fjiocxdhvc4588520bbg')

@app.route('/check', methods=['POST'])
def check_cards():
    # التحقق من المفتاح
    user_key = request.headers.get('Authorization')
    if user_key != CORRECT_KEY:
        return jsonify({"status": "error", "message": "Invalid key ❌"}), 401

    # قراءة الملف المرفوع
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file uploaded"}), 400
        
    file = request.files['file']
    cards = file.read().decode('utf-8').splitlines()

    # القوائم المرجعية
    valid_card = '4400665280532431|11|2027|195'
    done_buy_cards = ['5392254658087620|05|2028|622', valid_card]
    insufficient_cards = ['5502541000007075|04|2024|044', '5129915199204128|02|2026|773']

    # معالجة البطاقات
    results = []
    for card in cards:
        cc = card.strip().replace('/', '|').replace(':', '|')
        cc_parts = cc.split('|')
        
        if cc == valid_card:
            status = "✅ Charged 13$"
        elif cc in done_buy_cards:
            status = "✓ Approved"
        elif cc in insufficient_cards:
            status = "🔥 Insufficient funds"
        else:
            status = "❌ Declined"
        
        results.append({
            "card": cc,
            "status": status
        })

    return jsonify({
        "status": "success",
        "results": results
    })

if __name__ == '__main__':
    app.run(debug=False)