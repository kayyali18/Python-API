#Using Watson API to retrieve Bill Gates' lates 200 tweets

import sys
import operator
import requests
import simplejson as json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

# Consumer Key: 0XAX8qSRDyzdVrfSTrQlzKjZ8
# Consumer Secret: iY0q08SofIPh3hHIKGU68Zua5qvX7VLKFx1NaymJGaAfkP6JvE
# Access Token: 2339949552-1EO2dqOqZu9GNfUZU5ejFlNIMYFwOZld6KBpzap
# Access Secret: 85lumxGRY8zWRvhLMAEWlrQSkb9FUaeq2QHSzMB9sgTqv

# Adding credentials
twitter_consumer_key ="0XAX8qSRDyzdVrfSTrQlzKjZ8"
twitter_consumer_secret = "iY0q08SofIPh3hHIKGU68Zua5qvX7VLKFx1NaymJGaAfkP6JvE"
twitter_access_token = "2339949552-1EO2dqOqZu9GNfUZU5ejFlNIMYFwOZld6KBpzap"
twitter_access_secret = "85lumxGRY8zWRvhLMAEWlrQSkb9FUaeq2QHSzMB9sgTqv"

# creating instance of Twitter package
twitter_api = twitter.api(
    consumer_key = twitter_consumer_key,
    consumer_secret = twitter_consumer_secret,
    access_token_key = twitter_access_token,
    access_token_secret = twitter_access_secret)

# Calling the twitter API
handle = "@BillGates"
statuses = twitter_api.GetUserTimeline(
    screen_name = handle,
    count = 200,
    include_rts = False)

#adding the statuses to a text variable
text = ""

for status in statuses:
    if (status.lang == "en"):
        text += status.text.encode ("utf-8")
