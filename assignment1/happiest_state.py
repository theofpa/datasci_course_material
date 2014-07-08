import sys
import json
import operator

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
abr = {v:k for k, v in states.items()}

# Gets a filename of tweetstream and returns a list of tweets
def parse_tweets(tweetfile):
    tweets=[]
    tweets_file=open(tweetfile)
    for line in tweets_file:
        tweets.append(json.loads(line))
    return tweets

def parse_afin(afinfile):
    afinnfile = open(afinfile)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores

def main():
    tweets=parse_tweets(sys.argv[2])
    scores=parse_afin(sys.argv[1])
    happy={}
    for tweet in tweets:
        if tweet.get('place') and tweet['place']['country_code']=='US' and tweet.get('text'):
            full_name=tweet['place']['full_name'].split(', ')
            if full_name[1]=='USA':
                state=abr[full_name[0]]
            else:
                state=full_name[1]

            total=0
            for word in tweet["text"].split():
                if word.encode('UTF8') in scores.keys():
                    total=total+scores[word]
            if not happy.get('state'):
                happy[state]=total
            else:
                happy[state]=happy[state]+total
    #for happy_state, happiness in sorted(happy.iteritems(),key=operator.itemgetter(1)):
    #    print "%s %s" % (happy_state, happiness)
    print max(happy, key=happy.get)

if __name__ == '__main__':
    main()
