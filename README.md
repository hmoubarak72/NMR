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
   ```bash
   git clone https: https://github.com/hmoubarak72/NMR.git
   cd NMR
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

