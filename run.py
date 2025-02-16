import os
import shutil
import srt
import speech_recognition as sr
from pydub import AudioSegment, silence
import datetime
import textwrap

TEMP_FOLDER = "temp"

def create_temp_folder():
    """Create a temporary folder if it doesn't exist."""
    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)

def extract_audio(video_path, audio_path="temp/audio.wav"):
    """Extract audio from video using ffmpeg."""
    create_temp_folder()
    print("Extracting audio from video...")
    AudioSegment.from_file(video_path).export(audio_path, format="wav")
    print(f"Audio saved as {audio_path}")
    return audio_path

def split_audio_dynamic(audio_path, min_silence_len=700, silence_thresh=-40):
    """Dynamically split audio at silent parts to improve transcription accuracy."""
    print("Splitting audio into chunks based on silence detection...")
    audio = AudioSegment.from_wav(audio_path)

    chunks = silence.split_on_silence(
        audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh, keep_silence=300
    )

    chunk_paths = []
    start_times = []
    end_times = []

    start_time = 0
    for i, chunk in enumerate(chunks):
        chunk_path = os.path.join(TEMP_FOLDER, f"chunk_{i}.wav")
        chunk.export(chunk_path, format="wav")

        duration = len(chunk)
        end_time = start_time + duration

        chunk_paths.append(chunk_path)
        start_times.append(datetime.timedelta(milliseconds=start_time))
        end_times.append(datetime.timedelta(milliseconds=end_time))

        start_time = end_time  # Move start time for the next chunk

    return chunk_paths, start_times, end_times

def transcribe_audio(chunks, start_times, end_times, output_srt="captions.srt", max_line_length=40):
    """Transcribe audio and save as SRT file with dynamic text wrapping."""
    recognizer = sr.Recognizer()
    subtitles = []

    for i, (chunk_path, start, end) in enumerate(zip(chunks, start_times, end_times)):
        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio_data)

                # Wrap text dynamically to fit subtitles
                wrapped_text = textwrap.fill(text, width=max_line_length)

                subtitles.append(srt.Subtitle(index=i+1, start=start, end=end, content=wrapped_text))
                print(f"Transcribed {start} -> {end}: {wrapped_text}")

            except sr.UnknownValueError:
                print(f"Could not understand audio from {start} to {end}")
                continue

    srt_content = srt.compose(subtitles)

    with open(output_srt, "w", encoding="utf-8") as f:
        f.write(srt_content)

    print(f"Captions saved to {output_srt}")

def cleanup_temp_folder():
    """Remove all files and delete the temp folder."""
    if os.path.exists(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)
        print("Deleted all temporary files.")

if __name__ == "__main__":
    video_path = input("Enter path: ")  # Change to your video file
    audio_path = extract_audio(video_path)
    chunk_paths, start_times, end_times = split_audio_dynamic(audio_path)
    transcribe_audio(chunk_paths, start_times, end_times)
    cleanup_temp_folder()  # Clean up temp folder after processing
