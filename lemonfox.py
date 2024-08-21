import requests

class LemonFox:
    def __init__(self, api_key):
        self.base_url = "https://api.lemonfox.ai/v1"
        self.api_key = api_key

    def transcribe(self, language, is_url=False, audio=None, url=None, mode="json"):
        if is_url:
            if url is None:
                raise ValueError("You have to provide a URL if the is_url parameter is True")
            audio_url = f"{self.base_url}/audio/transcriptions"
            headers = {
                "Authorization": f"Bearer {self.api_key}"
            }
            data = {
                "file": url,
                "language": language,
                "response_format": mode
            }

            response = requests.post(audio_url, headers=headers, data=data)
        else:
            if audio is None:
                raise ValueError("You have to provide an audio file to be transcribed")
            audio_url = f"{self.base_url}/audio/transcriptions"
            headers = {
                "Authorization": f"Bearer {self.api_key}"
            }
            with open(audio, "rb") as f:
                files = {
                    "file": f
                }
                data = {
                    "language": language,
                    "response_format": mode
                }
                response = requests.post(audio_url, headers=headers, files=files, data=data)

        if response.status_code == 200:
            transcription_text = response.text.replace("\\n", "\n")
            return transcription_text
        else:
            raise ValueError(f"An error occurred. Status response from the API: {response.text}")
