from flask import Flask,jsonify, request
from flask_cors import CORS
import json
import requests 

app = Flask(__name__)
CORS(app)
def getArriaContent():
    null = None
    url = 'https://app.studio.arria.com:443/alite_content_generation_webapp/text/v3g3XPEvkxw'
    payload = {"data":[{"id":"Primary","type":"json","jsonData":{"name":"Mel Gibson","shortname":"Gibson","gender":"male","birthyear":1956,"diedyear":null,"nationality":"American","birthplace":"Peekskill, New York","movies":[{"name":"Lethal Weapon 3","role":"actor","year":1992,"rating":6.7,"award":null,"nominations":[]},{"name":"Get the Gringo","role":"actor","year":2012,"rating":7,"award":null,"nominations":[]},{"name":"War Pigs","role":"actor","year":null,"rating":null,"award":null,"nominations":[]},{"name":"Mad Max Beyond Thunderdome","role":"actor","year":1985,"rating":6.3,"award":null,"nominations":[]},{"name":"We Were Soldiers","role":"actor","year":2002,"rating":7.2,"award":null,"nominations":[]},{"name":"Tequila Sunrise","role":"actor","year":1988,"rating":6,"award":null,"nominations":[]},{"name":"Dragged Across Concrete","role":"actor","year":2018,"rating":8.7,"award":null,"nominations":[]},{"name":"The Road Warrior","role":"actor","year":1981,"rating":7.6,"award":null,"nominations":[]},{"name":"Berserker","role":"director","year":null,"rating":null,"award":null,"nominations":[]},{"name":"Braveheart","role":"actor","year":1995,"rating":8.4,"award":null,"nominations":[]},{"name":"Paparazzi","role":"producer","year":2004,"rating":5.8,"award":null,"nominations":[]},{"name":"Gallipoli","role":"actor","year":1981,"rating":7.5,"award":null,"nominations":[]},{"name":"The Professor and the Madman","role":"actor","year":2019,"rating":null,"award":null,"nominations":[]},{"name":"Lethal Weapon 2","role":"actor","year":1989,"rating":7.2,"award":null,"nominations":[]},{"name":"Attack Force Z","role":"actor","year":1981,"rating":5.6,"award":null,"nominations":[]},{"name":"Conspiracy Theory","role":"actor","year":1997,"rating":6.7,"award":null,"nominations":[]},{"name":"Destroyer","role":"director","year":null,"rating":null,"award":null,"nominations":[]},{"name":"The Man Without a Face","role":"actor","year":1993,"rating":6.7,"award":null,"nominations":[]},{"name":"Summer City","role":"actor","year":1977,"rating":4.5,"award":null,"nominations":[]},{"name":"Mad Max","role":"actor","year":1979,"rating":7,"award":null,"nominations":[]},{"name":"Lethal Weapon","role":"actor","year":1987,"rating":7.6,"award":null,"nominations":[]},{"name":"Pocahontas","role":"actor","year":1995,"rating":6.7,"award":null,"nominations":[]},{"name":"Boss Level","role":"actor","year":2019,"rating":null,"award":null,"nominations":[]},{"name":"What Women Want","role":"actor","year":2000,"rating":6.4,"award":null,"nominations":[]},{"name":"Daddy's Home 2","role":"actor","year":2017,"rating":6,"award":null,"nominations":[]},{"name":"Stonehearst Asylum","role":"producer","year":2014,"rating":6.8,"award":null,"nominations":[]},{"name":"Every Other Weekend","role":"actor","year":null,"rating":null,"award":null,"nominations":[]},{"name":"The Beaver","role":"actor","year":2011,"rating":6.7,"award":null,"nominations":[]},{"name":"Leonard Cohen: I'm Your Man","role":"producer","year":2005,"rating":6.9,"award":null,"nominations":[]},{"name":"Tim","role":"actor","year":1979,"rating":6.5,"award":null,"nominations":[]},{"name":"The River","role":"actor","year":1984,"rating":6.3,"award":null,"nominations":[]},{"name":"Chicken Run","role":"actor","year":2000,"rating":7,"award":null,"nominations":[]},{"name":"Payback","role":"actor","year":1999,"rating":7.1,"award":null,"nominations":[]},{"name":"Hacksaw Ridge","role":"director","year":2016,"rating":8.1,"award":null,"nominations":["Best Director"]},{"name":"Maverick","role":"actor","year":1994,"rating":7,"award":null,"nominations":[]},{"name":"Signs","role":"actor","year":2002,"rating":6.7,"award":null,"nominations":[]},{"name":"The Singing Detective","role":"actor","year":2003,"rating":5.6,"award":null,"nominations":[]},{"name":"Hamlet","role":"actor","year":1990,"rating":6.8,"award":null,"nominations":[]},{"name":"Ransom","role":"actor","year":1996,"rating":6.6,"award":null,"nominations":[]},{"name":"Apocalypto","role":"director","year":2006,"rating":7.8,"award":null,"nominations":[]},{"name":"Lethal Weapon 4","role":"actor","year":1998,"rating":6.6,"award":null,"nominations":[]},{"name":"Blood Father","role":"actor","year":2016,"rating":6.4,"award":null,"nominations":[]},{"name":"The Bounty","role":"actor","year":1984,"rating":7.1,"award":null,"nominations":[]},{"name":"The Million Dollar Hotel","role":"actor","year":2000,"rating":5.9,"award":null,"nominations":[]},{"name":"Forever Young","role":"actor","year":1992,"rating":6.3,"award":null,"nominations":[]},{"name":"Edge of Darkness","role":"actor","year":2010,"rating":6.6,"award":null,"nominations":[]},{"name":"The Passion of the Christ","role":"director","year":2004,"rating":7.2,"award":null,"nominations":[]},{"name":"The Last Trimate","role":"actor","year":2008,"rating":null,"award":null,"nominations":[]},{"name":"Mrs. Soffel","role":"actor","year":1984,"rating":6.3,"award":null,"nominations":[]},{"name":"The Year of Living Dangerously","role":"actor","year":1982,"rating":7.2,"award":null,"nominations":[]},{"name":"Air America","role":"actor","year":1990,"rating":5.7,"award":null,"nominations":[]},{"name":"Bird on a Wire","role":"actor","year":1990,"rating":5.9,"award":null,"nominations":[]},{"name":"The Patriot","role":"actor","year":2000,"rating":7.2,"award":null,"nominations":[]},{"name":"Machete Kills","role":"actor","year":2013,"rating":5.6,"award":null,"nominations":[]},{"name":"The Passion of the Christ: Resurrection","role":"director","year":null,"rating":null,"award":null,"nominations":[]},{"name":"Braveheart","role":"producer","year":1995,"rating":8.4,"award":"Best Picture","nominations":["Best Picture"]},{"name":"Braveheart","role":"director","year":1995,"rating":8.4,"award":"Best Director","nominations":["Best Director"]}]}}],"projectArguments":null,"options":null}
    headers = {'content-type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJUMHluQnhQN2RoaEsyN2dKQmJ5T2dUQ0QiLCJpYXQiOjE1NTI1NDgzODYsImV4cCI6MTcxMDIyODM4NiwiaXNzIjoiQUxpdGUiLCJzdWIiOiJCRVlxNzhBQ1lOR18iLCJBTGl0ZS5wZXJtIjpbInByczp4OnYzZzNYUEV2a3h3Il0sIkFMaXRlLnR0IjoidV9hIn0.FCLD4o6AOt5mLtRhUVcerPXlDYdw0njiNXXFTOyPbsSorWCMbg42z9hzY0qCHm9HnV5KgpXL55L8gPYWfw2yRg'
            }

    response  = requests.post(url, data=json.dumps(payload), headers=headers)
    output = response.json()
    #response = json.loads(response)
    result = output[0]["result"]
    #print(response.text.results[0])

    #print(output[0]["result"])
    return result


@app.route('/',methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent' : some_json}),201
    else:
        resultant = getArriaContent()
        return jsonify({'ArriaText': resultant})
@app.route('/multi/<int:num>',methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num*20})

# if __name__ == '__main__':
#     app.run(debug=True)
