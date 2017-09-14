#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By as identifier
from selenium.webdriver.support.ui import WebDriverWait as driver_wait
from selenium.webdriver.support import expected_conditions as conditions

def main():
    global page

    page = webdriver.Chrome()
    page.get("https://www.papajohns.com/order/stores-near-me")
    
    if ORDER['delivery method'] == 'carryout':
        fill_address_carryout()
    elif ORDER['delivery method'] == 'delivery':
        fill_address_delivery()

def scrape_locations():
    
    e_store_summary = driver_wait(page, 2).until(
            conditions.presence_of_element_located(
                (identifier.ID, 'store-summary-accord-id')))
    e_view_more = page.find_element_by_class_name('view-more-stores')
    e_view_more.click()
    e_stores = e_store_summary.find_elements_by_class_name('store-location')

    for each in e_stores:
        print(each.text[0])

def fill_address_carryout():
    e_form = page.find_element_by_id('carryout-form')
    e_form.click()
    e_zip = e_form.find_element_by_id('locations-zipPostalcode')
    e_zip.send_keys(ADDRESS['postal'])
    e_submit = e_form.find_element_by_class_name('button-desk')
    e_submit = e_submit.find_element_by_class_name('button')
    e_submit.click()
    scrape_locations()


def fill_address_delivery():
    e_form = page.find_element_by_id('delivery-form')
    
    e_country = e_form.find_element_by_id('locations-country')
    if ADDRESS['country'] == 'USA':
        e_country.send_keys('USA')
        e_zip = e_form.find_element_by_id('locations-usa-zipcode')
        e_zip.send_keys(ADDRESS['postal'])
    elif ADDRESS['country'] == 'Canada':
        e_country.send_keys('Canada')
        e_postal = e_form.find_element_by_id('locations-postalcode')
        e_postal.send_keys(ADDRESS['postal'])
    else:
        raise ValueError('delivery not possible outside of the USA and Canada')
    
    e_address = e_form.find_element_by_id('locations-streetaddress')
    e_address.send_keys(ADDRESS['first_line'])

    try:
        assert ADDRESS['second_line']
        e_apt_menu = e_form.find_element_by_id('locations-aptstefloor')
        e_apt_menu.send_keys('Apt')
        e_apt_num = e_form.find_element_by_id('locations-aptstefloornumber')
        e_apt_num.send_keys(ADDRESS['second_line'])
    except KeyError:
        pass

    e_submit = e_form.find_element_by_class_name('button-set')
    e_submit = e_submit.find_element_by_class_name('button')
    e_submit.click()

ORDER = {'items': [{'name': 'cheese pizza',
                    'size': 'medium',
                    'options': ['crust_thin',
                                'half1_pineapple',
                                'half1_ham',
                                'half2_pepperoni']},

                   {'name': 'pepperoni pizza',
                    'size': 'large',
                    'options': ['crust_original']},

                   {'name': 'diet coke',
                    'size': '2-liter'}],

         'delivery method': 'delivery',
         'payment method': 'credit'}

ADDRESS = {'first_line': '12336 Golden Knight Circle',
           'second_line': '29-105',
           'city': 'Orlando',
           'state/province': 'Florida',
           'country': 'USA',
           'postal': '32817'}

main()
