#! /usr/bin/python3

import argparse
import os
import youtube_dl

class YoutubeDownloader:
    url = ""
    dest = ""
    parser = ""
    defaultPath = os.getcwd() + '/'
     
    def createArgParser(self):
        """Create ArgumentParser object to handle command line args
        """
        self.parser = argparse.ArgumentParser(description='Extract the audio from online video(s).')
        self.parser.add_argument('-u', type=str, required=True, help='The link to your video or playlist.')
        self.parser.add_argument('-f', type=str, nargs='?', 
                                 const=self.defaultPath, default=self.defaultPath, 
                                 help='The path to the audio destination directory.')
        self.parser.add_argument('--playlist', '--p', type=lambda x: (str(x).lower() in ['true', '1', 'yes', 'y']), 
                                 nargs='?', default=False, help='Is this a playlist?')
     
    def getArgs(self):
        """Parse arguements and assign to globals
        """
        args = self.parser.parse_args()
        self.url = args.u 

        if args.playlist == True:
            self.dest = args.f + '%(playlist_title)s/%(title)s.%(ext)s'
        else: 
            self.dest = args.f + '%(title)s.%(ext)s'

        # print(self.defaultPath)

    def downloadAudio(self): 
        """Download specified video or playlist and extract audio with youtube-dl
        """
        options = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': self.dest,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([self.url])


if __name__ == "__main__": 
    downloader = YoutubeDownloader()
    downloader.createArgParser()

    downloader.getArgs()
    downloader.downloadAudio()
    print("Download complete!")
