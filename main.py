"""Instagram Follower Bot

This script follows users from a specified Instagram account.
The purpose is to follow users that follow similar accounts to the
user's, with the goal of obtaining more followers for the user's own account.
It is assumed that the user has an instagram account.

This script requires that 'python_dotenv', 'selenium' be installed within the Python
environment you are running this script in. The user also requires a WebDriver.

"""

from instafollower import InstaFollower

CHROME_EXECUTABLE_PATH = 'C:\\Development\\chromedriver.exe'

bot = InstaFollower(CHROME_EXECUTABLE_PATH)
bot.login()
bot.find_followers()
