# Project Detailing
I will be explaining my process along the way for this project

## **[x] Pick model**
This revision will be using transferred learning. Looking up the different models I can use, I narrowed it down to BERT models and GPT. It seems like GPT would be too complex for the work that I will be doing, which leaves BERT and its variants. I'm settling with DistilBERT which is just a lighter version of BERT. 

I am picking DistilBERT because:
1. I'm going to assume my work will not be as complex, binary classification for specifically cooking recipes.
2. I would like to use less computation power and DistilBERT is 40% smaller; as of right now, I'm still a beginner...

## **[] Create new structured classification data**
Now comes the annoying part. We need the data. Luckily, this original project has something I can use to make my work easier. Originally this project will read a webpage, take in sentences, and then classify based on the input sentence. The problem with this approach is that the threshold between a cooking sentence and a non-cooking sentence is arbitrary and although it does work, it's not what I am looking for. I will be using that same code to create a table of cooking and non-cooking sentences. The structure will be something like this:
```
"Put the chicken into the oven for 30 minutes at 400 degrees" : True
"Clean the toilet" : False
```
I will need to preprocess the data but that's in the next section.

*note: it seems like my coding has gotten a lot better through the years, i was able to optimize a lot of things which is good to see improvements

*Update: All the scripts are done. Now I just need to get more data manually which will take a while

## **[] Data preprocessing**
## **[] Tune model**