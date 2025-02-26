from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Funktion för att läsa citaten från filen
def read_quotes():
    try:
        with open("quotes.txt", "r", encoding="utf-8") as file:
            quotes = [line.strip() for line in file if line.strip()]  # Tar bort tomma rader
        return quotes
    except FileNotFoundError:
        return ["Citatfilen saknas! Lägg till en fil med namnet 'quotes.txt'."]

@app.route("/")
def daily_quote():
    quotes = read_quotes()
    today = datetime.date.today()
    formatted_date = today.strftime("%d %B %Y")  # Exempel: "24 februari 2025"
    quote = quotes[today.day % len(quotes)]  # Väljer citat baserat på datum
    return render_template("index.html", quote=quote, date=formatted_date)

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))  # Render sätter PORT-variabeln automatiskt

    app.run(host="0.0.0.0", port=port)

