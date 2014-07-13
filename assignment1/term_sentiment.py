import sys
import json

def parse_afin(afinfile):
    afinnfile = open(afinfile)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores

def parse_tweets(tweetfile):
    tweets=[]
    tweets_file=open(tweetfile)
    for line in tweets_file:
        tweets.append(json.loads(line))
    return tweets

def lines(fp):
    print str(len(fp.readlines()))

def main():
    scores=parse_afin(sys.argv[1])
    tweets=parse_tweets(sys.argv[2])
    for tweet in tweets:
        total=0
        for word in tweet["text"].split():
            if word.encode('UTF8') in scores.keys():
                total=total+scores[word]
        #print total
        for word in tweet["text"].split():
            if word.encode('UTF8') not in scores.keys():
                print "%s %s" % (word.encode('UTF8'),total)

if __name__ == '__main__':
    main()
