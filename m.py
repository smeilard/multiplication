#!/usr/bin/env python3

import random
import time
import statistics

questions_answers={}
for i in range(1, 10):
    for j in range(1, 10):
        questions_answers["%dx%d" % (i,j)]=i*j
answer_time=[]
errors=0

initial_size=len(questions_answers)
while len(questions_answers) > 0:
    answered_questions=initial_size - len(questions_answers)
    question, answer = random.choice(list(questions_answers.items()))
    print ("(%d/%d) Quel est le resultat de %s ? " % (answered_questions,initial_size,question))
    start=round(time.time() * 1000)
    try:
        user_answer = int(input('Input:'))
    except ValueError:
        stop=round(time.time() * 1000)
        answer_time.append(stop-start)
        print("réponse non reconnue comme un nonmbre :-( ")
        errors=errors+1
        continue
    stop=round(time.time() * 1000)
    answer_time.append(stop-start)
    if user_answer == answer:
        print ("ok, bonne reponse")
        del questions_answers[question]
    else :
        errors=errors+1
        print ("mauvaise reponse")

mean=statistics.mean(answer_time)
median=statistics.median(answer_time)
print ( """stats  :
temps moyen      : %f seconde
temps median     : %f seconde
nombre d'erreurs : %d""" % (mean/1000, median/1000, errors))
