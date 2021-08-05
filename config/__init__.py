
from .settings import ENV


class PytestConfig:
    """
    Pytest 运行参数配置
    """
    # -v  Verbose mode. Prints the full name of each test run.
    verbose_mode = False

    # -q  # Quiet mode. Print fewer details in the console output when running tests.
    quiet_mode = False

    # -x  # Stop running the tests after the first failure is reached.
    stop_running = False

    # --html=report.html  # Creates a detailed pytest-html report after tests finish.
    create_html_report = False

    # --collect-only | --co  # Show what tests would get run. (Without running them)
    show_case = False

    # -n=NUM  # Multi thread the tests using that many threads. (Speed up test runs!)
    multi_thread = None

    # -s  # See print statements. (Should be on by default with pytest.ini present.)
    print_statements = False

    # --junit-xml=report.xml  # Creates a junit-xml report after tests finish.
    create_junit_xml = False

    # --pdb  # If a test fails, pause run and enter debug mode. (Don't use with CI!)
    pause_run = False

    # -m=MARKER  # Run tests with the specified pytest marker.
    specified_marker = False

    # rerun failures, Number of retries failed to run
    rerun_failures_num = 0
