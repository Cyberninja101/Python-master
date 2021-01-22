import praw
import numpy as np
import pandas as pd
from traceback import format_exc, print_exc
import os
import requests
import datetime
import argparse

path = os.getcwd()

reddit = praw.Reddit(client_id="Rl-KzGv-CAItNw",
                    client_secret="QXsO7iF-RLCZi8RBSMf85mV_nUY",
                    user_agent="testscript by /u/Ru8ted",
                    username="Ru8ted",
                    password="myguitarisold")

#MAKE ALL OF THIS A FUNCTION 
#MAKE SURE ALL THE VARIABLES THATS DEFINED OUTSIDE SHOULD COME THROUGH
#ADD DOCSTRING TO FUNCTION
subreddits = ["gardening"]
for i in subreddits:
    subreddit = reddit.subreddit(i)
    # print(subreddit.display_name)  # Output: redditdev
    # print(subreddit.title)         # Output: reddit Development
    # print(subreddit.description) 

    catagories = ["controversial", "gilded", "hot", "new", "rising", "top"]
    catagories_new = [subreddit.controversial, subreddit.gilded, subreddit.hot, subreddit.new, subreddit.rising, subreddit.top]
    n = 3   
    columns = ["category","author", "clicked", "comments", "created_utc", "distinguished", "edited", "id", "is_original_content", "is_self", "link_flair_template_id", "link_flair_text", "locked", "name", "num_comments", "over_18", "permalink", "poll_data", "score", "selftext", "spoiler", "stickied", "subreddit", "title", "upvote_ratio", "url"]
    data = pd.DataFrame(np.zeros([len(catagories) * n, len(columns)]),columns=columns) #create array with all info from reddit

    columns.pop(0)
    #FIX THIS, THE DATA DOESN"T SHOW ON CSV FILE
    counter = 0
    for i in catagories_new:

        for submission in i(limit=n):
            
            
            
            print("Data in")
            data.loc[counter, "category"] = i
            print(counter)
            
            for j in columns:
                try:
                    data.loc[counter, j] = eval(f"submission.{j}")
                except:
                    er = format_exc()
                    #print(er)
            counter += 1   
            
                
                

    print(data)    
        
            
    # All work is in the exec or this section
    data = data.loc[data["title"] != 0]

# second csv section
# data2 = pd.DataFrame(np.zeros([999999, 3]),columns=["submission","id", "replies"])


# print("Testing out comments section:")
# count = 0
# # GO to this link and get all of the columns of data2 sorted out: https://praw.readthedocs.io/en/latest/code_overview/models/comment.html
# # Tip: make the columns on 119 based on what can be found in the api
# # 3 columns submission, id, and replies(not the replies in the api)
# for submission in subreddit.top(limit=1):
#     submission.comments.replace_more(limit=None)
#     for comment in submission.comments.list():
#         data2.loc[count, "submission"] = comment.body
#         data2.loc[data["id"] == data.loc[count,"id"]] = comment.id
#         print(comment.replies)

#         # Can't get the other info
#         count += 1


cwd = os.getcwd()
print(cwd)
data.to_csv(os.sep.join([cwd, "reddit.csv"]))


if __name__ in "__main__": #It checks if your module is being run directly or being imported
    #ARGPARSE 
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description= "This is a reddit data collection script.")
    parser.add_argument("-m","--mode", help = "    choose mode:\n    1. Get Submissions\n    2. Get Comments",choices=[1,2], default=1,metavar="\b", type = int)
    parser.add_argument("-d","--directory", help="  Put in your directory",default=os.getcwd(),metavar="\b",type = str)
    args = parser.parse_args()
    mode = args.mode
    directory = args.directory
    print(mode)
    print(directory)
    if mode == 1:
        print("This is where i call get submission function")
    elif mode == 2:
        print("This is where i call get comment function")

