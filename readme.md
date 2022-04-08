# Amazon A-to-Z Shift Scraper

Automated Web Scrapper for Booking new Shifts as soon as they are available. Initially created for my parents.  

## Setup Steps (Windows)

1. Clone this repository in your desired folder.

   ```bash
   git clone https://github.com/Jay206-Programmer/Amazon-AtoZ-Shift-Scraper.git
   ```

2. Setup Virtual environment. Move inside the cloned repository and enter below commands in the terminal.

    ```bash
    python -m venv .env
    cd .env/Scripts/
    activate
    cd ../..
    pip install -r requirements.txt
    ```

3. Download **[Edge WebDriver](https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp)**, Extract it and add folder path to PATH.

4. Create **Auth.json** file in Scrapper's root directory. Change values with your details.

    ```json
    {
       "atoz-email": "atoz-email-address",
       "atoz-pass": "atoz-password",
       "gmail-id": "gmail-id",
       "gmail-pass": "gmail password"
    }
    ```

5. Run **main.py** file.
