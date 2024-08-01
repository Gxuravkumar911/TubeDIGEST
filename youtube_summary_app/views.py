from django.shortcuts import render
from .forms import VideoURLForm
from .main import extract_video_id, get_video_transcript, summarize_text

def generate_summary(request):
    if request.method == 'POST':
        form = VideoURLForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            video_id = extract_video_id(video_url)
            if video_id:
                try:
                    transcript = get_video_transcript(video_id)
                    summary = summarize_text(transcript)
                    return render(request, 'summary.html', {'summary': summary})
                except Exception as e:
                    return render(request, 'index.html', {'error': 'Error generating summary: ' + str(e)})
            else:
                return render(request, 'index.html', {'error': 'Invalid YouTube video URL'})
        else:
            return render(request, 'index.html', {'form': form, 'error': 'Invalid form data'})
    else:
        form = VideoURLForm()
        return render(request, 'index.html', {'form': form})