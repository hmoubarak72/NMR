# NMR
This is a README file suitable for GitHub. It provides an overview of the project, instructions for setup, usage guidelines, and deployment options.

NMR Petrophysics Calculator and Visualizer
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

This Streamlit application calculates and visualizes porosity scenarios for Nuclear Magnetic Resonance (NMR) petrophysics. It evaluates different porosities and their respective T2 decay profiles based on user-defined input parameters.

Key Features
- Input Parameters: Users can define relaxivity, sphere radius, and porosity levels via interactive sliders.
- Calculations:
  - Surface area, volume, and surface-to-volume ratio of a sphere.
  - T2 relaxation time based on relaxivity and surface-to-volume ratio.
- Tables: Displays T2 vs Mt values for three porosity scenarios.
- Visualization: Cross-plot of T2 distribution vs porosity decay with customizable markers and labels.

Authors
- Dr. Hesham Moubarak heshammoubarak72@icloud.com
- Mahmoud Abou Shanab Mahmoud.Abou-Shanab@shell.com

Table of Contents
1. [Installation]
2. [Usage]
3. [Deployment]
4. [Contributing]
5. [License]

Installation
Prerequisites
- Python 3.8 or higher
- Pip package manager

Steps
1. Clone this repository:
  To clone the repository and access the specific file (`nmr_T2decay_model.py`) from the provided GitHub link, follow these step-by-step instructions:

Step 1: Install Git
Ensure that you have Git installed on your system. To check if Git is installed, run the following command in your terminal or command prompt:

```bash
git --version

If Git is not installed, download and install it from the official website: [https://git-scm.com/](https://git-scm.com/).

Step 2: Clone the Repository**

The provided link points to a specific file in the repository, but to clone the entire repository, you need the repository's main URL. Based on the link you provided, the repository's main URL is:

https://github.com/hmoubarak72/NMR.git

Run the following command in your terminal or command prompt to clone the repository:

```bash
git clone https://github.com/hmoubarak72/NMR.git
```

This will create a local copy of the repository on your machine.

Step 3: Navigate to the Cloned Repository
After cloning, navigate into the cloned repository directory using the `cd` (change directory) command:

```bash
cd NMR
```

Step 4: Locate the Specific File
The file you are interested in is located in the `main` branch under the path:

nmr_T2decay_model.py
```

You can verify its presence by listing the files in the directory:

```bash
ls
```

If the file is present, you can open it using your preferred text editor or IDE (e.g., VS Code, PyCharm, or Jupyter Notebook).

---

Step 5: Run the Code
1. Ensure you have Python installed. Check your Python version with:
   ```bash
   python --version
   ```

2. Install the required dependencies. If there is a `requirements.txt` file in the repository, install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python nmr_T2decay_model.py
   ```

Optional: Download Only the Specific File
If you don't want to clone the entire repository and only need the specific file (`nmr_T2decay_model.py`), you can download it directly from GitHub:

1. Visit the file's URL: [https://github.com/hmoubarak72/NMR/blob/main/nmr_T2decay_model.py](https://github.com/hmoubarak72/NMR/blob/main/nmr_T2decay_model.py).
2. Click the "Raw" button to view the raw content of the file.
3. Right-click anywhere on the page and select "Save As" to save the file to your computer.

---

Troubleshooting
- Error: Repository Not Found
  Ensure the repository URL is correct and publicly accessible. If the repository is private, you'll need permission from the owner to access it.

- Missing Dependencies
  If you encounter errors related to missing libraries, ensure you install all required dependencies using `pip`.

- File Not Found
  Double-check the file path in the repository. If the file has been moved or renamed, contact the repository owner for clarification.

---

By following these steps, you should be able to successfully clone the repository or download the specific file and run the code locally. Let me know if you encounter any issues!

   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The  file contains the following dependencies:
   streamlit
   pandas
   numpy
   matplotlib
   ```

3. Run the app locally:
   ```bash
   streamlit run app.py
   ```

   Replace `nmr_T2decay_model.py` with the name of your Python file if it differs.

---

Usage
Input Parameters
- Relaxivity (p): Adjust the relaxivity constant in µm/ms using the slider.
- Sphere Radius (r): Set the radius of the sphere in micrometers.
- Porosity Levels: Define three porosity levels (in %) using sliders.

Output
- Calculated Parameters:
  - Surface Area (S): Calculated in µm².
  - Volume (V): Calculated in µm³.
  - Surface-to-Volume Ratio (S/V).
  - T2 Relaxation Time: Calculated in milliseconds.
- Tables: Displays T2 vs Mt values for the three porosity scenarios.
- Cross Plot: Visualizes T2 distribution vs porosity decay for each porosity level.

Deployment
Option 1: Deploy on Streamlit Cloud
1. Push your code to a public GitHub repository.
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repository containing the app code.
4. Streamlit Cloud will automatically detect and deploy the app. Share the generated URL with others.

Option 2: Deploy Locally
1. Run the app locally:
   ```bash
   streamlit run app.py
   ```
2. Access the app via the local network IP address provided by Streamlit.
Option 3: Deploy on Heroku
1. Create a `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

2. Create a `Procfile` with the following content:
   ```
   web: streamlit run app.py --server.port=$PORT
   ```

3. Push your code to Heroku and follow their deployment guide.

Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m "Add YourFeatureName"`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

Please ensure your code adheres to PEP 8 standards and includes appropriate docstrings.

License
This project is licensed under the MIT License. 

Acknowledgments
- Inspired by the need for accessible tools in NMR petrophysics.
- Built using [Streamlit](https://streamlit.io), [Pandas](https://pandas.pydata.org), [NumPy](https://numpy.org), and [Matplotlib](https://matplotlib.org).

