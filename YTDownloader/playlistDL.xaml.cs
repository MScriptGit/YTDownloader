using System;
using System.IO;
using Microsoft.Maui;
using Microsoft.Maui.Controls;
using YoutubeExplode;

namespace YTDownloader
{
    public partial class playlistDL : ContentPage
    {
        public playlistDL()
        {
            InitializeComponent();

        }

        private async void getEntry(object sender, EventArgs e)
        {
            //get url
            string inputText = userInput.Text;



            var youtube = new YoutubeClient();

            // You can specify either the video URL or its ID
            var videoUrl = "https://youtube.com/watch?v=u_yIGGhubZs";
            var video = await youtube.Videos.GetAsync(videoUrl);

            var title = video.Title; // "Collections - Blender 2.80 Fundamentals"
            var author = video.Author.ChannelTitle; // "Blender"
            var duration = video.Duration; // 00:07:20





            //output??
            outputTxt.Text = "title";
        }
    }
}