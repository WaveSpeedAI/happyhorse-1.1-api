# HappyHorse 1.1 API — Python wrapper

Call **HappyHorse 1.1** from Python with one function per endpoint: text-to-video, image-to-video, reference-to-video, video extension. Built on the official [`wavespeed`](https://github.com/WaveSpeedAI/wavespeed-python) SDK and the [WaveSpeedAI](https://wavespeed.ai/?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api) hosted API — no GPU, pay per generation.

<p>
  <a href="https://wavespeed.ai/happyhorse-1-1-api?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api"><img src="https://img.shields.io/badge/HappyHorse_1.1_API-Get_API_key-00E5FF?style=for-the-badge&labelColor=0B0B0F" alt="HappyHorse 1.1 API"></a>
  <a href="https://wavespeed.ai/video-generator?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api"><img src="https://img.shields.io/badge/No_code-Try_in_browser-7C3AED?style=for-the-badge&labelColor=0B0B0F" alt="Try in browser"></a>
</p>

- **HappyHorse 1.1 API guide, live pricing and playground:** [wavespeed.ai/happyhorse-1-1-api](https://wavespeed.ai/happyhorse-1-1-api?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api)
- **No code:** generate in the browser with the [AI Video Generator](https://wavespeed.ai/video-generator?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api) on WaveSpeedAI

## Quick start

```bash
pip install git+https://github.com/WaveSpeedAI/happyhorse-1.1-api.git
export WAVESPEED_API_KEY="your-api-key"   # https://wavespeed.ai/accesskey
```

```python
import happyhorse_api

urls = happyhorse_api.text_to_video(
    prompt="A slow cinematic dolly shot through a rain-soaked neon night market, reflections on the pavement",
)
print(urls[0])
```

Every function waits for the generation to finish and returns a list of output URLs. Optional arguments you leave out are not sent, so the API defaults apply. Inputs such as images, videos and audio are passed as URLs; use `happyhorse_api.upload("local-file")` to get a URL for a local file.

## Endpoints

| Function | Model | Type |
| - | - | - |
| [`text_to_video()`](#text_to_video) | [alibaba/happyhorse-1.1/text-to-video](https://wavespeed.ai/models/alibaba/happyhorse-1.1/text-to-video?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api) | text-to-video |
| [`image_to_video()`](#image_to_video) | [alibaba/happyhorse-1.1/image-to-video](https://wavespeed.ai/models/alibaba/happyhorse-1.1/image-to-video?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api) | image-to-video |
| [`reference_to_video()`](#reference_to_video) | [alibaba/happyhorse-1.1/reference-to-video](https://wavespeed.ai/models/alibaba/happyhorse-1.1/reference-to-video?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api) | reference-to-video |
| [`video_extend()`](#video_extend) | [alibaba/happyhorse-1.1/video-extend](https://wavespeed.ai/models/alibaba/happyhorse-1.1/video-extend?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api) | video-extend |

Each model page has a playground, live pricing and copy-paste API snippets. Prices are per generation and depend on the settings you choose; check a request before running it with `wavespeed price <model>` from the [CLI](https://github.com/WaveSpeedAI/wavespeed-cli).

## Parameters

### text_to_video

`alibaba/happyhorse-1.1/text-to-video` — Alibaba Happy Horse 1.1 (Text-to-Video) generates cinematic 720p / 1080p videos from text prompts with smooth camera movement, expressive motion, and strong prompt fidelity.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | Text prompt describing the desired video. Max 2500 characters. |
| `aspect_ratio` | str |  | `"16:9"` | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `4:5`, `5:4`, `9:21`, `21:9` | The aspect ratio of the generated video. |
| `resolution` | str |  | `"720p"` | `480p`, `720p`, `1080p` | Output video resolution. |
| `duration` | int |  | `5` | 3–15 | Video length in seconds (3-15). |
| `seed` | int |  |  |  | Random seed for reproducibility. |

### image_to_video

`alibaba/happyhorse-1.1/image-to-video` — Alibaba Happy Horse 1.1 (Image-to-Video) animates a reference image into a cinematic 720p / 1080p video, optionally guided by a text prompt. Smooth camera movement and expressive, stable motion.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | Optional text prompt guiding the animation. Max 2500 characters. |
| `image` | str | yes |  |  | URL of the first-frame image. JPEG / PNG / BMP / WEBP. Min dimension 300px. Aspect ratio between 1:2.5 and 2.5:1. Max 10 MB. |
| `resolution` | str |  | `"720p"` | `480p`, `720p`, `1080p` | Output video resolution. |
| `duration` | int |  | `5` | 3–15 | Video length in seconds (3-15). |
| `seed` | int |  |  |  | Random seed for reproducibility. |

### reference_to_video

`alibaba/happyhorse-1.1/reference-to-video` — Alibaba Happy Horse 1.1 (Reference-to-Video) generates new video scenes guided by reference images, maintaining consistent characters, styles, and visual identity. Smooth camera movement and expressive, stable motion.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | Text description of the desired scene. Refer to reference images as [Image 1], [Image 2], ... in array order. |
| `images` | List[str] | yes |  | up to 9 items | Array of reference image URLs (1-9). |
| `resolution` | str |  | `"720p"` | `480p`, `720p`, `1080p` | Output video resolution. |
| `aspect_ratio` | str |  | `"16:9"` | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `4:5`, `5:4`, `9:21`, `21:9` | The aspect ratio of the generated video. |
| `duration` | int |  | `5` | 3–15 | Video length in seconds (3-15). |
| `seed` | int |  |  |  | Random seed for reproducibility. |

### video_extend

`alibaba/happyhorse-1.1/video-extend` — Alibaba Happy Horse 1.1 (Video Extend) extends existing videos with seamless AI-generated continuation, supporting 720p/1080p output. Natural, motion-consistent extension.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | Text description of the desired continuation. |
| `video` | str | yes |  |  | The source video to extend. |
| `resolution` | str |  | `"720p"` | `480p`, `720p`, `1080p` | Output video resolution. |
| `duration` | int |  | `5` | 3–15 | Total duration of the final output video in seconds (3-15). |
| `seed` | int |  |  |  | Random seed for reproducibility. |

## REST and CLI

The wrapper is a thin layer over the REST API: submit, then poll for the result.

```bash
curl -s -X POST "https://api.wavespeed.ai/api/v3/alibaba/happyhorse-1.1/text-to-video" \
  -H "Authorization: Bearer $WAVESPEED_API_KEY" -H "Content-Type: application/json" \
  -d '{"prompt": "A slow cinematic dolly shot through a rain-soaked neon night market, reflections on the pavement"}'
# -> {"data": {"id": "<prediction_id>"}}

curl -s "https://api.wavespeed.ai/api/v3/predictions/<prediction_id>/result" \
  -H "Authorization: Bearer $WAVESPEED_API_KEY"
# -> status: completed, outputs: ["<url>"]
```

```bash
npm i -g @wavespeed/cli && wavespeed login
wavespeed run alibaba/happyhorse-1.1/text-to-video -p "your prompt"
```

## Related

- More model wrappers: [Seedance 2.5](https://github.com/WaveSpeedAI/seedance-2.5-api) · [Wan 3.0](https://github.com/WaveSpeedAI/wan-3.0-api) · [Kling 4.0](https://github.com/WaveSpeedAI/kling-4.0-api) · [Veo 3.1](https://github.com/WaveSpeedAI/veo-3.1-api) · [MiniMax H3](https://github.com/WaveSpeedAI/minimax-h3-api) · [FLUX 3](https://github.com/WaveSpeedAI/flux-3-api) · [Seedream 5.5](https://github.com/WaveSpeedAI/seedream-5.5-api) · [GPT Image 2.6](https://github.com/WaveSpeedAI/gpt-image-2.6-api) · [Nano Banana 2.1](https://github.com/WaveSpeedAI/nano-banana-2.1-api)
- SDKs and tools: [Python](https://github.com/WaveSpeedAI/wavespeed-python) · [JavaScript](https://github.com/WaveSpeedAI/wavespeed-javascript) · [CLI](https://github.com/WaveSpeedAI/wavespeed-cli) · [MCP server](https://github.com/WaveSpeedAI/mcp-server) · [ComfyUI nodes](https://github.com/WaveSpeedAI/wavespeed-comfyui)
- [Full model catalog](https://wavespeed.ai/models?utm_source=github&utm_medium=readme&utm_campaign=happyhorse-1.1-api)

## Notes

- HappyHorse 1.1 is a model by Alibaba. This repository is maintained by WaveSpeedAI and wraps the WaveSpeedAI hosted API for it.
- Function signatures and the tables above are generated from the live model schemas (last generated 2026-11-22). The model pages are the source of truth if an endpoint changes.
- Issues and pull requests are welcome. License: MIT.
