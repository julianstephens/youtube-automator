import sys
import os
import youtube_dl

class YoutubeDownloader:
    
    playlist = ""
    folderPath = ""
    dest = ""
    
    def getArgs(self, playlistIndex, folderIndex):
        """Get playlist url and download destination

        Arguments:
            playlistIndex {int} -- Argument index for playlist url
            folderIndex {int} -- Argument index for download directory
        """
        try: 
            self.playlist = str(sys.argv[playlistIndex])
        except Exception:
            print("Provide a YouTube video/playlist link") 
            sys.exit()
        try: 
            self.folderPath = str(sys.argv[folderIndex])
            print("Saving to: " + self.folderPath + '%(title)s.%(ext)s')
        except Exception:
            print("Saving to current directory.")

        user_input = input("Is this a playlist? (Y/n)")
        
        if (user_input.lower() == 'y'):
            self.dest = self.folderPath + '%(playlist_title)s/%(title)s.%(ext)s'
        else: 
            self.dest = self.folderPath + '%(title)s.%(ext)s'
 

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
            ydl.download([self.playlist])



if __name__ == "__main__": 
    downloader = YoutubeDownloader()

    downloader.getArgs(1, 2)
    downloader.downloadAudio()
    print("Download complete!")
