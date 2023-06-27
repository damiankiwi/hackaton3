# Test Automation Framework

This repository contains a test automation framework for web applications using Python and Selenium.

## Table of Contents

- [General Info](#general-info)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Project Status](#project-status)
- [Room for Improvement](#room-for-improvement)
- [Contact](#contact)

## General Information

The test automation framework utilizes Python and Selenium to automate the testing of web applications. It includes the following components:

- **Configuration**: The framework allows for easy configuration of test environment settings.

- **Chrome Driver**: It provides the necessary setup for running tests on Google Chrome browser.

- **Test Cases**: The framework includes test cases that cover various scenarios, such as performance loading speed, browser functionality, and HTTP statuses.

- **Test Reporting**: The framework generates HTML reports for test execution results.

## Technologies Used

The test automation framework is created using the following technologies:

- Python 3.11.3
- Selenium
- ChromeDriver
- pytest
- requests

## Features

List of features in the test automation framework:

- Performance loading speed test for a web page.
- Test for browser functionality and interaction with elements on a web page.
- Test to check the HTTP statuses of specific URLs.

## Setup

To set up the test automation framework, follow these steps:

1. Install Python 3.11.3 on your machine.
2. Install the required Python packages: `requests`, `selenium`, `pytest`, `pytest-testrail`, and `webdriver_manager`.
3. Download the ChromeDriver executable and configure the path in the framework's code.
4. Update the configuration settings for TestRail (URL, user credentials, project ID, suite ID) if applicable.

## Usage

To use the test automation framework, follow these steps:

1. Run the desired test script by executing the Python file.
2. The test will run, and the results will be displayed in the console.
3. HTML test reports will be generated, providing detailed information about the test execution.

## Project Status

The test automation framework is currently complete and can be used for testing web applications.

## Room for Improvement

Areas for improvement and future development:

- Enhance test coverage by adding more test cases for different scenarios.
- Implement support for other browsers besides Google Chrome.
- Add support for other testing frameworks and tools.
- Integrate with a continuous integration system for automated test execution.

## Contact

- GitHub: damiankiwi