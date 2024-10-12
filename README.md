# CancerIQ: Fast, AI-Powered Diagnosis

CancerIQ is an AI-driven tool designed to assist cytology labs in diagnosing breast cancer. By leveraging machine learning, the app predicts whether a breast mass is benign or malignant based on lab measurements, providing a fast and accurate diagnostic solution.

You can either connect the app directly to your cytology lab or manually input measurements using the interactive sliders in the sidebar for flexible analysis.

## Features

- **AI-Powered Predictions**: Using a trained machine learning model, CancerIQ provides quick predictions on breast cancer diagnoses.
- **Lab Integration**: Seamlessly connect your cytology lab to the app for automatic data input and instant predictions.
- **Manual Input**: For greater flexibility, you can input measurements manually through the user-friendly sliders in the sidebar.
- **Real-time Analysis**: Get immediate feedback on the likelihood of a breast mass being benign or malignant based on your data.

## Usage

To use the app, visit the following link: [CancerIQ on Streamlit](https://canceriq.streamlit.app/).

### Manual Data Entry
1. Launch the app using the link above.
2. Enter the required measurements by adjusting the sliders in the sidebar.
3. View the AI-generated prediction instantly.

### Lab Integration
1. Connect your cytology lab to the app by linking your lab's data feed.
2. The app will automatically process the incoming data and display the diagnosis.

## Installation

If you'd like to run the app locally:

1. Clone the repository:
    ```bash
    git clone <https://github.com/mahmoudalrefaey/streamlit-cancer-diagnosis/tree/main>
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

## How It Works

CancerIQ utilizes a machine learning model that was trained on breast cancer cytology data to predict whether a mass is benign or malignant. The app processes lab measurements (either manually entered or fed via an integration) to make predictions, providing real-time diagnostic insights.

## Contributing

If you’d like to contribute, please submit a pull request or open an issue for suggestions.

