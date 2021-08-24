# SPOTIFY-Create-and-Update-Playlist-Automation
</br>
<b>This repo contains the code to scrape the billboard website for a particular date and create your own spotify playlist filled with those songs.</b></br>
</br>
DESCRIPTION:</br>
</br>
- This application is developed using beautiful soup, spotipy and requests libraries from python.</br>
- It scrapes data from Billboard website using beautiful soup.</br>
- It then uses the spotipy library to populate a playlist.</br>
- For authorization to spotify you will need to create some environment variables for spotipy to use.</br>
- If you need more info regarding authorization, please read the documentation present at https://spotipy.readthedocs.io/en/2.19.0/ .</br>
- After the user is authorized, a cache file should get created which contains an auth token and refresh token.</br>
- After the Code gets executed, you can check the playlist on your spotify.</br>
</br>
<b> Note: The playlist might not contain all the songs as they are added only if spotipy is able to find them.</b></br>
