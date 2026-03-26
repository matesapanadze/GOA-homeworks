import React from "react";
import incredibleAudio from "/assets/audios/audio.mp3";
import incredibleVideo from "/assets/videos/video.mp4";
import ReactPlayer from "react-player";
import {
  MediaController,
  MediaControlBar,
  MediaTimeRange,
  MediaTimeDisplay,
  MediaVolumeRange,
  MediaPlaybackRateButton,
  MediaPlayButton,
  MediaSeekBackwardButton,
  MediaSeekForwardButton,
  MediaMuteButton,
  MediaFullscreenButton,
} from "media-chrome/react";

export default function App() {
  return (
    <div>
      <p>video</p>
      <audio controls src={incredibleAudio}></audio>
      <video controls src={incredibleVideo}></video>
      <MediaController
        style={{
          width: "100%",
          aspectRatio: "16/9",
        }}
      >
        <ReactPlayer
          slot="media"
          src={incredibleVideo}
          controls={false}
          style={{
            width: "100%",
            height: "100%",
            "--controls": "none",
          }}
        ></ReactPlayer>
        <MediaControlBar>
          <MediaPlayButton />
          <MediaSeekBackwardButton seekOffset={10} />
          <MediaSeekForwardButton seekOffset={10} />
          <MediaTimeRange />
          <MediaTimeDisplay showDuration />
          <MediaMuteButton />
          <MediaVolumeRange />
          <MediaPlaybackRateButton />
          <MediaFullscreenButton />
        </MediaControlBar>
      </MediaController>
      ;
    </div>
  );
}
