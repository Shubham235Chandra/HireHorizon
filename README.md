# HireHorizon

HireHorizon is a web application designed to enhance your resume by comparing it with job descriptions. The app uses advanced generative AI to analyze your resume against a job description and provides feedback to help you improve your resume's alignment with the job requirements.

## Features

- Upload your resume in PDF or DOCX format
- Paste a job description for comparison
- Receive a percentage match score between your resume and the job description
- Identify missing keywords in your resume
- Get a profile summary to enhance your resume

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- PyPDF2
- google.generativeai
- python-dotenv
- python-docx
- docx2pdf

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/HireHorizon.git
    cd HireHorizon
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    - Create a `.env` file in the root directory of the project.
    - Add your Google API key to the `.env` file:
      ```plaintext
      GOOGLE_API_KEY=your_google_api_key
      ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the sidebar to upload your resume and paste the job description.

4. Click the "Submit" button to receive your resume analysis.

## File Structure

- `app.py`: The main Streamlit application script.
- `requirements.txt`: A list of the required Python packages.
- `README.md`: This readme file.

## Example

Here is a step-by-step example of how to use HireHorizon:

1. Open the app in your web browser.
2. Paste the job description in the provided text area.
3. Upload your resume in PDF or DOCX format.
4. Click "Submit".
5. View the analysis results, including the profile summary, match percentage, and missing keywords.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- The project uses [Streamlit](https://streamlit.io/) for the web interface.
- Thanks to [google.generativeai](https://pypi.org/project/google.generativeai/) for the AI functionalities.

## Website

You can also access HireHorizon online at [HireHorizon on Hugging Face](https://huggingface.co/spaces/Shubham235/hire_horizon).
