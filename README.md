## End to End Machine Learning Project

# Student Performance Predictor

## Overview

This project aims to predict student performance using machine learning techniques. It includes data preprocessing, model training, and evaluation components. The application is built using Python and utilizes libraries such as Pandas, Scikit-learn, and CatBoost.

## Project Structure

The project is structured as follows:

- `.ebextensions/`: Contains configuration files for Elastic Beanstalk deployment.
- `.gitignore`: Specifies intentionally untracked files that Git should ignore.
- `application.py`: The main Flask application file.
- `artifacts/`: Directory for storing artifacts such as model files.
- `catboost_info/`: Directory for CatBoost model information.
- `notebook/`: Contains Jupyter notebooks for experimentation and analysis.
- `requirements.txt`: Lists the Python dependencies required to run the application.
- `setup.py`: Installation script for the project.
- `src/`: Source code directory containing various modules and components.
- `templates/`: Directory for HTML templates used by the Flask application.

### Source Code Structure (`src/`)

- `src/components/`: Contains reusable components.
- `src/exception.py`: Defines custom exception handling.
- `src/logger.py`: Configures logging for the application.
- `src/pipeline/`: Implements the data processing and model training pipeline.
- `src/utils.py`: Provides utility functions.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/askchandan/Student_Performance_Predictor.git
    cd Student_Performance_Predictor
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Flask application:**

    ```bash
    python application.py
    ```

2.  **Access the application in your web browser:**

    Open your browser and navigate to `http://127.0.0.1:5000` (or the appropriate address if the application is running on a different host/port).

## Dependencies

The project relies on the following Python packages:

-   Flask
-   Scikit-learn
-   Pandas
-   CatBoost
-   Other dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License

This project does not have a specified license. Please add a license file to clarify the terms of use.

## Contact

For questions or issues, please open an issue on the GitHub repository.