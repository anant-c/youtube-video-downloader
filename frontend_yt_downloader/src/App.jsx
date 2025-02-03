import { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [audioOnly, setAudioOnly] = useState(false);
  const [downloadLink, setDownloadLink] = useState(null);  // ✅ Add this state
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleDownload = async () => {
    setLoading(true);
    setError(null);
    setDownloadLink(null);  // ✅ Reset download link before fetching

    try {
      const response = await fetch("https://youtube-video-downloader-w9mj.onrender.com/download", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url, audio_only: audioOnly }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();

      if (data.success) {
        setDownloadLink(`https://youtube-video-downloader-w9mj.onrender.com/get-file/${data.file}`);
      } else {
        setError("Download failed. Try again.");
      }
    } 
    catch (err) {
      setError(`An error occurred: ${err.message}`);
    } 
    finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>YouTube Video Downloader</h1>
      <input
        type="text"
        placeholder="Enter YouTube URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <label>
        <input
          type="checkbox"
          checked={audioOnly}
          onChange={() => setAudioOnly(!audioOnly)}
        />
        Download as MP3
      </label>
      <button onClick={handleDownload} disabled={loading}>
        {loading ? "Getting link..." : "Get Download Link"}
      </button>

      {error && <p className="error">{error}</p>}

      {downloadLink && (  // ✅ Display download link when available
        <div>
          <p>Click below to download:</p>
          <a href={downloadLink} target="_blank" rel="noopener noreferrer">
            Download Now
          </a>
        </div>
      )}
    </div>
  );
}

export default App;
