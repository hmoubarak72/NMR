"""
NMR Petrophysics Calculator and Visualizer

This Streamlit application calculates and visualizes porosity scenarios for Nuclear Magnetic Resonance (NMR) petrophysics.
It evaluates different porosities and their respective T2 decay profiles based on user-defined input parameters.

Key Features:
- Two tabs: 
  - Tab 1: T2 Decay @ Variant Porosities (Red Background)
  - Tab 2: T2 Decay with Variant Pore Size (Green Background)
- Input parameters for relaxivity, Bore radius, and porosity levels or pore sizes.
- Calculations for surface area, volume, surface-to-volume ratio, and T2 relaxation time.
- Tables displaying T2 vs Mt values for three scenarios.
- Cross-plot visualization of T2 distribution vs porosity decay.
- Error handling for edge cases.
- Dynamic T2 values input by users.
- Unit conversion options (e.g., µm → nm, ms → s).
- Export results as CSV or PNG files.
- Responsive design for smaller screens.

Key Improvements
Tab-Specific Input Parameters :
Each tab now has its own set of input parameters, ensuring no overlap or conflicts between tabs.
Unique key arguments are assigned to all widgets to avoid duplicate widget IDs.
Tab Bar Colors :
The first tab has a red background, and the second tab has a green background using CSS styling.
Dynamic Input Handling :
Users can input custom T2 values dynamically, with error handling for invalid inputs.
Unit Conversion :
Users can switch between units (e.g., µm → nm, ms → s) independently for each tab.
Responsive Design :
Tables and plots adapt to screen size using use_container_width=True.
Export Functionality :
Results can be exported as CSV or PNG files for both tabs.
How to Run the App
Save the code in a file named app.py.
Install dependencies:
bash
Copy
1
pip install streamlit pandas numpy matplotlib
Run the app:
bash
Copy
1
streamlit run T2dist.py

Author: Dr. Hesham Moubarak (heshammoubarak72@icloud.com) and Mahmoud Abou Shanab (Mahmoud.Abou-Shanab@shell.com)
"""
import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# Create two tabs with different colors
tab1, tab2 = st.tabs(["T2 Decay @ Variant Porosities", "T2 Decay with Variant Pore Size"])

# Tab 1: T2 Decay @ Variant Porosities (Red Background)
with tab1:
    # Set background color to red for the first tab
    st.markdown(
        """
        <style>
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
            background-color: red !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title and subtitle
    st.markdown("### T2 Decay @ Variant Porosities")
    st.markdown("""
    Evaluating different porosities and their respective T2 decay profiles.  
    **Author:** Dr. Hesham Moubarak (heshammoubarak72@icloud.com) and Mahmoud Abou Shanab (Mahmoud.Abou-Shanab@shell.com)
    """)

    # Input fields in the sidebar (Tab 1 specific)
    st.sidebar.header("Input Parameters (Tab 1)")
    relaxivity_tab1 = st.sidebar.slider(
        "Relaxivity (p) (in µm/ms):",
        min_value=0.001,
        max_value=0.01,
        value=0.003,
        step=0.001,
        format="%.4f",
        key="relaxivity_tab1"
    )
    bore_radius_tab1 = st.sidebar.slider(
        "Bore Radius (r in µm):",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01,
        format="%.2f",
        key="bore_radius_tab1"
    )
    porosity_1_tab1 = st.sidebar.slider(
        "Porosity 1 (%):",
        min_value=0,
        max_value=100,
        value=30,
        step=1,
        key="porosity_1_tab1"
    )
    porosity_2_tab1 = st.sidebar.slider(
        "Porosity 2 (%):",
        min_value=0,
        max_value=100,
        value=20,
        step=1,
        key="porosity_2_tab1"
    )
    porosity_3_tab1 = st.sidebar.slider(
        "Porosity 3 (%):",
        min_value=0,
        max_value=100,
        value=10,
        step=1,
        key="porosity_3_tab1"
    )

    # Dynamic T2 Values
    st.sidebar.subheader("T2 Distribution")
    custom_t2_values_tab1 = st.sidebar.text_input(
        "Enter custom T2 values (comma-separated, e.g., 0.5, 1, 2, 4):",
        value="0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024",
        key="custom_t2_values_tab1"
    )
    try:
        slider_t2_values_tab1 = [float(t.strip()) for t in custom_t2_values_tab1.split(",")]
    except ValueError:
        st.error("Invalid T2 values. Please enter comma-separated numbers.")
        slider_t2_values_tab1 = [0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    # Unit Conversion
    unit_options = {"µm": 1, "nm": 1000, "ms": 1, "s": 0.001}
    radius_unit_tab1 = st.sidebar.selectbox("Select radius unit:", list(unit_options.keys()), key="radius_unit_tab1")
    time_unit_tab1 = st.sidebar.selectbox("Select time unit:", list(unit_options.keys()), key="time_unit_tab1")

    # Adjust units
    bore_radius_tab1 *= unit_options[radius_unit_tab1]
    slider_t2_values_tab1 = [t * unit_options[time_unit_tab1] for t in slider_t2_values_tab1]

    def calculate_surface_area(radius):
        return 4 * math.pi * radius**2

    def calculate_volume(radius):
        return (4/3) * math.pi * radius**3

    def calculate_surface_to_volume_ratio(surface_area, volume):
        return surface_area / volume if volume != 0 else 0

    def calculate_t2(relaxivity, surface_to_volume_ratio):
        try:
            return 1 / (relaxivity * surface_to_volume_ratio) if surface_to_volume_ratio != 0 else 0
        except ZeroDivisionError:
            st.error("Numerical instability detected. Please check your input parameters.")
            return 0

    # Surface area, volume, and S/V ratio calculations
    surface_area_tab1 = calculate_surface_area(bore_radius_tab1)
    volume_tab1 = calculate_volume(bore_radius_tab1)
    surface_to_volume_ratio_tab1 = calculate_surface_to_volume_ratio(surface_area_tab1, volume_tab1)
    t2_tab1 = calculate_t2(relaxivity_tab1, surface_to_volume_ratio_tab1)

    # Display calculations
    st.subheader("Calculated Parameters")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Surface Area (S): {surface_area_tab1:.4f} µm²")
        st.write(f"Volume (V): {volume_tab1:.4f} µm³")
    with col2:
        st.write(f"Surface-to-Volume Ratio (S/V): {surface_to_volume_ratio_tab1:.4f}")
        st.write(f"T2: {t2_tab1:.4f} ms")

    # Mt calculations
    mt1_values_tab1 = [porosity_1_tab1 * math.exp(-t / t2_tab1) if t2_tab1 > 0 else 0 for t in slider_t2_values_tab1]
    mt2_values_tab1 = [porosity_2_tab1 * math.exp(-t / t2_tab1) if t2_tab1 > 0 else 0 for t in slider_t2_values_tab1]
    mt3_values_tab1 = [porosity_3_tab1 * math.exp(-t / t2_tab1) if t2_tab1 > 0 else 0 for t in slider_t2_values_tab1]

    # Create DataFrames for tables
    df_mt1_tab1 = pd.DataFrame({"T2": slider_t2_values_tab1, "Mt1": mt1_values_tab1})
    df_mt2_tab1 = pd.DataFrame({"T2": slider_t2_values_tab1, "Mt2": mt2_values_tab1})
    df_mt3_tab1 = pd.DataFrame({"T2": slider_t2_values_tab1, "Mt3": mt3_values_tab1})

    # Export Results
    st.subheader("Export Results")
    if st.button("Download Tables as CSV", key="download_csv_tab1"):
        df_combined_tab1 = pd.concat([df_mt1_tab1, df_mt2_tab1["Mt2"], df_mt3_tab1["Mt3"]], axis=1)
        csv_tab1 = df_combined_tab1.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv_tab1,
            file_name="nmr_petrophysics_results_tab1.csv",
            mime="text/csv"
        )

    # Display tables side by side
    st.subheader("Tables: T2 vs Mt Values")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Table 1: T2 and Mt1")
        st.dataframe(df_mt1_tab1.style.format({"T2": "{:.1f}", "Mt1": "{:.4f}"}), use_container_width=True)
    with col2:
        st.write("Table 2: T2 and Mt2")
        st.dataframe(df_mt2_tab1.style.format({"T2": "{:.1f}", "Mt2": "{:.4f}"}), use_container_width=True)
    with col3:
        st.write("Table 3: T2 and Mt3")
        st.dataframe(df_mt3_tab1.style.format({"T2": "{:.1f}", "Mt3": "{:.4f}"}), use_container_width=True)

    # Cross Plot: T2 Distribution vs Porosity
    st.subheader("Cross Plot: Porosity T2 Decay")
    fig_data_tab1 = {
        "T2": slider_t2_values_tab1,
        "Mt1": mt1_values_tab1,
        "Mt2": mt2_values_tab1,
        "Mt3": mt3_values_tab1
    }
    df_plot_tab1 = pd.DataFrame(fig_data_tab1)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_plot_tab1["T2"], df_plot_tab1["Mt1"], label=f"Porosity 1 ({porosity_1_tab1}%)", marker='o')
    ax.plot(df_plot_tab1["T2"], df_plot_tab1["Mt2"], label=f"Porosity 2 ({porosity_2_tab1}%)", marker='s')
    ax.plot(df_plot_tab1["T2"], df_plot_tab1["Mt3"], label=f"Porosity 3 ({porosity_3_tab1}%)", marker='^')
    ax.set_title("Porosity T2 Decay", fontsize=14)
    ax.set_xlabel(f"T2 Distribution ({time_unit_tab1})", fontsize=12)
    ax.set_ylabel("Porosity (%)", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)

    # Export Plot
    if st.button("Download Plot as PNG", key="download_plot_tab1"):
        fig.savefig("nmr_petrophysics_plot_tab1.png", dpi=300, bbox_inches="tight")
        with open("nmr_petrophysics_plot_tab1.png", "rb") as file:
            st.download_button(
                label="Download PNG",
                data=file,
                file_name="nmr_petrophysics_plot_tab1.png",
                mime="image/png"
            )

    st.pyplot(fig)

    st.caption(f"""
    **X-axis:** T2 Distribution ({time_unit_tab1})  
    **Y-axis:** Porosity (%)  
    Labels: Each line represents a porosity level (Mt1, Mt2, Mt3).
    """)

# Tab 2: T2 Decay with Variant Pore Size (Green Background)
with tab2:
    # Set background color to green for the second tab
    st.markdown(
        """
        <style>
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
            background-color: green !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title and subtitle
    st.markdown("### T2 Decay with Variant Pore Size")
    st.markdown("""
    Evaluating different pore sizes and their respective T2 decay profiles.  
    **Author:** Dr. Hesham Moubarak (heshammoubarak72@icloud.com) and Mahmoud Abou Shanab (Mahmoud.Abou-Shanab@shell.com)
    """)

    # Input fields in the sidebar (Tab 2 specific)
    st.sidebar.header("Input Parameters (Tab 2)")
    relaxivity_tab2 = st.sidebar.slider(
        "Relaxivity (p) (in µm/ms):",
        min_value=0.001,
        max_value=0.01,
        value=0.003,
        step=0.001,
        format="%.4f",
        key="relaxivity_tab2"
    )
    pore_size_1_tab2 = st.sidebar.slider(
        "Pore Size 1 (r in µm):",
        min_value=0.0,
        max_value=1.0,
        value=1.0,
        step=0.01,
        format="%.2f",
        key="pore_size_1_tab2"
    )
    pore_size_2_tab2 = st.sidebar.slider(
        "Pore Size 2 (r in µm):",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01,
        format="%.2f",
        key="pore_size_2_tab2"
    )
    pore_size_3_tab2 = st.sidebar.slider(
        "Pore Size 3 (r in µm):",
        min_value=0.0,
        max_value=1.0,
        value=0.25,
        step=0.01,
        format="%.2f",
        key="pore_size_3_tab2"
    )
    porosity_tab2 = st.sidebar.slider(
        "Porosity (%):",
        min_value=0,
        max_value=100,
        value=50,
        step=1,
        key="porosity_tab2"
    )

    # Dynamic T2 Values
    st.sidebar.subheader("T2 Distribution")
    custom_t2_values_tab2 = st.sidebar.text_input(
        "Enter custom T2 values (comma-separated, e.g., 0.5, 1, 2, 4):",
        value="0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024",
        key="custom_t2_values_tab2"
    )
    try:
        slider_t2_values_tab2 = [float(t.strip()) for t in custom_t2_values_tab2.split(",")]
    except ValueError:
        st.error("Invalid T2 values. Please enter comma-separated numbers.")
        slider_t2_values_tab2 = [0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    # Unit Conversion
    unit_options = {"µm": 1, "nm": 1000, "ms": 1, "s": 0.001}
    radius_unit_tab2 = st.sidebar.selectbox("Select radius unit:", list(unit_options.keys()), key="radius_unit_tab2")
    time_unit_tab2 = st.sidebar.selectbox("Select time unit:", list(unit_options.keys()), key="time_unit_tab2")

    # Adjust units
    pore_size_1_tab2 *= unit_options[radius_unit_tab2]
    pore_size_2_tab2 *= unit_options[radius_unit_tab2]
    pore_size_3_tab2 *= unit_options[radius_unit_tab2]
    slider_t2_values_tab2 = [t * unit_options[time_unit_tab2] for t in slider_t2_values_tab2]

    # Surface area, volume, and S/V ratio calculations
    surface_area_1_tab2 = calculate_surface_area(pore_size_1_tab2)
    surface_area_2_tab2 = calculate_surface_area(pore_size_2_tab2)
    surface_area_3_tab2 = calculate_surface_area(pore_size_3_tab2)
    volume_1_tab2 = calculate_volume(pore_size_1_tab2)
    volume_2_tab2 = calculate_volume(pore_size_2_tab2)
    volume_3_tab2 = calculate_volume(pore_size_3_tab2)
    surface_to_volume_ratio_1_tab2 = calculate_surface_to_volume_ratio(surface_area_1_tab2, volume_1_tab2)
    surface_to_volume_ratio_2_tab2 = calculate_surface_to_volume_ratio(surface_area_2_tab2, volume_2_tab2)
    surface_to_volume_ratio_3_tab2 = calculate_surface_to_volume_ratio(surface_area_3_tab2, volume_3_tab2)
    t2_1_tab2 = calculate_t2(relaxivity_tab2, surface_to_volume_ratio_1_tab2)
    t2_2_tab2 = calculate_t2(relaxivity_tab2, surface_to_volume_ratio_2_tab2)
    t2_3_tab2 = calculate_t2(relaxivity_tab2, surface_to_volume_ratio_3_tab2)

    # Display calculations
    st.subheader("Calculated Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"Pore Size 1: {pore_size_1_tab2:.2f} µm")
        st.write(f"Surface Area (S): {surface_area_1_tab2:.4f} µm²")
        st.write(f"Volume (V): {volume_1_tab2:.4f} µm³")
        st.write(f"Surface-to-Volume Ratio (S/V): {surface_to_volume_ratio_1_tab2:.4f}")
        st.write(f"T2: {t2_1_tab2:.4f} ms")
    with col2:
        st.write(f"Pore Size 2: {pore_size_2_tab2:.2f} µm")
        st.write(f"Surface Area (S): {surface_area_2_tab2:.4f} µm²")
        st.write(f"Volume (V): {volume_2_tab2:.4f} µm³")
        st.write(f"Surface-to-Volume Ratio (S/V): {surface_to_volume_ratio_2_tab2:.4f}")
        st.write(f"T2: {t2_2_tab2:.4f} ms")
    with col3:
        st.write(f"Pore Size 3: {pore_size_3_tab2:.2f} µm")
        st.write(f"Surface Area (S): {surface_area_3_tab2:.4f} µm²")
        st.write(f"Volume (V): {volume_3_tab2:.4f} µm³")
        st.write(f"Surface-to-Volume Ratio (S/V): {surface_to_volume_ratio_3_tab2:.4f}")
        st.write(f"T2: {t2_3_tab2:.4f} ms")

    # Mt calculations
    mt1_values_tab2 = [porosity_tab2 * math.exp(-t / t2_1_tab2) if t2_1_tab2 > 0 else 0 for t in slider_t2_values_tab2]
    mt2_values_tab2 = [porosity_tab2 * math.exp(-t / t2_2_tab2) if t2_2_tab2 > 0 else 0 for t in slider_t2_values_tab2]
    mt3_values_tab2 = [porosity_tab2 * math.exp(-t / t2_3_tab2) if t2_3_tab2 > 0 else 0 for t in slider_t2_values_tab2]

    # Create DataFrames for tables
    df_mt1_tab2 = pd.DataFrame({"T2": slider_t2_values_tab2, "Mt1": mt1_values_tab2})
    df_mt2_tab2 = pd.DataFrame({"T2": slider_t2_values_tab2, "Mt2": mt2_values_tab2})
    df_mt3_tab2 = pd.DataFrame({"T2": slider_t2_values_tab2, "Mt3": mt3_values_tab2})

    # Export Results
    st.subheader("Export Results")
    if st.button("Download Tables as CSV", key="download_csv_tab2"):
        df_combined_tab2 = pd.concat([df_mt1_tab2, df_mt2_tab2["Mt2"], df_mt3_tab2["Mt3"]], axis=1)
        csv_tab2 = df_combined_tab2.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv_tab2,
            file_name="nmr_petrophysics_results_tab2.csv",
            mime="text/csv"
        )

    # Display tables side by side
    st.subheader("Tables: T2 vs Mt Values")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Table 1: T2 and Mt1")
        st.dataframe(df_mt1_tab2.style.format({"T2": "{:.1f}", "Mt1": "{:.4f}"}), use_container_width=True)
    with col2:
        st.write("Table 2: T2 and Mt2")
        st.dataframe(df_mt2_tab2.style.format({"T2": "{:.1f}", "Mt2": "{:.4f}"}), use_container_width=True)
    with col3:
        st.write("Table 3: T2 and Mt3")
        st.dataframe(df_mt3_tab2.style.format({"T2": "{:.1f}", "Mt3": "{:.4f}"}), use_container_width=True)

    # Cross Plot: T2 Distribution vs Porosity
    st.subheader("Cross Plot: Pore Size T2 Decay")
    fig_data_tab2 = {
        "T2": slider_t2_values_tab2,
        "Mt1": mt1_values_tab2,
        "Mt2": mt2_values_tab2,
        "Mt3": mt3_values_tab2
    }
    df_plot_tab2 = pd.DataFrame(fig_data_tab2)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_plot_tab2["T2"], df_plot_tab2["Mt1"], label=f"Pore Size 1 ({pore_size_1_tab2:.2f} µm)", marker='o')
    ax.plot(df_plot_tab2["T2"], df_plot_tab2["Mt2"], label=f"Pore Size 2 ({pore_size_2_tab2:.2f} µm)", marker='s')
    ax.plot(df_plot_tab2["T2"], df_plot_tab2["Mt3"], label=f"Pore Size 3 ({pore_size_3_tab2:.2f} µm)", marker='^')
    ax.set_title("Pore Size T2 Decay", fontsize=14)
    ax.set_xlabel(f"T2 Distribution ({time_unit_tab2})", fontsize=12)
    ax.set_ylabel("Porosity (%)", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)

    # Export Plot
    if st.button("Download Plot as PNG", key="download_plot_tab2"):
        fig.savefig("nmr_petrophysics_plot_tab2.png", dpi=300, bbox_inches="tight")
        with open("nmr_petrophysics_plot_tab2.png", "rb") as file:
            st.download_button(
                label="Download PNG",
                data=file,
                file_name="nmr_petrophysics_plot_tab2.png",
                mime="image/png"
            )

    st.pyplot(fig)

    st.caption(f"""
    **X-axis:** T2 Distribution ({time_unit_tab2})  
    **Y-axis:** Porosity (%)  
    Labels: Each line represents a pore size level (Mt1, Mt2, Mt3).
    """)