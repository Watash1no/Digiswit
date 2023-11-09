Steps to run a autotests with selenium and pyton

1. Download a "saucedemo autotest.py" from "Exercise 1B - Selenium" folder
2. Download a latest Chromedriver according to your version of browser (https://googlechromelabs.github.io/chrome-for-testing/) and unpack it
3. Download an install pyton (https://www.python.org/downloads/)
4. Install any IDE you like (example based on https://www.jetbrains.com/pycharm/)
5. Install Selenium webdriver
   
     5.1 Open your console/terminal app
   
     5.2 Write and run "pip install -U selenium"

     5.3 Wait untill install

 6. Open your IDE
 7. Create a project
 8. Open project
 9. Open settings
 10. Select your project and go to Python Interpreter
 11. With + button search for Selenium add it and close tab
 12. In IDE go to File - Open - saucedemo autotest.py
 13. Change path in (os.environ['PATH'] += r"/usr/local/bin") to directory where your chromedriver is (lines 10, 23, 47, 72)
 14. Click on play button to run a test
 15. In the lower part of the screen in tab "Run" observe test run results
