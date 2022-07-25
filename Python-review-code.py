def create_youtube_video(title, description):
	youtube_vid = {"Title":title, "Description": description, "Likes": 0, "Dislikes": 0, "Comments": {}}
	return youtube_vid

def likes(video):
	if "Likes" in video:
		video["Likes"] += 1
	return video

def dislikes(video):
	if "Dislikes" in video:
		video["Dislikes"] += 1
	return video

def add_comment(video, username, commenttext):
	video["Comments"][username] = commenttext
	return video