# 📸 PI-Camera-Picture-Labels

> Real-time object detection on a Raspberry Pi 5 — powered by YOLOv8 and Claude AI.

---

## 🧠 About This Project

**PI-Camera-Picture-Labels** is an edge AI computer vision project that uses a Raspberry Pi 5 and a connected camera to capture images and automatically identify objects in real time. YOLOv8 handles the detection, and Claude (Anthropic) adds intelligent labeling and description on top — all running on the Pi.

No cloud vision API. No lag. Just AI on hardware.

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| **Hardware** | Raspberry Pi 5 + Camera Module |
| **Object Detection** | YOLOv8 (Ultralytics) |
| **AI / Labeling** | Claude (Anthropic API), Gemini (Google) |
| **Language** | Python |

---

## ⚙️ How It Works

1. **Capture** — The Pi camera takes a photo or reads a live video frame
2. **Detect** — YOLOv8 runs inference on the image and draws bounding boxes around detected objects
3. **Label** — Claude receives the detection results and generates smart, readable labels or descriptions
4. **Output** — The annotated image is saved or displayed with object names and confidence scores

---

## 🎯 What It Can Identify

YOLOv8 is trained on 80 object classes including:

- People, animals (dogs, cats, birds...)
- Vehicles (cars, bikes, buses...)
- Everyday objects (bottles, chairs, laptops, phones...)
- Food, sports equipment, and more

Claude adds context on top — turning raw detection data into natural language descriptions.

---

## 💡 Key Learnings

- Deploying a computer vision model on edge hardware (no GPU required)
- Combining a local detection model (YOLOv8) with a cloud AI (Claude) in one pipeline
- Working with the Raspberry Pi camera module in Python
- Processing and annotating images programmatically

---

## 📁 Project Structure

```
PI-Camera-Picture-Labels/
├── detect.py          # Main script — capture, detect, label
├── camera.py          # Pi camera setup and capture logic
├── claude_label.py    # Claude API integration for descriptions
├── output/            # Saved annotated images
└── README.md
```

---

## 🚀 Part of the Austin Edge-AI Lab

This project was built during the **Week 2 Physical AI** phase of a 15-day AI Developer Bootcamp in Austin, Texas.  
See the full bootcamp repo → [The AI Bootcamp](../README.md)

---

*Built with a Pi, a camera, and a lot of object detection curiosity.* 🥧📷
