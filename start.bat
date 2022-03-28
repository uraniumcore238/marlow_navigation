cd /d D:\Programming\marlow_navigation\tests
py.test --browser_name chrome -v -s test_verify_price_in_cart.py --alluredir D:\Programming\marlow_navigation\Reports
cd D:\Programming\marlow_navigation\HTMLReports
allure generate D:\Programming\marlow_navigation\Reports -c