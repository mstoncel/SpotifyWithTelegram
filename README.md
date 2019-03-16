Send spotify detail with Telegram.
- pip install -r requirements.txt

## Usage
    ```python
        from telegramwithspotify import SpotifyWithTelegram
        res = SpotifyWithTelegram(client_id = 'xxx', client_secret = 'xxx', 
              personal_user_name = 'xxxx', api_id =00000,api_hash = 'xxxx')
        res.initial_playlist_tracks('kadiköy müzik')
        res.send_message_user('mesutoncel')
     ```