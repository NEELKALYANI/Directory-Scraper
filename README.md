# Directory-Scraper

This Python script automates the process of extracting certified coach listings from **Gallup's directory** using Selenium. It navigates through a dropdown list of countries, selects each one, and retrieves the names, email addresses, and profile image URLs of listed coaches. The extracted data is then saved in an Excel file (scraped_data.xlsx).

**Features:**

* Uses Selenium to interact with the webpage dynamically.
* Extracts coach names, emails, and profile images.
* Iterates through all available countries in the dropdown list.
* Saves the collected data into an Excel file.
* Runs in headless mode for efficiency.
* Uses explicit waits to handle dynamic content loading.

**Requirements:**

* Python 3.x
* Selenium
* WebDriver Manager
* Pandas
* Chrome WebDriver

**How It Works:**

* Opens the Gallup certification directory.
* Extracts the available countries from the dropdown.
* Selects each country and applies the filter.
* Waits for the results to load.
* Extracts coach details: name, email, and profile image.
* Saves the data to an Excel file.
* Closes the browser instance.

**Notes:**

* Ensure Google Chrome is installed on your system.
* The script runs in headless mode by default, meaning it does not open a visible browser window.
* If the website layout changes, the script may require updates to the element locators.
