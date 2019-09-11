import praw
import details

###  LOGGING INTO REDDIT  ###
reddit_instance = praw.Reddit(user_agent=        'add_your_user_agent_here',
                              client_id=         details.client_id,
                              client_secret=     details.secret,
                              password=          details.password,
                              username=          details.username)


### OPENING/CREATING COMMENTED FILE AND RETRIEVING ID'S ###
# the 'commented' variable holds a live version of this sessions' replied-to-comments
f = open('commented.txt', 'r')
commented = list(filter(None, f.read().split('\n')))
f.close()



### COMMENTING ###
while True:
    for comment in reddit_instance.subreddit('freekarma4u').comments(limit=200):
        if (comment.id not in commented) and (comment.author != reddit_instance.user.me()):            
            comment.reply("Please upvote me!")
            print('commented')
            
            # Adds the replied-to-comment's id into the variable 'commented' and also writes this comment's id into the file
            commented.append(comment.id)
            with open('commented.txt', 'a') as f:
                f.write(comment.id + '\n')
