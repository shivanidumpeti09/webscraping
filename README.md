# LinkedIn Web Scraping Project

This project uses Python with Flask, Selenium, and other libraries to perform web scraping on LinkedIn.

## Prerequisites

Before running this project, ensure you have the following installed:

-   Python 3.x
-   pip (Python package installer)
-   Google Chrome (or another browser, with the appropriate driver)

## Setup

1.  **Create Project Directory:**

    \* Open your terminal and create a new directory for your project in VS Code. [cite: 1]

2.  **Create Virtual Environment:**

    \* In the terminal, navigate to your project directory and run the following command to create a virtual environment:

        ```bash
        python -m venv venv
        ```

3.  **Activate Virtual Environment:**

    \* Activate the virtual environment using the following command:

        \* On Windows:

            ```bash
            venv\Scripts\activate
            ```

        \* On macOS and Linux:

            ```bash
            source venv/bin/activate
            ```

4.  **Install Dependencies:**

    \* Install the required Python packages using pip:

        ```bash
        pip install Flask Flask-WTF linkedin_scraper email_validator
        ```

        \* This will install Flask, Flask-WTF, linkedin\_scraper, and email\_validator.

5.  **Create Python Files:**

    \* Create two Python files in your project directory: `app.py` and `forms.py`.
    \* Copy and paste your Python code into these files.

6.  **Create Templates Directory:**

    \* Create a directory named `templates` in your project directory.
    \* Copy your HTML files into the `templates` directory.

## Running the Application

To run the Flask application, use the following command in your terminal:

```bash
python app.py
