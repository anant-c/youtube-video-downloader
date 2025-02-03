# 🎥 YouTube Video Downloader v1.0

A powerful **YouTube Video Downloader** with:
✅ **Flask Backend** (Hosted on **Render**)
✅ **React Frontend** (Hosted on **Vercel**)
✅ **Command-line Tool** for downloading videos in the highest quality.

---

## 🚀 Features
- Download **YouTube videos** in the **best available quality**.
- Choose between **video + audio** or **audio-only (MP3)**.
- Simple **React UI** to paste a link and download.
- **Terminal app** for direct downloads.

---

## 🏗️ Architecture

### **Backend (Flask - `main2.py`)**
- Uses `yt-dlp` for fetching and downloading YouTube videos.
- Hosted on **Render** for a seamless experience.
- Provides an API for the **React frontend**.

### **Frontend (React - `vercel` Deployment)**
- Simple and modern UI using **React + Vite**.
- Calls the Flask backend to get the download link.
- Hosted on **Vercel** for easy deployment and accessibility.

### **CLI Tool (Terminal - `main.py`)**
- A standalone script for downloading videos via the terminal.
- Automatically selects the **best available format**.
- Perfect for users who prefer **command-line** workflows.

---

## 🔧 How to Set Up Locally

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/anant-c/youtube-video-downloader
cd youtube-video-downloader
```

### **2️⃣ Backend Setup (Flask API)**
```sh
cd backend  # Navigate to the backend folder
pip install -r requirements.txt  # Install dependencies
python main2.py  # Start the Flask server
```
> The backend will be available at `http://127.0.0.1:5000`.

### **3️⃣ Frontend Setup (React UI)**
```sh
cd frontend  # Navigate to the frontend folder
npm install  # Install dependencies
npm run dev  # Start the React frontend
```
> The frontend will run at `http://localhost:5173`.

### **4️⃣ Terminal App (Optional CLI Downloader)**
```sh
python main.py "<YouTube Video URL>"
```

---

## 🔮 Future Work (v2.0 & Beyond)
- **🚀 Direct Streaming:** Let users directly download without downloading in the backend machine.
- **🎨 UI Enhancements:** Make the frontend more visually appealing.
- **🔑 Authentication & Cookies:** Support for downloading even when youtube bans the ip (bot-detection), solution is 
you need to pass your YouTube login session cookies.

---

## 🌎 Deployment
- **Backend**: Hosted on **Render** (`https://youtube-video-downloader-w9mj.onrender.com`).
- **Frontend**: Hosted on **Vercel** (`https://youtube-video-downloader-sandy.vercel.app/`).


## 💡 Contributing
Feel free to **fork**, create a **pull request**, or **open an issue** for improvements! 🚀

