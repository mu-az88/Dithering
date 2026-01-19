Dithering — Usage Guide

- **Note about the image path (line 79):**
  - Open `Dithering code.py` and go to line 79.
  - Replace the path on that line with the path to the image you want to process. For example:

    ```python
    image_path = r"images\your_image.png"
    ```

  - Use a relative path inside the repository (like `images/your_image.png`) or an absolute path to where the image is stored on your machine.

- **How to upload an image to this repo (PowerShell / Windows):**
  1. Copy your image into the `images/` folder in the repository root.
  2. From the repo root open PowerShell and run:

    ```powershell
    git status
    git add images\your_image.png
    git commit -m "Add example image for dithering"
    git push origin master
    ```

  - If you haven't set a remote yet, set it first (example):

    ```powershell
    git remote add origin https://github.com/your-username/your-repo.git
    git push -u origin master
    ```

- **Quick checklist:**
  - [ ] Put the image file into `images/`.
  - [ ] Update line 79 in `Dithering code.py` to point to that file.
  - [ ] Run the script.

- **Optional improvement (recommended):**
  - Instead of editing line 79 every time, consider changing the script to accept a command-line argument or use a config variable at the top. If you'd like, I can modify the script so it reads `image_path` from an environment variable or `sys.argv[1]`.

If you want me to update `Dithering code.py` to accept a CLI argument (so you won't need to edit line 79), tell me and I'll make that change and demonstrate running it.