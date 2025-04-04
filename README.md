# **Sugar-Auto_SRT**  
🚀 **Automatically generate subtitles (`.srt`) from videos using AI-powered speech recognition.**  

## **Features**  
✔️ Extracts **audio from video**  
✔️ Splits audio **dynamically** for better accuracy  
✔️ Uses **Google Speech Recognition** for **speech-to-text**  
✔️ Outputs **SRT subtitles** formatted for readability  
✔️ Cleans up **temporary files** after processing  

## **Installation & Setup**  
### **1. Clone the Repository**  
```bash
git clone https://github.com/Sugarcube08/Sugar-Auto_SRT.git
cd Sugar-Auto_SRT
```
### **2. Install Dependencies**  
Make sure **Python 3.8+** is installed, then run:  
```bash
pip install -r requirements.txt
```
### **3. Ensure FFmpeg is Installed**  
FFmpeg is needed to process audio. Install it using:  
- **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to **system PATH**  
- **Linux (Debian/Ubuntu)**:  
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```
- **MacOS**:  
  ```bash
  brew install ffmpeg
  ```

## **Usage**  
### **Run the Script**  
```bash
python sugar_auto_srt.py
```
It will prompt:  
```
Enter path: /path/to/video.mp4
```
Provide the full video file path. The script will:  
1️⃣ Extract audio from the video  
2️⃣ Split audio at **silent parts**  
3️⃣ Convert speech to text  
4️⃣ Save subtitles as **captions.srt**  

## **Example Output (`captions.srt`)**
```
1
00:00:01,000 --> 00:00:03,500
This is an example  
of short subtitles.

2
00:00:03,500 --> 00:00:06,000
Automatically generated  
from your video.
```
Subtitles are **auto-formatted** for better readability.  

## **Configuration**  
### **Modify Subtitle Length**  
Change **max characters per line** (default **40 chars**) in `sugar_auto_srt.py`:  
```python
textwrap.fill(text, width=40)
```
### **Adjust Silence Detection**  
Modify `min_silence_len` and `silence_thresh`:  
```python
split_audio_dynamic(audio_path, min_silence_len=700, silence_thresh=-40)
```
- **Lower `min_silence_len`** = **shorter subtitle chunks**  
- **Higher `silence_thresh`** = **detects quieter pauses**  

## **Uninstall & Cleanup**  
To remove everything:  
```bash
rm -rf Sugar-Auto_SRT
```

## **Troubleshooting**  
### **1. `ffmpeg` Not Found?**  
Ensure FFmpeg is installed and added to **system PATH**.  
### **2. Speech Recognition is Inaccurate?**  
- Use **clearer audio**  
- Increase `min_silence_len` for better splits  
- Try **other STT engines** (e.g., `Vosk`)  



---

## Made with ❤️ by SugarCube.
---
Feel free to customize the repository and use it for your own bulk audio volume adjustments! 😄🎶

---
## ☕ Support Me
If you like this project, consider buying me a coffee!
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20Me-orange?style=flat-square&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/sugarcube08)

---
## Don't Forget To Subscribe
### Click on the Following Buttons:
[![YouTube Banner](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://www.youtube.com/@SugarCode-Z?sub_confirmation=1)
[![Instagram Banner](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://www.instagram.com/sugarcodez)
[![WhatsApp Banner](https://img.shields.io/badge/WhatsApp-%25D366.svg?logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029Vb5fFdzKgsNlaxFmhg1T)
