import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():        # logic part starts here
    nltk.download('punkt')                              #just need to do it once

    url = urll.get('1.0',"end").strip()

    article=Article(url)        # we have created an article object of newspaper library

    article.download()      # downloading the data
    article.parse()         # our object parses the data and understand it then breaks it down to what it needs

    article.nlp()       # it does all the work for us

    print(f'Title: {article.title}')
    print(f'Authors: {article.authors}')
    print(f'Publication Date: {article.publish_date}')
    print(f'Summary: {article.summary}')

    analysis=TextBlob(article.text)      # we provide text as parameter and it does the analysis
    print(analysis.polarity)
    print(f'Sentiment: {"positive " if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')
    #logic part ends here

    #  now we are just adding info to interface

    title.config(state='normal')    #we do this so that we can edit text infos
    author.config(state='normal')
    published.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0',"end")       # this means to delete whatever is in the label
    title.insert('1.0',article.title)

    author.delete('1.0', "end")
    author.insert('1.0', article.authors)

    published.delete('1.0', "end")
    published.insert('1.0', article.publish_date or '-none-')

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    sentiment.delete('1.0', "end")
    sentiment.insert('1.0', f'Polarity: {analysis.polarity},  Sentiment: {"positive " if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')



#Interface part starts here

root=tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

#Title part
tlabel=tk.Label(root, text="Title")
tlabel.pack()       #adds label to window

title=tk.Text(root, height=1, width=140)
title.config(state='disabled',bg="#dddddd")      #so user can't input anything
title.pack()

# Author part
alabel=tk.Label(root, text="Author")
alabel.pack()       #adds label to window

author=tk.Text(root, height=1, width=140)
author.config(state='disabled',bg="#dddddd")      #so user can't input anything
author.pack()

# Publication date
plabel=tk.Label(root, text="Publication Date")
plabel.pack()       #adds label to window

published=tk.Text(root, height=1, width=140)
published.config(state='disabled',bg="#dddddd")      #so user can't input anything
published.pack()

# summary part
slabel=tk.Label(root, text="Summary")
slabel.pack()       #adds label to window

summary=tk.Text(root, height=20, width=140)
summary.config(state='disabled',bg="#dddddd")      #so user can't input anything
summary.pack()


#sentiment analysis
selabel=tk.Label(root, text="Sentiment Analysis")
selabel.pack()       #adds label to window

sentiment=tk.Text(root, height=1, width=140)
sentiment.config(state='disabled',bg="#dddddd")      #so user can't input anything
sentiment.pack()

#url entering section
ulabel=tk.Label(root, text="URL")
ulabel.pack()       #adds label to window

urll=tk.Text(root, height=1, width=140)
urll.config(bg="#dddddd")      #so user can't input anything
urll.pack()

#button to get url
btn=tk.Button(root, text='Summarize',command=summarize)
btn.pack()




root.mainloop()

