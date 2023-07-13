# Automation Suite for Backpack for Laravel Demo Project

This automation suite is developed using Python and Selenium WebDriver, following the Page Object Model (POM) design pattern for organizing the test suite. The suite is designed to test the functionality and responsiveness of the Backpack for Laravel demo project, which can be accessed at [https://demo.backpackforlaravel.com/](https://demo.backpackforlaravel.com/).

## Installation

### Python Installation:
1. Visit the official Python website: [https://www.python.org/downloads](https://www.python.org/downloads)
2. Download the appropriate Python installer for your operating system.
3. Run the installer and follow the on-screen instructions.
4. Verify the installation by opening a terminal/command prompt and running the command `python --version`.

### Selenium Installation:
1. Open a terminal/command prompt.
2. Run the command `pip install selenium` to install Selenium using pip (Python package installer).
3. Selenium will be downloaded and installed along with its dependencies.
4. Verify the installation by running a sample Selenium script or importing the Selenium module in a Python script.

## Getting Started

1. Clone the project repository:

git clone https://github.com/islemfablab/backpack-selenium.git


2. Test the login page:

    python -m Tests.unit_test_login


3. Test the product page:

    python -m Tests.test_product_page


4. Test the responsiveness of the product page:

    python -m Tests.test_product_responsive


5. Test the response time from creating a product:

    python -m Tests.test_product_listener


NB. The generated test reports can be found in the "Report" directory.



