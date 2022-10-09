from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1' 
  content = requests.get(url).text 
  soup = BeautifulSoup(content, 'html.parser') 
  rate = soup.find("span", class_="ccOutputRslt").get_text().split(' ')[0]  
  
  return float(rate)


app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Currency Rate API</h1> <p>Hey omer ben arieh.</p><p>I knew you supposed to enter in, please copy the text bellow me and paste it at the end of the URL.</p><p>You also can change the currency that you want to get(instead of usd-eur you can write usd-ils or anything else. Have fun my brother)<p>Text to copy URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
  rate = get_currency(in_cur, out_cur)
  result_dictionary = {'input_currncy':in_cur,'output_currency':out_cur,'rate':rate}
  return jsonify(result_dictionary)
  
app.run(host='0.0.0.0')