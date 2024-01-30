# Project Detailing
I will be explaining my process along the way for this project

## **[X] Pick model**
This revision will be using transferred learning. Looking up the different models I can use, I narrowed it down to BERT models and GPT. It seems like GPT would be too complex for the work that I will be doing, which leaves BERT and its variants. I'm settling with DistilBERT which is just a lighter version of BERT. 

I am picking DistilBERT because:
1. I'm going to assume my work will not be as complex, binary classification for specifically cooking recipes.
2. I would like to use less computation power and DistilBERT is 40% smaller; as of right now, I'm still a beginner...

## **[X] Create new structured classification data**
Now comes the annoying part. We need the data. Luckily, this original project has something I can use to make my work easier. Originally this project will read a webpage, take in sentences, and then classify based on the input sentence. The problem with this approach is that the threshold between a cooking sentence and a non-cooking sentence is arbitrary and although it does work, it's not what I am looking for. I will be using that same code to create a table of cooking and non-cooking sentences. The structure will be something like this:
```
"Put the chicken into the oven for 30 minutes at 400 degrees" : True
"Clean the toilet" : False
```
I will need to preprocess the data but that's in the next section.

*note: it seems like my coding has gotten a lot better through the years, i was able to optimize a lot of things which is good to see improvements

*Update: All the scripts are done. Now I just need to get more data manually which will take a while

*Update: Now that we are in the data gathering section. I need to make sure that there will be equal data. This means I will be gather a 50/50 split of recipe and non recipe sentences. 
Non recipe sentences will need to a varity of sentnce ranging from:
- random sentence written officially like news articles and books. 
- unofficial sentences from threads and blogs
Recipe sentences will also need to come from a variety of places too like cooking websites, cooking books, and online forums.
The data gathering will take a little bit longer because I am not just looking for cooking related sentences, I am looking speicifically for recipe instructions so getting a good 50/50 split will be hard.

*Update: After a couple of tries of using my original scorer, it doesn't classify as well as I want it to. 
I will be switch to a different method. Now, I will use 2 different files for uncleand data. One for only 'True' data, and another for 'False' data. This will require a little bit more work for me since I will now have to make sure I put them in the correct location. I also have to setup a new script to process the data.

## **[X] Tune model**
Tuning the model took a lot longer than I thought. I ended up using a small BERT model. I had to learn what all the variations did and compared the different models. Tried adding in dropout, regularization, and just normal layers with different activations. The general accuracy that I achieved was 90+%. I managed to get a smaller varient of the model to achieve and same performance of a much larger model.

*Update: There has been a lot of problems with the models and had to switch a lot around. GCP isnt working like how I wanted and having it embedded into the chrome extension itself also isnt working out. I settled with AWS but that also caused complications a quite a long time. I solved everything but in the end, I switched to NLTK (Natural Language Toolkit). The size is a lot smaller and the accuracy is still up to my standard. I am finally done with this section!!!

## **[X] AWS Setup**
I decided to host the model on AWS Lambda and hitting the API Gateway endpoint for my chrome extension. I ran into a lot of problems with the speed of the processes. I hadn't realized that the amount of memory allocated also scales with the computational power that you receive. I just assumed that since im not using all the memory, I wouldn't need to increase it... I ended up getting that solved and the time it takes from the page loading to sending the user the processed text is around 4-5 seconds which is not bad. In the future I can consider making that faster but at the moment, there is no need.

## **[] Extension**
After starting on this extension, I have come to thte conclusion that DistilBERT is too large of a model if i want to keep this extension working without the need for a server to host the model. I will be testing TinyBERT and possibily ALBERT.

*Update: TinyBERT is still too large. I am scrapping the LLM idea and going with something a lot smaller. spaCy-small with scikitlearn SVC

*Update: Turns out there were a lot more problems with deploying that I didn't know before. I switched back to using a small variant of BERT.

*Update: In the latest update of my 'Tune Model' section, I updated the model and will also be updating the way i recieve information from AWS

Now that I am done with the model, I will need to process the data coming from the model. The problem with the model is that it returns a huge list of sentences and its predictions. I will have to sort through that list to return back to the customer. I also want to implement a way to check for potential recipes on the page before sending of the list of sentences.