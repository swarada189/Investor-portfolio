'''
import re
line = """<p>The pattern analysis of the weekly chart presents an interesting picture. On the daily chart, index remains steeply underbought and evidently prone to consolidation. The FTSE has observed near bearish pattern reaching to the lower circuit points on the weekly chart averaging for 6 months.That said, contrary to what was expected, the markets ended up putting up a weak show.The headline index of 7,228.28 piled up strong loss and ended the week with a net loss of 0.012 points on a weekly basis.According to current market value, stocks in the portfolio are at the valuation of 341,300. Comparing it with average purchase value, portfolio has made loss of 0.071 and made absolute return of 7.1%.Overall Portfolio has made heavy loss in 0.059 as against benchmark index FTSE.In general, portfolio shares of the company SSE, has pulled down the valuations by 0.058.</p><p><p><p>Your fund BARC.L(Barclays), which was originally purchased at &pound;172.52 per share, is currently valued at &pound;16,500.Although both the FTSE index (-0.0116389) and your fund (-0.0435891) are making loss, there are more worrying signs as your fund is performing below the benchmark . This fund is making -0.0020479% contribution to the general portfolio.Following analysis of the market using our algorithms and projections,we predict the new price will be greater than both the purchased and current price, hence you can hold this fund (since your already recording loss on this fund). However you can buy more to increase your earnings.</p><p>Your fund VOD.L(Vodafone), which was originally purchased at &pound;193.62 per share, is currently valued at &pound;14,300.Although both the FTSE index (-0.0116389) and your fund (-0.2614399) are making loss, there are more worrying signs as your fund is performing below the benchmark . This fund is making -0.0137849% contribution to the general portfolio.Following analysis of the market using our algorithms and projections,we predict the new price will be greater than both the purchased and current price, hence you can hold this fund (since your already recording loss on this fund). However you can buy more to increase your earnings.</p><p>Your fund SSE.L(SSE), which was originally purchased at &pound;1,421.5 per share, is currently valued at &pound;120,700.Although both the FTSE index (-0.0116389) and your fund (-0.1508969) are making loss, there are more worrying signs as your fund is performing below the benchmark . This fund is making -0.0584128% contribution to the general portfolio.Following analysis of the market using our algorithms and projections,we predict the new price will be greater than both the purchased and current price, hence you can hold this fund (since your already recording loss on this fund). However you can buy more to increase your earnings.</p><p>Your fund MCRO.L(Micro_focus), which was originally purchased at &pound;1,884.5 per share, is currently valued at &pound;189,800.The FTSE index is making loss (-0.0116389)and your fund is making profit(0.0071637). There is even better news as your fund is performing above the benchmark. This fund is making 0.0036763% contribution to the general portfolio.Following analysis of the market using our algorithms and projections,we predict the new price will be greater than both the current and purchased price, hence you can hold this stock (since your already recording profit on this fund). You can also buy more stocks to improve your profits.</p></p></p>"""

text = line.split('<p>')
mydict = {}
i=0
for para in text:
    if len(para)>0:
        mydict[i]=para
        i+=1
print(mydict) 

import PredictStock as pred
predictedValue = pred.myPrediction()
print(predictedValue)
#pattern = re.compile("(<.*(?<=>))(.*)((?=</)[^>]*>)")
#print(re.findall(pattern, line))
'''
num = -90876.893279254165
print(abs(round(num,3)))