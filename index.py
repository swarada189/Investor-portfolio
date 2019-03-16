from flask import Flask,jsonify, request
from flask_cors import CORS
import json
import requests 

import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime
from sys import exit
import fix_yahoo_finance as yf
#import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
yf.pdr_override() 

app = Flask(__name__)
CORS(app)

def moneyARC():
    
    #Initialise dates
    start_date="2018-09-12"
    end2 = "2018-09-13"
    end_date="2019-03-15"
    today=datetime.date.today()


    # In[25]:


    #Populate stocks dataframe using excel
    stockPF = pd.read_excel('Portfolio.xlsx')
    stockPF["CUR_PRICE"] = 0


    # In[26]:



    stockPF["CUR_PRICE"][0]= si.get_live_price('BARC.L')
    stockPF["CUR_PRICE"][1]= si.get_live_price('VOD.L')
    stockPF["CUR_PRICE"][2]= si.get_live_price('SSE.L')
    stockPF["CUR_PRICE"][3]= si.get_live_price('MCRO.L')


    # In[27]:


    stockPF["FUND_VAL"] = stockPF["QTY"] * stockPF["CUR_PRICE"]
    stockPF["PRO/LOSS"] = stockPF["CUR_PRICE"] - stockPF["PCH_PRICE"]
    stockPF["PERC"] = stockPF["PRO/LOSS"] / stockPF["PCH_PRICE"]
    stockPF


    # In[28]:


    #comparison of net portfolio value with index
    prevPF = (stockPF["QTY"] * stockPF["PCH_PRICE"]).sum()
    currPF = (stockPF["FUND_VAL"]).sum()
    delPF = (currPF - prevPF)/prevPF


    # In[34]:


    prevID = pdr.get_data_yahoo('^FTSE',start=start_date,end=start_date)
    prevID = float(prevID["Close"])
    


    # In[35]:


    currID = pdr.get_data_yahoo('^FTSE',start="2019-03-16",end="2019-03-17")
    currID = float(currID["Close"])
    delID = (currID - prevID)/prevID
    if delID < 0:
        neg = 1
    else:
        neg=0


    # In[36]:


    stockPF["CONTRI"] = (stockPF["PRO/LOSS"]*stockPF["QTY"])/prevPF
    stockPF


    # In[42]:


    import json
    data =  {'acc_value':float(currPF),'buying_power':190000,'cash':210000,'annual_ret':0.49,
            'ftse':currID,
            'del_index':delID,
            'del_pf':delPF,
            'ID_updown':neg}
    data['stocks'] = []
    for i in range(0,4):
        data['stocks'].append({'company':stockPF['COMP'][i],
                            'symbol':stockPF['SYM'][i],
                            'pprice':float(stockPF['PCH_PRICE'][i]),
                            'qty':float(stockPF['QTY'][i]),
                            'cprice':float(stockPF['CUR_PRICE'][i]),
                                'fund':float(stockPF['FUND_VAL'][i]),
                            'pro-loss':float(stockPF['PRO/LOSS'][i]),
                            'perc':float(stockPF['PERC'][i]),
                            'contri':float(stockPF['CONTRI'][i])})
    return data
    #with open('findata.json','w') as outfile:
        #json.dump(data,outfile)
def getArriaContent():
    null = None
    url = 'https://app.studio.arria.com:443/alite_content_generation_webapp/text/onNQNMR0N7Q'
    
    payload = moneyARC()
    #payload = {"data":[{"id":"Primary","type":"json","jsonData":{"name":"Mel Gibson","shortname":"Gibson","gender":"male","birthyear":1956,"diedyear":null,"nationality":"American","birthplace":"Peekskill, New York","movies":[{"name":"Lethal Weapon 3","role":"actor","year":1992,"rating":6.7,"award":null,"nominations":[]},{"name":"Get the Gringo","role":"actor","year":2012,"rating":7,"award":null,"nominations":[]},{"name":"War Pigs","role":"actor","year":null,"rating":null,"award":null,"nominations":[]},{"name":"Mad Max Beyond Thunderdome","role":"actor","year":1985,"rating":6.3,"award":null,"nominations":[]},{"name":"We Were Soldiers","role":"actor","year":2002,"rating":7.2,"award":null,"nominations":[]},{"name":"Tequila Sunrise","role":"actor","year":1988,"rating":6,"award":null,"nominations":[]},{"name":"Dragged Across Concrete","role":"actor","year":2018,"rating":8.7,"award":null,"nominations":[]},{"name":"The Road Warrior","role":"actor","year":1981,"rating":7.6,"award":null,"nominations":[]},{"name":"Berserker","role":"director","year":null,"rating":null,"award":null,"nominations":[]},{"name":"Braveheart","role":"actor","year":1995,"rating":8.4,"award":null,"nominations":[]},{"name":"Paparazzi","role":"producer","year":2004,"rating":5.8,"award":null,"nominations":[]},{"name":"Gallipoli","role":"actor","year":1981,"rating":7.5,"award":null,"nominations":[]},{"name":"The Professor and the Madman","role":"actor","year":2019,"rating":null,"award":null,"nominations":[]},{"name":"Lethal Weapon 2","role":"actor","year":1989,"rating":7.2,"award":null,"nominations":[]},{"name":"Attack Force Z","role":"actor","year":1981,"rating":5.6,"award":null,"nominations":[]},{"name":"Conspiracy Theory","role":"actor","year":1997,"rating":6.7,"award":null,"nominations":[]},{"name":"Destroyer","role":"director","year":null,"rating":null,"award":null,"nominations":[]},{"name":"The Man Without a Face","role":"actor","year":1993,"rating":6.7,"award":null,"nominations":[]},{"name":"Summer City","role":"actor","year":1977,"rating":4.5,"award":null,"nominations":[]},{"name":"Mad Max","role":"actor","year":1979,"rating":7,"award":null,"nominations":[]},{"name":"Lethal Weapon","role":"actor","year":1987,"rating":7.6,"award":null,"nominations":[]},{"name":"Pocahontas","role":"actor","year":1995,"rating":6.7,"award":null,"nominations":[]},{"name":"Boss Level","role":"actor","year":2019,"rating":null,"award":null,"nominations":[]},{"name":"What Women Want","role":"actor","year":2000,"rating":6.4,"award":null,"nominations":[]},{"name":"Daddy's Home 2","role":"actor","year":2017,"rating":6,"award":null,"nominations":[]},{"name":"Stonehearst Asylum","role":"producer","year":2014,"rating":6.8,"award":null,"nominations":[]},{"name":"Every Other Weekend","role":"actor","year":null,"rating":null,"award":null,"nominations":[]},{"name":"The Beaver","role":"actor","year":2011,"rating":6.7,"award":null,"nominations":[]},{"name":"Leonard Cohen: I'm Your Man","role":"producer","year":2005,"rating":6.9,"award":null,"nominations":[]},{"name":"Tim","role":"actor","year":1979,"rating":6.5,"award":null,"nominations":[]},{"name":"The River","role":"actor","year":1984,"rating":6.3,"award":null,"nominations":[]},{"name":"Chicken Run","role":"actor","year":2000,"rating":7,"award":null,"nominations":[]},{"name":"Payback","role":"actor","year":1999,"rating":7.1,"award":null,"nominations":[]},{"name":"Hacksaw Ridge","role":"director","year":2016,"rating":8.1,"award":null,"nominations":["Best Director"]},{"name":"Maverick","role":"actor","year":1994,"rating":7,"award":null,"nominations":[]},{"name":"Signs","role":"actor","year":2002,"rating":6.7,"award":null,"nominations":[]},{"name":"The Singing Detective","role":"actor","year":2003,"rating":5.6,"award":null,"nominations":[]},{"name":"Hamlet","role":"actor","year":1990,"rating":6.8,"award":null,"nominations":[]},{"name":"Ransom","role":"actor","year":1996,"rating":6.6,"award":null,"nominations":[]},{"name":"Apocalypto","role":"director","year":2006,"rating":7.8,"award":null,"nominations":[]},{"name":"Lethal Weapon 4","role":"actor","year":1998,"rating":6.6,"award":null,"nominations":[]},{"name":"Blood Father","role":"actor","year":2016,"rating":6.4,"award":null,"nominations":[]},{"name":"The Bounty","role":"actor","year":1984,"rating":7.1,"award":null,"nominations":[]},{"name":"The Million Dollar Hotel","role":"actor","year":2000,"rating":5.9,"award":null,"nominations":[]},{"name":"Forever Young","role":"actor","year":1992,"rating":6.3,"award":null,"nominations":[]},{"name":"Edge of Darkness","role":"actor","year":2010,"rating":6.6,"award":null,"nominations":[]},{"name":"The Passion of the Christ","role":"director","year":2004,"rating":7.2,"award":null,"nominations":[]},{"name":"The Last Trimate","role":"actor","year":2008,"rating":null,"award":null,"nominations":[]},{"name":"Mrs. Soffel","role":"actor","year":1984,"rating":6.3,"award":null,"nominations":[]},{"name":"The Year of Living Dangerously","role":"actor","year":1982,"rating":7.2,"award":null,"nominations":[]},{"name":"Air America","role":"actor","year":1990,"rating":5.7,"award":null,"nominations":[]},{"name":"Bird on a Wire","role":"actor","year":1990,"rating":5.9,"award":null,"nominations":[]},{"name":"The Patriot","role":"actor","year":2000,"rating":7.2,"award":null,"nominations":[]},{"name":"Machete Kills","role":"actor","year":2013,"rating":5.6,"award":null,"nominations":[]},{"name":"The Passion of the Christ: Resurrection","role":"director","year":null,"rating":null,"award":null,"nominations":[]},{"name":"Braveheart","role":"producer","year":1995,"rating":8.4,"award":"Best Picture","nominations":["Best Picture"]},{"name":"Braveheart","role":"director","year":1995,"rating":8.4,"award":"Best Director","nominations":["Best Director"]}]}}],"projectArguments":null,"options":null}
    headers = {'content-type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJNbW5XNkpHZEdPVVdMTjFWVkdsbTBndzkiLCJpYXQiOjE1NTI3NTUyNTYsImV4cCI6MTcxMDQzNTI1NiwiaXNzIjoiQUxpdGUiLCJzdWIiOiJDbWlOdDlGT1NMRzIiLCJBTGl0ZS5wZXJtIjpbInByczp4Om9uTlFOTVIwTjdRIl0sIkFMaXRlLnR0IjoidV9hIn0.QQxBFOeZMd6iszkW3QmkdYYLQYUJrM7NWR4nryW_TbyXcvsvnCBIhKzQwaed-xI1ZlJCWN5ie7be4fJvem7r-w'
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

#if __name__ == '__main__':
     #app.run(debug=True)
