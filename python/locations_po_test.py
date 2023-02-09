from locations_main_po import LocationsMainPage

def test_create(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form("Work", "2,2")
    page.click_on_create_location_button()

    assert page.get_text_on_message_panel() == "Location has been created"


def test_create_with_default_data(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form()
    page.click_on_create_location_button()

    assert page.get_text_on_message_panel() == "Location has been created"


def test_empty_name(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form("")
    page.click_on_create_location_button()

    assert page.get_error_message() == "Can not be empty name!"

def test_empty_coords(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form(coords="")
    page.click_on_create_location_button()        
    assert page.get_error_message() == "Invalid format!"

def test_big_data(driver):
    page = LocationsMainPage(driver)
    page.open()

    with open("MOCK_DATA.csv", encoding="utf-8") as f:
        for line in f:
            (name, lat, lon) = line.strip().split(",")
            page.click_create_location_link()
            page.fill_form(name, lat + "," + lon)
            page.click_on_create_location_button()
