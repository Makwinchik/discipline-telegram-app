CLIP_DURATIONS = [15, 30, 45, 60]
CAPTION_PRESETS = ["TikTok", "Alex Hormozi", "MrBeast", "Minimal", "Podcast", "Modern"]

def analyze_video(source_key: str) -> dict:
    """Production seam for Whisper, Pyannote, FFmpeg, OpenCV, MediaPipe, YOLO, and GPT ranking."""
    transcript = "Welcome to ClipForge AI. This placeholder transcript represents model output."
    clips = []
    for index, duration in enumerate(CLIP_DURATIONS, start=1):
        clips.append({
            "title": f"Viral moment #{index}",
            "topic": "AI generated highlight",
            "score": 100 - index * 7,
            "duration_seconds": duration,
            "output_key": f"renders/{source_key.split('/')[-1]}-{duration}s.mp4",
            "captions": {"preset": CAPTION_PRESETS[index % len(CAPTION_PRESETS)], "words": []},
            "hashtags": {
                "tiktok": ["#viral", "#learnontiktok", "#clipforge"],
                "instagram": ["#reels", "#creator", "#video"],
                "youtube": ["#shorts", "#youtube", "#ai"],
            },
            "description": "AI-selected high-engagement short with dynamic captions and smart crop.",
        })
    return {
        "transcript": transcript,
        "analysis": {
            "chapters": ["Hook", "Insight", "Payoff"],
            "signals": ["viral_hook", "emotional_moment", "informative_moment", "facial_expression"],
            "enhancements": ["color", "contrast", "audio_normalization", "noise_reduction"],
        },
        "clips": clips,
    }
