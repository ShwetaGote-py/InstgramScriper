# Instagram Scraper

This project is a Python script that uses the `instaloader` library to scrape profile information from Instagram. The script reads a list of Instagram usernames from an input Excel file, extracts various details about each profile, and saves the data to an output Excel file with a timestamp.

## Description

The script extracts the following information for each Instagram user:
- Username
- Full Name
- Bio
- Follower Count
- Following Count
- Post Count
- Profile Picture URL
- Website
- Account Type (Business or Personal/Creator)
- Verified Status

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/instagram_scraper.git
   cd instagram_scraper
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the necessary permissions to run the script and access Instagram data.

## Usage

1. Prepare an input Excel file with a column named `Username` that contains the Instagram usernames you want to scrape.

2. Run the script with the input file as a command-line argument:
   ```bash
   python instagram_scraper.py <input_file>
   ```

   Replace `<input_file>` with the path to your input Excel file.

3. The script will create an output Excel file with the scraped data. The filename will include a timestamp to avoid overwriting previous files.

## Example

```bash
python instagram_scraper.py usernames.xlsx
```

This command will read the usernames from `usernames.xlsx` and save the scraped profile information to a new Excel file with a name like `instagram_profiles_18_Mar_2025_05_23_13.xlsx`.

## Requirements

- Python 3.x
- `instaloader`
- `pandas`
- `openpyxl`

All required packages can be installed via `pip` using the provided `requirements.txt` file.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- ShwetaGote-py
