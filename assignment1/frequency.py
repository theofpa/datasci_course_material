import sys
import json

# Gets a filename of tweetstream and returns a list of tweets
def parse_tweets(tweetfile):
    tweets=[]
    tweets_file=open(tweetfile)
    for line in tweets_file:
        tweets.append(json.loads(line))
    return tweets

# Gets a list of tweets and returns a dictionary with their words frequency
def frequency(tweets):
    freq=dict()
    for tweet in tweets:
        if "text" in tweet:
            for word in tweet["text"].split():
                uword=word.encode('UTF8')
                if not uword.startswith("@") and ":" not in uword:
                    if uword not in freq.keys():
                        freq[uword]=1
                    else:
                        freq[uword]+=1
    return freq

def main():
    tweets=parse_tweets(sys.argv[1])
    freq=frequency(tweets)
    all=sum(freq.values())
    for key in freq:
        print "%s %.4f" % (key, float(freq[key])/all)

if __name__ == '__main__':
    main()
