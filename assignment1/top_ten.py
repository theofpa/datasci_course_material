import sys
import json

# Gets a filename of tweetstream and returns a list of tweets
def parse_tweets(tweetfile):
    tweets=[]
    tweets_file=open(tweetfile)
    for line in tweets_file:
        tweets.append(json.loads(line))
    return tweets

def main():
    tweets=parse_tweets(sys.argv[1])
    tags={}
    for tweet in tweets:
        if tweet.get('entities') and tweet['entities']['hashtags']:
            for hashtag in tweet['entities']['hashtags']:
                uword=hashtag['text'].encode('UTF8')
                if uword not in tags.keys():
                    tags[uword]=1
                else:
                    tags[uword]+=1
    for key in sorted(tags,key=tags.get,reverse=True)[:10]:
        print "%s %s" % (key,tags[key])

if __name__ == '__main__':
    main()
