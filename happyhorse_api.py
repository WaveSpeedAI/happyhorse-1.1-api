"""HappyHorse 1.1 API — Python wrapper for the WaveSpeedAI hosted endpoints.

Each function calls one endpoint through the official `wavespeed` SDK, waits for
the result and returns the list of output URLs. Arguments left as None are not
sent, so the server-side defaults apply.

Set WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey

Generated from the live model schemas; do not edit by hand.
"""
from typing import Any, Dict, List, Optional

import wavespeed

__version__ = "0.1.0"

__all__ = ["MODELS", "upload", "text_to_video", "image_to_video", "reference_to_video", "video_extend"]

#: function name -> WaveSpeedAI model id
MODELS: Dict[str, str] = {
    "text_to_video": "alibaba/happyhorse-1.1/text-to-video",
    "image_to_video": "alibaba/happyhorse-1.1/image-to-video",
    "reference_to_video": "alibaba/happyhorse-1.1/reference-to-video",
    "video_extend": "alibaba/happyhorse-1.1/video-extend",
}


def upload(file: Any) -> str:
    """Upload a local file (path or binary file object) and return its URL."""
    return wavespeed.upload(file)


def _run(name: str, params: Dict[str, Any], timeout: Optional[float], poll_interval: float) -> List[str]:
    payload = {k: v for k, v in params.items() if v is not None}
    result = wavespeed.run(MODELS[name], payload, timeout=timeout, poll_interval=poll_interval)
    return list(result["outputs"])


def text_to_video(
    prompt: str,
    *,
    aspect_ratio: Optional[str] = None,
    resolution: Optional[str] = None,
    duration: Optional[int] = None,
    seed: Optional[int] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Alibaba Happy Horse 1.1 (Text-to-Video) generates cinematic 720p / 1080p videos from text prompts with smooth camera movement, expressive motion, and strong prompt fidelity.

    Model: ``alibaba/happyhorse-1.1/text-to-video``

    Args:
        prompt: Text prompt describing the desired video. Max 2500 characters.
        aspect_ratio: The aspect ratio of the generated video. Allowed: 16:9, 9:16, 1:1, 4:3, 3:4, 4:5, 5:4, 9:21, 21:9. Server default: "16:9".
        resolution: Output video resolution. Allowed: 480p, 720p, 1080p. Server default: "720p".
        duration: Video length in seconds (3-15). Allowed: 3–15. Server default: 5.
        seed: Random seed for reproducibility.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "text_to_video",
        {"prompt": prompt, "aspect_ratio": aspect_ratio, "resolution": resolution, "duration": duration, "seed": seed},
        timeout,
        poll_interval,
    )


def image_to_video(
    prompt: str,
    image: str,
    *,
    resolution: Optional[str] = None,
    duration: Optional[int] = None,
    seed: Optional[int] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Alibaba Happy Horse 1.1 (Image-to-Video) animates a reference image into a cinematic 720p / 1080p video, optionally guided by a text prompt. Smooth camera movement and expressive, stable motion.

    Model: ``alibaba/happyhorse-1.1/image-to-video``

    Args:
        prompt: Optional text prompt guiding the animation. Max 2500 characters.
        image: URL of the first-frame image. JPEG / PNG / BMP / WEBP. Min dimension 300px. Aspect ratio between 1:2.5 and 2.5:1. Max 10 MB.
        resolution: Output video resolution. Allowed: 480p, 720p, 1080p. Server default: "720p".
        duration: Video length in seconds (3-15). Allowed: 3–15. Server default: 5.
        seed: Random seed for reproducibility.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "image_to_video",
        {"prompt": prompt, "image": image, "resolution": resolution, "duration": duration, "seed": seed},
        timeout,
        poll_interval,
    )


def reference_to_video(
    prompt: str,
    images: List[str],
    *,
    resolution: Optional[str] = None,
    aspect_ratio: Optional[str] = None,
    duration: Optional[int] = None,
    seed: Optional[int] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Alibaba Happy Horse 1.1 (Reference-to-Video) generates new video scenes guided by reference images, maintaining consistent characters, styles, and visual identity. Smooth camera movement and expressive, stable motion.

    Model: ``alibaba/happyhorse-1.1/reference-to-video``

    Args:
        prompt: Text description of the desired scene. Refer to reference images as [Image 1], [Image 2], ... in array order.
        images: Array of reference image URLs (1-9). Allowed: up to 9 items.
        resolution: Output video resolution. Allowed: 480p, 720p, 1080p. Server default: "720p".
        aspect_ratio: The aspect ratio of the generated video. Allowed: 16:9, 9:16, 1:1, 4:3, 3:4, 4:5, 5:4, 9:21, 21:9. Server default: "16:9".
        duration: Video length in seconds (3-15). Allowed: 3–15. Server default: 5.
        seed: Random seed for reproducibility.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "reference_to_video",
        {"prompt": prompt, "images": images, "resolution": resolution, "aspect_ratio": aspect_ratio, "duration": duration, "seed": seed},
        timeout,
        poll_interval,
    )


def video_extend(
    prompt: str,
    video: str,
    *,
    resolution: Optional[str] = None,
    duration: Optional[int] = None,
    seed: Optional[int] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Alibaba Happy Horse 1.1 (Video Extend) extends existing videos with seamless AI-generated continuation, supporting 720p/1080p output. Natural, motion-consistent extension.

    Model: ``alibaba/happyhorse-1.1/video-extend``

    Args:
        prompt: Text description of the desired continuation.
        video: The source video to extend.
        resolution: Output video resolution. Allowed: 480p, 720p, 1080p. Server default: "720p".
        duration: Total duration of the final output video in seconds (3-15). Allowed: 3–15. Server default: 5.
        seed: Random seed for reproducibility.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "video_extend",
        {"prompt": prompt, "video": video, "resolution": resolution, "duration": duration, "seed": seed},
        timeout,
        poll_interval,
    )
