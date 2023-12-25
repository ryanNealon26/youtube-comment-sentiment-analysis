from Video import Video
question = "Enter Video Id: "
video_id = input(question)
video = Video(video_id)

video.view_negative_comments()