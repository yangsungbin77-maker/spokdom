# -*- coding: utf-8 -*-
"""best grammarly alternatives 글 이미지 2장 fal flux-pro → webp. 상표 없음."""
import os, sys, urllib.request, io
sys.path.insert(0, r"C:/Users/use/클로드 코드/TheLastDay-troy")
import fal_lib
from PIL import Image

OUT = r"C:/Users/use/spokdom/src/assets/posts"
os.makedirs(OUT, exist_ok=True)

JOBS = [
    ("best-grammarly-alternatives.webp",
     "Cinematic clean flat-lay of a modern writer's desk from above, laptop showing an abstract text-editor interface with generic highlighted words and edit marks, notebook, coffee, soft daylight, minimal SaaS aesthetic, calm and professional, no text, no words, no letters, no logos, no brand names"),
    ("best-grammarly-alternatives-compared.webp",
     "Cinematic minimal illustration of several floating app cards comparing writing tools, abstract UI panels with generic checkmarks, sliders and rating bars, soft gradient background in blue and teal, clean SaaS comparison aesthetic, no text, no words, no letters, no logos"),
]

for fname, prompt in JOBS:
    r = fal_lib.run("fal-ai/flux-pro/v1.1",
                    {"prompt": prompt, "image_size": "landscape_16_9", "num_images": 1,
                     "safety_tolerance": "5"}, poll=3, maxwait=180)
    raw = urllib.request.urlopen(r["images"][0]["url"], timeout=120).read()
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    p = os.path.join(OUT, fname)
    img.save(p, "WEBP", quality=88, method=6)
    print("saved", p, img.size)
