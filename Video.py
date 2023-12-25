from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
api_key="AIzaSyBUFNjfHbxq-N4jdgCAGIE0aIb1RV6iTrI"

class Video:
    sentiment = SentimentIntensityAnalyzer()
    def __init__(self, video_id):
        self.video_id = video_id

    def pull_comments(self):
        max_comments = input("Print the number of comments to be pulled: ")
        youtube = build(
            'youtube',
            'v3',
        developerKey=api_key
        )
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=self.video_id,
            textFormat = 'plainText',
            maxResults=max_comments
        ).execute()
        return request
    def view_comments(self):
        video_comments = self.pull_comments()
        counter = 1
        for items in video_comments['items']:
            comment = items['snippet']['topLevelComment']['snippet']['textDisplay']
            print(str(counter) +". " + comment+'\n')
            counter+=1
    def comment_sentiment_list(self):
        comment_sentiment_list = []
        video_comments = self.pull_comments()
        for items in video_comments['items']:
            comment = items['snippet']['topLevelComment']['snippet']['textDisplay']
            comment_sentiment = self.sentiment.polarity_scores(comment)['compound']
            comment_pair = (comment, comment_sentiment)
            comment_sentiment_list.append(comment_pair)
        return comment_sentiment_list
    def view_comment_sentiment(self):
        video_comments = self.comment_sentiment_list()
        for comment in video_comments:
            print("Comment: " + comment[0])
            print("Sentiment Score: "+ str(comment[1])+'\n')
    def view_positive_comments(self):
        video_comments = self.comment_sentiment_list()
        for comment in video_comments:
            if comment[1]>0:
                print("Comment: " + comment[0])
                print("Sentiment Score: "+ str(comment[1])+'\n')
    def view_negative_comments(self):
        video_comments = self.comment_sentiment_list()
        for comment in video_comments:
            if comment[1]<0:
                print("Comment: " + comment[0])
                print("Sentiment Score: "+ str(comment[1])+'\n')