from urlextract import URLExtract
extract =URLExtract()
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

def fetch_stats(selected_user,df):
    if selected_user != "Overall Group":
        df=df[df['user'] == selected_user]

    # Number of messages
    num_messages = df.shape[0]
    # Number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    #fetch number of media messages
    num_media_messages =df[df['message']=='<Media omitted>\n'].shape[0]

    #fecth number of links shared
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words),num_media_messages,len(links)


def most_busy_users(df):
    x=df['user'].value_counts().head()
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'name','user':'percent'})
    return x,df


def create_wordcloud(selected_user,df):
    if selected_user != "Overall Group":
        df=df[df['user']]==selected_user

    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y=[]
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message']=temp['message'].apply(remove_stop_words)
    df_wc=wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):

    if selected_user != 'Overall Group':
        df=df[df['user']==selected_user]

    f=open('stop_hinglish.txt','r')
    stop_words = f.read()

    temp=df[df['user'] != 'group_notification']
    temp=temp[temp['message'] != '<Media omitted>\n']

    words=[]

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_words=pd.DataFrame(Counter(words).most_common(20))
    return most_common_words

def emoji_helper(selected_user,df):
    if selected_user != 'Overall Group':
        df=df[df['user']==selected_user]

    emojis = []
    for message in df['message']:
        for char in message:
            if emoji.is_emoji(char):
                emojis.append(char)

    emoji_df =pd.DataFrame(Counter(emojis).most_common(len(emojis)))

    return emoji_df

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall Group':
        df=df[df['user']==selected_user]

    timeline=df.groupby(['year','month_num','month']).count()['message'].reset_index()

    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+"-"+str(timeline['year'][i]))

    timeline['time'] =time

    return timeline

def daily_timeline(selected_user,df):
    if selected_user != 'Overall Group':
        df=df[df['user']==selected_user]

    daily_timeline = df.groupby('date_').count()['message'].reset_index()

    return daily_timeline




