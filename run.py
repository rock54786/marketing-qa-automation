import os
from seleniumbase import create_dir

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

"""
Here are some useful command-line options that come with pytest:

    -v  # Verbose mode. Prints the full name of each test run.
    -q  # Quiet mode. Print fewer details in the console output when running tests.
    -x  # Stop running the tests after the first failure is reached.
    --html=report.html  # Creates a detailed pytest-html report after tests finish.
    --collect-only | --co  # Show what tests would get run. (Without running them)
    -n=NUM  # Multithread the tests using that many threads. (Speed up test runs!)
    -s  # See print statements. (Should be on by default with pytest.ini present.)
    --junit-xml=report.xml  # Creates a junit-xml report after tests finish.
    --pdb  # If a test fails, pause run and enter debug mode. (Don't use with CI!)
    -m=MARKER  # Run tests with the specified pytest marker.


SeleniumBase provides additional pytest command-line options for tests:
    --browser=BROWSER  # (The web browser to use. Default: "chrome".)
    --chrome  # (Shortcut for "--browser=chrome". On by default.)
    --edge  # (Shortcut for "--browser=edge".)
    --firefox  # (Shortcut for "--browser=firefox".)
    --ie  # (Shortcut for "--browser=ie".)
    --opera  # (Shortcut for "--browser=opera".)
    --safari  # (Shortcut for "--browser=safari".)
    --cap-file=FILE  # (The web browser's desired capabilities to use.)
    --cap-string=STRING  # (The web browser's desired capabilities to use.)
    --settings-file=FILE  # (Override default SeleniumBase settings.)
    --env=ENV  # (Set a test environment. Use "self.env" to use this in tests.)
    --data=DATA  # (Extra test data. Access with "self.data" in tests.)
    --var1=DATA  # (Extra test data. Access with "self.var1" in tests.)
    --var2=DATA  # (Extra test data. Access with "self.var2" in tests.)
    --var3=DATA  # (Extra test data. Access with "self.var3" in tests.)
    --user-data-dir=DIR  # (Set the Chrome user data directory to use.)
    --protocol=PROTOCOL  # (The Selenium Grid protocol: http|https.)
    --server=SERVER  # (The Selenium Grid server/IP used for tests.)
    --port=PORT  # (The Selenium Grid port used by the test server.)
    --proxy=SERVER:PORT  # (Connect to a proxy server:port for tests.)
    --proxy=USERNAME:PASSWORD@SERVER:PORT  # (Use authenticated proxy server.)
    --agent=STRING  # (Modify the web browser's User-Agent string.)
    --mobile  # (Use the mobile device emulator while running tests.)
    --metrics=STRING  # (Set mobile metrics: "CSSWidth,CSSHeight,PixelRatio".)
    --chromium-arg=ARG  # (Add a Chromium arg for Chrome/Edge, comma-separated.)
    --firefox-arg=ARG  # (Add a Firefox arg for Firefox, comma-separated.)
    --firefox-pref=SET  # (Set a Firefox preference:value set, comma-separated.)
    --extension-zip=ZIP  # (Load a Chrome Extension .zip|.crx, comma-separated.)
    --extension-dir=DIR  # (Load a Chrome Extension directory, comma-separated.)
    --headless  # (Run tests headlessly. Default mode on Linux OS.)
    --headed  # (Run tests with a GUI on Linux OS.)
    --locale=LOCALE_CODE  # (Set the Language Locale Code for the web browser.)
    --interval=SECONDS  # (The autoplay interval for presentations & tour steps)
    --start-pages=URL  # (The starting URL for the web browser when tests begin.)
    --archive-logs  #  (Archive existing log files instead of deleting them.)
    --archive-downloads  #  (Archive old downloads instead of deleting them.)
    --time-limit=SECONDS  # (Safely fail any test that exceeds the time limit.)
    --slow  # (Slow down the automation. Faster than using Demo Mode.)
    --demo  # (Slow down and visually see test actions as they occur.)
    --demo-sleep=SECONDS  # (Set the wait time after Demo Mode actions.)
    --highlights=NUM  # (Number of highlight animations for Demo Mode actions.)
    --message-duration=SECONDS  # (The time length for Messenger alerts.)
    --check-js  # (Check for JavaScript errors after pages loads.)
    --ad-block  # (Block some types of display ads after pages loads.)
    --block-images  # (Block images from loading during tests.)
    --verify-delay=SECONDS  # (The delay before MasterQA verification checks.)
    --disable-csp  # (Disable the Content Security Policy of websites.)
    --disable-ws  # (Disable Web Security on Chromium-based browsers.)
    --enable-ws  # (Enable Web Security on Chromium-based browsers.)
    --enable-sync  # (Enable "Chrome Sync".)
    --use-auto-ext  # (Use Chrome's automation extension.)
    --remote-debug  # (Enable Chrome's Remote Debugger on http://localhost:9222)
    --dashboard  # (Enable the SeleniumBase Dashboard. Saved at: dashboard.html)
    --swiftshader  # (Use Chrome's "--use-gl=swiftshader" feature.)
    --incognito  #  (Enable Chrome's Incognito mode.)
    --guest  # (Enable Chrome's Guest mode.)
    --devtools  # (Open Chrome's DevTools when the browser opens.)
    --reuse-session | --rs  # (Reuse browser session between tests.)
    --crumbs  # (Delete all cookies between tests reusing a session.)
    --maximize-window  # (Start tests with the web browser window maximized.)
    --save-screenshot  # (Save a screenshot at the end of each test.)
    --visual-baseline  # (Set the visual baseline for Visual/Layout tests.)
    --timeout-multiplier=MULTIPLIER  # (Multiplies the default timeout values.)

"""


def main():
    """

    :return:
    """
    if os.path.isdir(BASE_DIR) is False:
        os.mkdir(BASE_DIR)
    base = os.path.join(str(BASE_DIR), 'result')
    if os.path.isdir(base) is False:
        os.mkdir(base)
    result_dir, report_name = create_dir.web_report_dir(base)
    pytest_command = 'pytest -s -v tests/test_home.py --alluredir=' + result_dir

    os.system(pytest_command)
    report_dir = os.path.join(BASE_DIR, "report", report_name)
    os.system("allure generate {result_dir} -o {report_dir}".format(result_dir=result_dir, report_dir=report_dir))


if __name__ == '__main__':
    main()
