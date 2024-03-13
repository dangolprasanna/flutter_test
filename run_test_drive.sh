#!/bin/sh

# Start ChromeDriver in the background
/app/chromedriver --whitelisted-ips --port=4444 &
CHROMEDRIVER_PID=$!

# Wait for a moment to ensure ChromeDriver has started
sleep 5
flutter --version
# Run Flutter commands
flutter doctor
flutter pub get
flutter analyze 2>&1 | tee analyzer_log.txt
sleep 10
python3 generateNewReport.py
# Check if analyzer_log.txt contains any issues
if grep -q "issues found" analyzer_log.txt; then
  echo "Issues found. Stopping the process."
  # Kill the ChromeDriver process
  kill $CHROMEDRIVER_PID
  exit 1
else
  echo "No issues found. Continuing the process."
fi

# Output versions of Chrome and ChromeDriver
google-chrome --version
/app/chromedriver --version

# Export path to ChromeDriver executable as an environment variable
export CHROMEDRIVER_BINARY=/app/chromedriver

flutter drive --release --driver=test_driver/integration_test.dart --target=integration_test/app_test.dart -d web-server

# Kill the ChromeDriver process
kill $CHROMEDRIVER_PID
