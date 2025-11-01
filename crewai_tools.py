class YoutubeChannelSearchTool:
    def __init__(self, youtube_channel_handle: str):
        self.youtube_channel_handle = youtube_channel_handle

    def search(self, topic: str):
        # Return a deterministic dummy result for local testing
        return {"channel": self.youtube_channel_handle, "topic": topic, "videos": []}
