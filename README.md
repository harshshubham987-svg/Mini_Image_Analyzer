**Mini Image Analyzer**

- **Project**: A tiny Python script that performs basic intensity analysis on a small grayscale image represented as a 2D list.
- **Language**: Python

**Files**
- **Script:** [mini_image_analyzer.py](mini_image_analyzer.py) — computes totals, averages, brightest/darkest pixels, per-row brightness, diagonal sum, and creates an inverted image.

**Quick Description**
- **What it does:** Reads a hard-coded 2D list named `image` and prints summary statistics and an inverted image.

**Usage**
- **Run:**
```bash
python mini_image_analyzer.py
```

**Expected Output (example)**
- **Image Dimensions:** : 3 x 3
- **Total Pixels:** : 9
- **Total Intensity:** : 982
- **Average Intensity:** : 109.11111111111111
- **Brightness Pixel:** : 255
- **Drakest Pixel:** : 12
- **Row 0 Brightness:** : 257
- **Row 1 Brightness:** : 379
- **Row 2 Brightness:** : 279
- **Diagonal Intensity:** : 178
- **Inverted Image:**
- [243, 210, 55]
- [221, 0, 165]
- [132, 188, 166]

**Code Notes / Explanation**
- **Input representation:** The image is a 2D Python list `image` where each element is an integer intensity (0–255).
- **Computed metrics:** total intensity, average, brightest/darkest pixel, per-row sums, diagonal sum, and inverted pixels (`255 - value`).
- **Extending:** To analyze different images, replace the `image` list in [mini_image_analyzer.py](mini_image_analyzer.py) or adapt the script to load external image files or CSV data.

**How to extend or test**
- Replace the `image` variable with other 2D lists to validate behavior.
- Add functions to encapsulate each metric for unit testing.


Author: Harsh Shubham Singh