"""HappyHorse 1.1 — text-to-video with `alibaba/happyhorse-1.1/text-to-video`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import happyhorse_api

urls = happyhorse_api.text_to_video(
    prompt="A slow cinematic dolly shot through a rain-soaked neon night market, reflections on the pavement",
)
print(urls[0])
