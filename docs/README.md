# Project Detailing
I will be explaining my process along the way for this project

## **[X] Pick model**
This revision will be using transferred learning. Looking up the different models I can use, I narrowed it down to BERT models and GPT. It seems like GPT would be too complex for the work that I will be doing, which leaves BERT and its variants. I'm settling with DistilBERT which is just a lighter version of BERT. 

*Update: After starting on this extension, I have come to the conclusion that DistilBERT is too large of a model if I want to keep this extension working without the need for a server to host the model. I will be testing TinyBERT and possibly ALBERT.

*Update: TinyBERT is still too large. I am scrapping the LLM idea and going with something a lot smaller. spaCy-small with sci-kit learn SVC

I settled on using NLTK(Natural Language Toolkit). This option was a lot smaller but it doesn't use a LLM to do the classification. Since this is only a binary classification problem, this shouldn't be a problem, although unfortunate.


## **[X] Create new structured classification data**
Now comes the annoying part. We need the data. Luckily, this original project has something I can use to make my work easier. Originally this project will read a webpage, take in sentences, and then classify based on the input sentence. The problem with this approach is that the threshold between a cooking sentence and a non-cooking sentence is arbitrary and although it does work, it's not what I am looking for. I will be using that same code to create a table of cooking and non-cooking sentences. The structure will be something like this:
```
"Put the chicken into the oven for 30 minutes at 400 degrees": True
"Clean the toilet": False
```
I will need to preprocess the data but that's in the next section.

*note: it seems like my coding has gotten a lot better through the years, i was able to optimize a lot of things which is good to see improvements

*Update: All the scripts are done. Now I just need to get more data manually which will take a while

*Update: Now that we are in the data-gathering section. I need to make sure that there will be equal data. This means I will be gathering a 50/50 split of the recipe and non-recipe sentences. 
Non-recipe sentences will need to be a variety of sentences ranging from:
- random sentences are written officially like news articles and books. 
- unofficial sentences from threads and blogs
Recipe sentences will also need to come from a variety of places too like cooking websites, cooking books, and online forums.
The data gathering will take a little bit longer because I am not just looking for cooking related sentences, I am looking speicifically for recipe instructions so getting a good 50/50 split will be hard.

*Update: After a couple of tries of using my original scorer, it doesn't classify as well as I want it to. 
I will be switching to a different method. Now, I will use 2 different files for uncleaned data. One for only 'True' data, and another for 'False' data. This will require a little bit more work for me since I will now have to make sure I put them in the correct location. I also have to set up a new script to process the data.

*Update: The predictions that I am getting back are not up to my standard so I will be starting over with the model training

## **[X] Tune model**
Tuning the model took a lot longer than I thought. I ended up using a small BERT model. I had to learn what all the variations did and compared the different models. Tried adding in dropout, regularization, and just normal layers with different activations. The general accuracy that I achieved was 90+%. I managed to get a smaller varient of the model to achieve and same performance of a much larger model.

*Update: There has been a lot of problems with the models and had to switch a lot around. GCP isnt working like how I wanted and having it embedded into the chrome extension itself also isnt working out. I settled with AWS but that also caused complications a quite a long time. I solved everything but in the end, I switched to NLTK (Natural Language Toolkit). The size is a lot smaller and the accuracy is still up to my standard. I am finally done with this section!!!

## **[X] AWS Setup**
I decided to host the model on AWS Lambda and hit the API Gateway endpoint for my Chrome extension. I ran into a lot of problems with the speed of the processes. I hadn't realized that the amount of memory allocated also scales with the computational power that you receive. I just assumed that since I'm not using all the memory, I wouldn't need to increase it... I ended up getting that solved and the time it takes from the page loading to sending the user the processed text is around 4-5 seconds which is not bad. In the future I can consider making that faster but at the moment, there is no need.

I had a lot of problems with setting up the AWS Lambda itself. 

## **[] Extension**
The extension comes with a lot of problems. First of all, I cannot have LLM within the extension itself and two, if I decide to use some sort of model within my extension, the size of the extension would be too large. Although the size of my extension is within the limit of what Chrome is allowing, it doesn't make sense for an extension to be more than 50mb let alone anything more than that. That being the case, it would be best to move the model to a server at the cost of expensive and API time. 
