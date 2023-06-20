#!/usr/bin/env python3

import tkinter as tk
import random
import time
import statistics

questions_answers={}
for i in range(1, 10):
    for j in range(1, 10):
        questions_answers["%dx%d" % (i,j)]=i*j
answer_time=[]

initial_size=len(questions_answers)
start=round(time.time() * 1000)
errors=0
answer=0

window = tk.Tk()
zoneQuestion = tk.Label(text="texte de la question")
zoneQuestion.pack()
zoneSaisie = tk.Entry()
zoneSaisie.pack()
zoneStats = tk.Label(text="texte de stats")
zoneStats.pack()

def check(event):
    global errors, questions_answers
    stop=round(time.time() * 1000)
    try:
        user_answer = int(zoneSaisie.get())
    except ValueError:
        answer_time.append(stop-start)
        print("réponse non reconnue comme un nonmbre :-( ")
        errors=errors+1
        return
    answer_time.append(stop-start)
    if user_answer == answer:
        print ("ok, bonne reponse")
        del questions_answers[question]
    else :
        errors=errors+1
        print ("mauvaise reponse %d vs %d" % (user_answer,answer))
    stats()
    ask_question()

zoneSaisie.bind('<Return>', check)

def stats():
    mean=statistics.mean(answer_time)
    median=statistics.median(answer_time)
    text_stats = """stats  :
    temps moyen      : %f seconde
    temps median     : %f seconde
    nombre d'erreurs : %d""" % (mean/1000, median/1000, errors)
    zoneStats.config(text= text_stats)

def ask_question():
    global question, answer
    answered_questions=initial_size - len(questions_answers)
    question, answer = random.choice(list(questions_answers.items()))
    zoneQuestion.config(text= "(%d/%d) Quel est le resultat de %s ? " % (answered_questions,initial_size,question))
    zoneSaisie.delete(0,100)
    start=round(time.time() * 1000)

ask_question()
window.mainloop()

