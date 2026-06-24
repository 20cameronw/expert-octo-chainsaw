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
| Scale | Multiplier on the auto-measured eye ellipse (1.0 = tight fit, 1.2 = slightly larger) |
| Both Y (px) | Shift both eye holes up or down together |
| Left X / Y (px) | Fine-tune left eye hole position |
| Right X / Y (px) | Fine-tune right eye hole position |

> Eye holes are **ellipses** whose size is automatically computed each frame from the MediaPipe eye-contour landmarks. They grow/shrink when you open/close your eyes.

### 👄 Mouth
| Slider | What it does |
|---|---|
| Scale | Multiplier on the auto-measured mouth ellipse |
| X / Y Offset (px) | Nudge the mouth hole |

### 🎯 Tracking
| Slider | What it does |
|---|---|
| Smoothing | Higher = more lag but smoother movement (0 = raw, 0.97 = very smooth) |
| Yaw scale | How much the pickle turns left/right (default 0.45 — much subtler than before) |
| Pitch scale | How much the pickle tilts up/down (default 0.35) |
| Roll scale | How much the pickle rolls (default 0.45) |

### 🔄 Neck Twist
| Slider | What it does |
|---|---|
| Body rot % | Fraction of head rotation applied to the body (0 = body stays still, 1 = all moves together) |
| Twist falloff | Power curve — higher values concentrate the twist near the top (head moves more than neck) |

> The pickle is **one continuous mesh** whose vertices are twisted per their Y position: the bottom (body) rotates by `yaw × bodyRot%` and the top (head) by the full yaw. This creates a natural neck-skin morph effect.

---

## OBS setup

1. Add a **Browser Source** in OBS, URL `http://localhost:8000`
2. Set width/height to match your canvas resolution
3. ✅ Check **"Allow transparency"**
4. In the browser source, press **O** (or click **OBS Mode**) — background turns transparent, UI disappears

> The webcam feed is **never shown** as a background. Only the eye and mouth regions are composited onto the pickle via a hidden 2D canvas layer.