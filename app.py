from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Asosiy sahifa

@app.route('/')
def home():
    return render_template('index.html')

# Python backend mantigi (API endpoint)

@app.route('/salomlashtirish', methods=['POST'])
def salomlashtirish():
    data = request.get_json()
    ism = data.get('ism', '').strip()

 
    if not ism:
        return jsonify({"muvaffaqiyat": False, "xabar": "Iltimos, ismingizni kiriting!"})

    xabar = f"Salom, {ism}! Python serveringiz so'rovingizni muvaffaqiyatli qabul qildi."
    return jsonify({"muvaffaqiyat": True, "xabar": xabar})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/salomlashtirish', methods=['POST'])
def salomlashtirish():
    data = request.get_json()
    ism = data.get('ism', '').strip()

    # --- MANA SHU QATOR TERMINALDA KO'RSATADI ---
    print(f"\n[YANGI SO'ROV]: Saytdan kelgan foydalanuvchi ismi -> '{ism}'\n")

    if not ism:
        return jsonify({"muvaffaqiyat": False, "xabar": "Iltimos, ismingizni kiriting!"})

    xabar = f"Salom, {ism}! Python serveringiz so'rovingizni muvaffaqiyatli qabul qildi."
    return jsonify({"muvaffaqiyat": True, "xabar": xabar})