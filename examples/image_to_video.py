"""HappyHorse 1.1 — image-to-video with `alibaba/happyhorse-1.1/image-to-video`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import happyhorse_api

urls = happyhorse_api.image_to_video(
    prompt="Describe the result you want",
    image="https://example.com/your-image.jpg",
)
print(urls[0])
