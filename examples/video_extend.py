"""HappyHorse 1.1 — video-extend with `alibaba/happyhorse-1.1/video-extend`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import happyhorse_api

urls = happyhorse_api.video_extend(
    prompt="Describe the result you want",
    video="https://example.com/your-video.mp4",
)
print(urls[0])
