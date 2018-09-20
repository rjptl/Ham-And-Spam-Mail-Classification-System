import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score


# Step 1 : Makig a dictionary

def make_dict():
    #open a file
    direc = "C:/Users/Raj Patel/Desktop/Ham & Spam Classifcation/Emails/"
    files = os.listdir(direc)


    #this would print all the files and directories
    #for file in files:
    #    print(file)

    emails = [direc + email for email in files ]

    #Read all the emails and put it into words
    words = []
    c = len(emails)
    for email in emails:
        #f = open(email)
        f = open(email, encoding="latin-1")
        blob = f.read()
        words += blob.split(" ")
        print (c)
        c -= 1

    #print (word)

    #It Removes Non AlphaNumeric Words from words means we make that words as empty string
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

        
    #Print most common 3000 words from dictionary
    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)
    
# Step 2: Prepare Dataset (Supervised Learning)

def make_dataset(dictionary):
    #open a file
    direc = "C:/Users/Raj Patel/Desktop/Ham & Spam Classifcation/Emails/"
    files = os.listdir(direc)

    emails = [direc + email for email in files ]

    feature_set = []
    labels = []
    c = len(emails)
    
    for email in emails:
        data = []
        #f = open(email)
        f = open(email, encoding="latin-1")
        words = f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)
        
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print (c)
        c = c-1
    return feature_set , labels
            
d = make_dict()
features, labels = make_dataset(d)

#print (len(features))
#print (len(labels))

#Step 3 : Train And Test

# 20% use as testing
x_train, x_test, y_train, y_test = tts(features, labels, test_size = 0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)

preds = clf.predict(x_test)
print("accurcy of model is : ")
print(accuracy_score(y_test, preds)*100)



