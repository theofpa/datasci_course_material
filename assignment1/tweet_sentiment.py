import sys
import json

def parse_afin(afinfile):
    afinnfile = open(afinfile)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    print scores.items() # Print every (term, score) pair in the dictionary

def parse_tweets(tweetfile):
    tweets=[]
    tweets_file=open(tweetfile)
    for line in tweets_file:
        tweet=json.loads(line)
        print tweet["text"]

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #parse_afin(sys.argv[1])
    parse_tweets(sys.argv[2])
    #lines(tweet_file)

if __name__ == '__main__':
    main()
