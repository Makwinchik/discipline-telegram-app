from apps.api.app.services.ai_pipeline import analyze_video

def test_pipeline_returns_ranked_clips():
    result = analyze_video('uploads/demo.mp4')
    assert len(result['clips']) == 4
    assert result['clips'][0]['score'] > result['clips'][-1]['score']
