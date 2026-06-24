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
| Scale | Multiplier on the polygon cutout size — scales each eye polygon around its centroid (1.0 = tight landmark fit, 1.2 = slightly larger) |
| Both Y | Shift both eye cutouts up or down together (in pickle-half-height units; –1 = bottom, +1 = top) |
| Left X / Y | Fine-tune left eye cutout position (pickle-half-height units) |
| Right X / Y | Fine-tune right eye cutout position (pickle-half-height units) |

> Eye holes are **precise polygons** traced from the MediaPipe eye-contour landmarks (16 points per eye). They automatically follow the shape of your eye as you open/close it. Position offsets are relative to the pickle's current size — a value of **+1.0** moves a feature up by one pickle half-height, so you can shift eyes all the way to the top of the pickle.

### 👄 Mouth
| Slider | What it does |
|---|---|
| Scale | Multiplier on the mouth polygon size (scales around centroid) |
| X / Y Offset | Nudge the mouth cutout position (pickle-half-height units) |

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
| Body rot % | Fraction of head rotation applied to the body (0 = body stays still, 1 = all moves together, >1 = body over-rotates for exaggerated morph) |
| Twist falloff | Power curve — higher values concentrate the twist near the top for a more dramatic deformation |

> The pickle is **one continuous mesh** whose vertices are twisted per their Y position: the bottom (body) rotates by `yaw × bodyRot%` and the top (head) by the full yaw. This creates a natural neck-skin morph effect.

---

## OBS setup

1. Add a **Browser Source** in OBS, URL `http://localhost:8000`
2. Set width/height to match your canvas resolution
3. ✅ Check **"Allow transparency"**
4. In the browser source, press **O** (or click **OBS Mode**) — background turns transparent, UI disappears

> The webcam feed is **never shown** as a background. Only the eye and mouth regions are composited onto the pickle via a hidden 2D canvas layer.