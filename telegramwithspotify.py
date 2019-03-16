import time
import requests
import json
import spotipy
from telethon import TelegramClient, events, sync

# https://my.telegram.org

class AuthTelegram:
    def __init__(self, api_id:int, api_hash:str):
        self.api_id = int(api_id)
        self.api_hash = api_hash

    @property
    def start_client(self)->object:
        client = TelegramClient('session_api', self.api_id, self.api_hash)
        client.start()
        return client


class SpotifyWithTelegram(AuthTelegram):
    def __init__(self, client_id:str, client_secret:str, personal_user_name:str, *args, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.personal_user_name = personal_user_name
        self.playlist_name = None
        self.payload = None

        super().__init__(*args, **kwargs)

    @property
    def sp(self)->object:
        client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=self.client_id,
                                                              client_secret=self.client_secret)
        token = client_credentials_manager.get_access_token()
        return spotipy.Spotify(auth=token)

    
    def initial_user_playists(self):
        playlist = self.sp.user_playlists(self.personal_user_name)
        for item in playlist.get('items'):
            if item.get('name').upper() == self.playlist_name.upper():
                return item.get('id')

    def initial_playlist_tracks(self, playlist_name:str)->dict:
        self.playlist_name = playlist_name
        playlist_tracks = self.sp.user_playlist_tracks(
            self.personal_user_name, self.initial_user_playists())
        self.payload = playlist_tracks.get('items')
        return playlist_tracks.get('items')

    def send_message_user(self, send_username:str)-> None:
        for item in self.payload:
                url = item.get('track').get('album').get('external_urls').get('spotify')
                self.start_client.send_message(send_username, url)

