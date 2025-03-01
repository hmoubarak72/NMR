"""
NMR Petrophysics Calculator and Visualizer

This Streamlit application calculates and visualizes porosity scenarios for Nuclear Magnetic Resonance (NMR) petrophysics.
It evaluates different porosities and their respective T2 decay profiles based on user-defined input parameters.

Key Features:
- Input parameters for relaxivity, sphere radius, and porosity levels.
- Calculations for surface area, volume, surface-to-volume ratio, and T2 relaxation time.
- Tables displaying T2 vs Mt values for three porosity scenarios.
- Cross-plot visualization of T2 distribution vs porosity decay.
- Error handling for edge cases.
- Dynamic T2 values input by users.
- Unit conversion options (e.g., µm → nm, ms → s).
- Export results as CSV or PNG files.
- Responsive design for smaller screens.

Author: Dr. Hesham Moubarak (heshammoubarak72@icloud.com) and Mahmoud Abou Shanab (Mahmoud.Abou-Shanab@shell.com)
"""

import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# Title with large font
st.markdown("<h1 style='text-align: center; font-size: 40px;'>NMR (Nuclear Magnetic Resonance) Petrophysics</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("""
<h3 style='text-align: center; font-size: 20px;'>
Porosity Scenarios: Evaluating different porosities and their respective T2 decay profiles.<br>
Author: Dr. Hesham Moubarak (heshammoubarak72@icloud.com) and Mahmoud Abou Shanab (Mahmoud.Abou-Shanab@shell.com)
</h3>
""", unsafe_allow_html=True)

# Input fields in the sidebar
st.sidebar.header("Input Parameters")
relaxivity = st.sidebar.slider(
    "Relaxivity (p) (in µm/ms):",
    min_value=0.001,
    max_value=0.01,
    value=0.003,
    step=0.001,
    format="%.4f"
)
sphere_radius = st.sidebar.slider(
    "Sphere Radius (r in µm):",
    min_value=0.1,
    max_value=5.0,
    value=1.0,
    step=0.1,
    format="%.2f"
)
porosity_1 = st.sidebar.slider(
    "Porosity 1 (%):",
    min_value=0,
    max_value=100,
    value=30,
    step=1
)
porosity_2 = st.sidebar.slider(
    "Porosity 2 (%):",
    min_value=0,
    max_value=100,
    value=20,
    step=1
)
porosity_3 = st.sidebar.slider(
    "Porosity 3 (%):",
    min_value=0,
    max_value=100,
    value=10,
    step=1
)

# Dynamic T2 Values
st.sidebar.subheader("T2 Distribution")
custom_t2_values = st.sidebar.text_input(
    "Enter custom T2 values (comma-separated, e.g., 0.5, 1, 2, 4):",
    value="0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024"
)
try:
    slider_t2_values = [float(t.strip()) for t in custom_t2_values.split(",")]
except ValueError:
    st.error("Invalid T2 values. Please enter comma-separated numbers.")
    slider_t2_values = [0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# Unit Conversion
unit_options = {"µm": 1, "nm": 1000, "ms": 1, "s": 0.001}
radius_unit = st.sidebar.selectbox("Select radius unit:", list(unit_options.keys()))
time_unit = st.sidebar.selectbox("Select time unit:", list(unit_options.keys()))

# Adjust units
sphere_radius *= unit_options[radius_unit]
slider_t2_values = [t * unit_options[time_unit] for t in slider_t2_values]

def calculate_surface_area(radius):
    """
    Calculate the surface area of a sphere given its radius.

    Parameters:
        radius (float): Radius of the sphere in micrometers.

    Returns:
        float: Surface area of the sphere in square micrometers.
    """
    return 4 * math.pi * radius**2


def calculate_volume(radius):
    """
    Calculate the volume of a sphere given its radius.

    Parameters:
        radius (float): Radius of the sphere in micrometers.

    Returns:
        float: Volume of the sphere in cubic micrometers.
    """
    return (4/3) * math.pi * radius**3


def calculate_surface_to_volume_ratio(surface_area, volume):
    """
    Calculate the surface-to-volume ratio of a sphere.

    Parameters:
        surface_area (float): Surface area of the sphere.
        volume (float): Volume of the sphere.

    Returns:
        float: Surface-to-volume ratio (S/V). Returns 0 if volume is zero.
    """
    return surface_area / volume if volume != 0 else 0


def calculate_t2(relaxivity, surface_to_volume_ratio):
    """
    Calculate the T2 relaxation time based on relaxivity and surface-to-volume ratio.

    Parameters:
        relaxivity (float): Relaxivity constant in µm/ms.
        surface_to_volume_ratio (float): Surface-to-volume ratio of the sphere.

    Returns:
        float: T2 relaxation time in milliseconds. Returns 0 if S/V ratio is zero.
    """
    try:
        return 1 / (relaxivity * surface_to_volume_ratio) if surface_to_volume_ratio != 0 else 0
    except ZeroDivisionError:
        st.error("Numerical instability detected. Please check your input parameters.")
        return 0


# Surface area, volume, and S/V ratio calculations
surface_area = calculate_surface_area(sphere_radius)
volume = calculate_volume(sphere_radius)
surface_to_volume_ratio = calculate_surface_to_volume_ratio(surface_area, volume)
t2 = calculate_t2(relaxivity, surface_to_volume_ratio)

# Display calculations
st.subheader("Calculated Parameters")
col1, col2 = st.columns(2)
with col1:
    st.write(f"Surface Area (S): {surface_area:.4f} µm²")
    st.write(f"Volume (V): {volume:.4f} µm³")
with col2:
    st.write(f"Surface-to-Volume Ratio (S/V): {surface_to_volume_ratio:.4f}")
    st.write(f"T2: {t2:.4f} ms")

# Mt calculations
mt1_values = [porosity_1 * math.exp(-t / t2) if t2 > 0 else 0 for t in slider_t2_values]
mt2_values = [porosity_2 * math.exp(-t / t2) if t2 > 0 else 0 for t in slider_t2_values]
mt3_values = [porosity_3 * math.exp(-t / t2) if t2 > 0 else 0 for t in slider_t2_values]

# Create DataFrames for tables
df_mt1 = pd.DataFrame({"T2": slider_t2_values, "Mt1": mt1_values})
df_mt2 = pd.DataFrame({"T2": slider_t2_values, "Mt2": mt2_values})
df_mt3 = pd.DataFrame({"T2": slider_t2_values, "Mt3": mt3_values})

# Export Results
st.subheader("Export Results")
if st.button("Download Tables as CSV"):
    df_combined = pd.concat([df_mt1, df_mt2["Mt2"], df_mt3["Mt3"]], axis=1)
    csv = df_combined.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="nmr_petrophysics_results.csv",
        mime="text/csv"
    )

# Display tables side by side
st.subheader("Tables: T2 vs Mt Values")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Table 1: T2 and Mt1")
    st.dataframe(df_mt1.style.format({"T2": "{:.1f}", "Mt1": "{:.4f}"}), use_container_width=True)
with col2:
    st.write("Table 2: T2 and Mt2")
    st.dataframe(df_mt2.style.format({"T2": "{:.1f}", "Mt2": "{:.4f}"}), use_container_width=True)
with col3:
    st.write("Table 3: T2 and Mt3")
    st.dataframe(df_mt3.style.format({"T2": "{:.1f}", "Mt3": "{:.4f}"}), use_container_width=True)

# Cross Plot: T2 Distribution vs Porosity
st.subheader("Cross Plot: Porosity T2 Decay")
fig_data = {
    "T2": slider_t2_values,
    "Mt1": mt1_values,
    "Mt2": mt2_values,
    "Mt3": mt3_values
}
df_plot = pd.DataFrame(fig_data)

fig, ax = plt.subplots(figsize=(10, 5))  # Make the plot wider
ax.plot(df_plot["T2"], df_plot["Mt1"], label=f"Porosity 1 ({porosity_1}%)", marker='o')
ax.plot(df_plot["T2"], df_plot["Mt2"], label=f"Porosity 2 ({porosity_2}%)", marker='s')
ax.plot(df_plot["T2"], df_plot["Mt3"], label=f"Porosity 3 ({porosity_3}%)", marker='^')
ax.set_title("Porosity T2 Decay", fontsize=14)
ax.set_xlabel(f"T2 Distribution ({time_unit})", fontsize=12)
ax.set_ylabel("Porosity (%)", fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

# Export Plot
if st.button("Download Plot as PNG"):
    fig.savefig("nmr_petrophysics_plot.png", dpi=300, bbox_inches="tight")
    with open("nmr_petrophysics_plot.png", "rb") as file:
        st.download_button(
            label="Download PNG",
            data=file,
            file_name="nmr_petrophysics_plot.png",
            mime="image/png"
        )

st.pyplot(fig)

st.caption(f"""
**X-axis:** T2 Distribution ({time_unit})<br>
**Y-axis:** Porosity (%)<br>
Labels: Each line represents a porosity level (Mt1, Mt2, Mt3).
""", unsafe_allow_html=True)
