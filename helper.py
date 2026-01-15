from urlextract import URLExtract
extract =URLExtract()
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







