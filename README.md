# 🥒 Pickle Face Tracker

TheBurntPeanut-style face-tracker that replaces your head with a 3-D pickle.  
Eyes and mouth are cut-out holes so your actual face shows through.  
Built with **Three.js** (WebGL pickle mesh) and **MediaPipe FaceMesh** (face tracking), served by a tiny **Python** HTTP server.

---

## Quick start

```bash
python server.py
```

Then open **http://localhost:8000** in Chrome or Edge.

> Requires a webcam and a browser that supports WebRTC (`getUserMedia`).

```
# optional port
python server.py --port 8080
```

---

## Features

| Feature | Detail |
|---|---|
| 3-D pickle mesh | One continuous `LatheGeometry` — no seams |
| Head tracking | Yaw, pitch and roll follow your head in real time |
| Cut-out eyes & mouth | Screen-space GLSL shader punches holes at tracked iris / mouth positions |
| OBS mode | Click **OBS Mode** (or press **O**) → transparent background, all UI hidden |
| Mirror toggle | Press **M** or click **Mirror** |
| Settings panel | Press **S** or click **⚙ Settings** to open sliders |
| Persistent settings | Saved automatically to `localStorage` |
| Reset | "↺ Reset to defaults" button inside the panel |

---

## Settings reference

### 🥒 Pickle
| Slider | What it does |
|---|---|
| Size | Scale the pickle relative to your detected face size |
| X / Y Offset | Shift the pickle left/right or up/down in world space |
| Z (depth) | Move the pickle toward / away from camera |

### 👁 Eyes
| Slider | What it does |
|---|---|
| Radius (px) | Size of the circular cut-out for each eye |
| Both Y (px) | Shift both eye holes up or down together |
| Left X / Y (px) | Fine-tune the left eye hole position |
| Right X / Y (px) | Fine-tune the right eye hole position |

### 👄 Mouth
| Slider | What it does |
|---|---|
| Radius (px) | Size of the circular mouth cut-out |
| X / Y Offset (px) | Nudge the mouth hole |

### 🎯 Tracking
| Slider | What it does |
|---|---|
| Smoothing | Higher = more lag but smoother movement (0 = raw, 0.97 = very smooth) |
| Yaw scale | How much the pickle turns left/right |
| Pitch scale | How much the pickle tilts up/down |
| Roll scale | How much the pickle rolls |

---

## OBS setup

1. Add a **Browser Source** in OBS, URL `http://localhost:8000`
2. Set width/height to match your canvas resolution
3. ✅ Check **"Allow transparency"**
4. In the browser source, press **O** (or click **OBS Mode**) — background turns transparent

Your real webcam source goes on a layer below; the pickle overlay sits on top.