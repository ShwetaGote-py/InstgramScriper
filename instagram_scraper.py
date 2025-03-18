import instaloader
import pandas as pd
from datetime import datetime

# Initialize Instaloader
L = instaloader.Instaloader()

# Load usernames from an Excel file
if len(sys.argv) != 2:
    print("Usage: python instagram_scraper.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
df_input = pd.read_excel(input_file)
usernames = df_input['Username'].tolist()

# Define a function to extract profile information
def get_profile_info(username):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Bio": profile.biography,
            "Follower Count": profile.followers,
            "Following Count": profile.followees,
            "Post Count": profile.mediacount,
            "Profile Picture URL": profile.profile_pic_url,
            "Website": profile.external_url,
            "Account Type": "Business" if profile.is_business_account else "Personal/Creator",
            "Verified": profile.is_verified
        }
    except Exception as e:
        print(f"Failed to get profile for {username}: {e}")
        return None

# Extract data for all usernames
profiles_data = []
for username in usernames:
    profile_info = get_profile_info(username)
    if profile_info:
        profiles_data.append(profile_info)

# Create a pandas DataFrame and save it to an Excel file
df = pd.DataFrame(profiles_data)

# Get the current timestamp
timestamp = datetime.now().strftime("%d_%b_%Y_%H_%M_%S")

# Create a filename with the timestamp
output_file = f"instagram_profiles_{timestamp}.xlsx"

# Save the DataFrame to the new file
df.to_excel(output_file, index=False)

print("Data extraction complete. Saved to instagram_profiles.xlsx")