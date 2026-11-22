"""HappyHorse 1.1 — reference-to-video with `alibaba/happyhorse-1.1/reference-to-video`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import happyhorse_api

urls = happyhorse_api.reference_to_video(
    prompt="Describe the result you want",
    images=["https://example.com/your-image.jpg"],
)
print(urls[0])
