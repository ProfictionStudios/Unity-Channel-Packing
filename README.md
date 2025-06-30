# 🎮 Unity ORM Channel Packer (HDRP & URP)

A lightweight texture packing tool to combine **Occlusion**, **Roughness/Smoothness**, and **Metallic** grayscale maps into a single RGBA texture, optimized for Unity's **HDRP** and **URP** pipelines.

---

## 📦 Features

- Supports Unity HDRP and URP Mask Map standards
- Packs grayscale images into correct RGBA channels
- Fast, simple, and works offline
- Ideal for reducing draw calls and texture memory

---

## 🔧 How to Use

### 1. 📥 Install Dependencies

Make sure Python 3.x is installed. Then install the required library:

```bash
pip install pillow
```

*(No other dependencies are needed.)*

---

### 2. 📂 Add Your Files

- Extract this project folder
- Place your grayscale textures into the `source` folder:
  - `ao.png` → Ambient Occlusion
  - `metallic.png` → Metallic
  - `smoothness.png` → Smoothness

*(File names may vary. Just ensure you're referencing them correctly inside the script.)*

---

### 3. ▶️ Run the Script

Open a terminal in the project directory and run:

```bash
python orm_packer.py
```

- The packed texture will be saved in the `output` folder as `orm_packed.png`
- You can rename or batch this as needed

---

## 🎯 Output Format (Channel Layout)

| Channel | Texture            |
|---------|--------------------|
| Red     | Metallic           |
| Green   | Ambient Occlusion  |
| Blue    | (Optional / Detail Mask) |
| Alpha   | Smoothness         |

Compatible with:
- **HDRP Mask Map**
- **URP Lit Shader Mask Map**

---

## 🧰 Tools Used

- [Python 3.x](https://www.python.org/)
- [Pillow (PIL)](https://python-pillow.org/) for image handling

---

## 📎 License

MIT License — Free for personal and commercial use.

---

## 🙌 Contributions

Feel free to fork, improve, or open a pull request to:
- Add batch processing
- Add GUI
- Support more pipelines or custom workflows
---

## 🔗 About the Author

**Developed by Jaswanth Gnanasekar**

- 🌐 [ProfictionStudios.com](https://profictionstudios.com)  
- 🎮 [ArtStation Portfolio](https://adrenoakasharm.artstation.com/)  
- 💼 [LinkedIn](https://www.linkedin.com/in/jaswanth-gnanasekar-677239187/)  
- 📱 [Google Play Developer Page](https://play.google.com/store/apps/dev?id=6724334764661774476)  
- 🎥 [Showreel](https://youtu.be/25UPvEzgeVo)  
- 🕹️ [Game Demo – The Wish](https://youtu.be/-6N9hIAjHe8?si=IvEo9V4NcCK5hhk9)  

Search **"Jaswanth Gnanasekar"** to explore all apps, games, tools, and immersive experiences built across Unity and Unreal ecosystems.
