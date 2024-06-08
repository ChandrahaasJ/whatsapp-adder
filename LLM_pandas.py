import time
from gemini import askgem
import pandas as pd
res_list=[]
df=pd.read_csv("C://Users/niran/Desktop/IMP Docs/RITI _ CLUB RECRUITMENTS - 2024  (Responses) - Form responses 1.csv")
for i in range(len(df)+1):
    prompt=df["What's your understanding of upcycling and trends?"][1] + "rate this response for the question \"What's your understanding of upcycling and trends?\" out of 10" + "just give the rating(example: 10 or 3 or 2.8) with no additional text and fractions"+"give the score in decimals since I'll be filtering the responses later based on the score which you gave"
    res=askgem(prompt)
    print(res,"\n")
    res_list.append(res)
    time.sleep(10)
res_list.pop()
df["resp1 score"]=res_list

res_list=[]
for i in range(len(df)):
    prompt=df["What interests you about our club?"][1] + "rate this response for the question \"What interests you about our club?\" out of 10" + "just give the rating(example: 10 or 3 or 2.8) with no additional text and fractions"+"give the score in decimals since I'll be filtering the responses later based on the score which you gave"
    res=askgem(prompt)
    print(res,"\n")
    res_list.append(res)
    time.sleep(10)



df["resp2 score"]=res_list

res_list=[]
for i in range(len(df)+1):
    prompt=df["What do you know about the activities conducted by Riti, and have you participated in any events or activities with Riti?"][1] + "rate this response for the question \"What do you know about the activities conducted by Riti, and have you participated in any events or activities with Riti?\" out of 10" + "just give the rating(example: 10 or 3 or 2.8) with no additional text and fractions"+"give the score in decimals since I'll be filtering the responses later based on the score which you gave"
    res=askgem(prompt)
    print(res,"\n")
    res_list.append(res)
    time.sleep(10)

df["resp3 score"]=res_list