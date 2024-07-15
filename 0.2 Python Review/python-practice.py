
def create_youtube_video(title, description):
    youtube = {}
    youtube["title"] = title
    youtube["description"] = description
    youtube["likes"] = 0
    youtube["dislikes"] = 0
    youtube["comments"] = {}
    return youtube


def dislike_video(video):
    video["dislikes"] += 1
    return video
def like_video(video):
    video["likes"] += 1
    return video

def add_comment(youtube_video, username, comment_text):
    youtube_video["comments"][username] = comment_text
    return youtube_video


video = create_youtube_video("My First Video", "This is the description of my first video.")
print("Initial video state:")
print(video)


video = dislike_video(video)
print(video)

video = add_comment(video, "user1", "Great video!")
print(video)

video = add_comment(video, "user2", "Nice job!")
print(video)

video ["likes"] = 465
video = like_video(video)
print(video)

video = dislike_video(video)
print(video)
