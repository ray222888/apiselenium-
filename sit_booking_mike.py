# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import time
import csv
import pandas as pd
import datetime
import requests
from selenium import  webdriver
from time import sleep

def print_hi(name):
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWTU40U09mNGRXQzRhZ1dMYk9ta0FRR0ZPcmpETzBHcms2TjhVal9ScnhjIn0.eyJleHAiOjE2MDgwODYxMjQsImlhdCI6MTYwODA4NTUyNCwianRpIjoiNThmZTU5NjMtMDg2Yi00NmQwLTljYmYtNTc2YjVmZTBkODEyIiwiaXNzIjoiaHR0cHM6Ly91YXQuY29ubmVjdGF0Y2hhbmdpLmNvbS9rZXljbG9hay9yZWFsbXMvdWF0IiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImVlNWNmZjFkLWYwZmQtNDJjMy05MDA2LWY1NzcwZTk2NWI4YiIsInR5cCI6IkJlYXJlciIsImF6cCI6InRtc2stY2FzZy1tYWdpYy1saW5rIiwic2Vzc2lvbl9zdGF0ZSI6ImIyODM0MzJmLWEwYjQtNDVlOS1hZTkzLWJmNzdiZDU5MDhlOCIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZ2VuZGVyIjoiQ2ZESjhQXzNyZWo0NHJWS25LZ2FrOFBQWS1fcXY4UGIzOTY1cUNFLVhXdHBJZ1hxRURuMUk5ZUhxTktHcThUanpPdEVjUlMwdll6dFJ4YjF4WkRwb1YyeFp4UndQMktKV3Zua2hVeElKejY5bmhMcHp0eGVTSDVncnJvNVFrdnJZYmNtSnciLCJuYW1lIjoiTGlzYSBTaGVuZyIsInByZWZlcnJlZF91c2VybmFtZSI6Imxpc2Ffc2hlbmdAZXBhbS5jb20iLCJnaXZlbl9uYW1lIjoiTGlzYSIsImZhbWlseV9uYW1lIjoiU2hlbmciLCJlbWFpbCI6Imxpc2Ffc2hlbmdAZXBhbS5jb20ifQ.Bp-j31aURN5caz0B_M-A_NCQ1idATFNJlawgBKwH07M0MLwtv55-DgVDdjC3MhR7UEJDBdpgfw--ZMKVvQbeEnuH5wHD6Y9Q8LNgG6VkDRcV_y8VUX8IccduffXAL3hrfRxaoTZpGaM840NIVIHB70lPJlUUYRsUN-JRtMH_nC2Jy7XTfaSDQLFFuBZx_BJzWi1DYdRpv7HOgSfPRCW5IhkXJQkCb8JNY_X-Rqjlv1ioBGaj0XGloKiCK3yXdIDqO-4dZbN4BBIRC9r7gVqybEGZyl4p_nI7gKmJVM-QZQQX7-4pG4-mpivgzyxfYMdqrvojxV1Tq3pCcvsgKX0W0Q',
        'Content-Type':'application/json',
        'User-Agent':'PostmanRuntime/7.26.3',
        'Connection': 'keep-alive',
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br'}

    datatest ={
         'room_id': 3,
         'rate_type_id': 'STAY5',
         'check_in_time': '2021-01-16T03:00:00Z',
         'check_out_time': '2021-01-29T03:00:00Z',
         'arriving_from': 'Australia',
         'number_of_guest': 1,
         'primary_guest_first_name': 'mike',
         'primary_guest_last_name': 'chen',
         'primary_guest_email': 'testpepam@163.com',
         "guests": [
            {
                "salutation_id": "1",
                "first_name": "mike",
                "last_name": "chen",
                "date_of_birth": "1990-02-01T02:18:17.364Z",
                "gender": "Male",
                "nationality": "1",
                "country_of_residence": "AF",
                "passport_number": "A123456789",
                "mobile_phone_code": "86",
                "mobile_number": "13923715041",
                "email": "testpepam@163.com",
                "emergency_contact": {
                    "first_name": "Paul",
                    "last_name": "Gu",
                    "mobile_phone_code": "86",
                    "mobile_number": "13724463321"
                },
                "passport_file_name": "flzuwcoz_1610245127.pdf",
                "passport_expiry_date": "2030-02-01T02:18:38.302Z",
                "nric_fin_number": ""
            }
        ],
        "sg_contact_point": {
            "first_name": "Willam",
            "last_name": "wang",
            "mobile_phone_code": "65",
            "mobile_number": "13855215457"
        },
        "additional_remarks": "test",
        "visit_detail": {
            "purpose_of_visit_id": 1,
            "business_industry_id": 1,
            "your_company": "EPAM",
            "engagement_industry_id": 0,
            "company_of_engagement": "",
            "is_there_sponsorship_invitation_letter": False,
            "sponsor_id": 0,
            "business_person_number_type_id": 2,
            "required_service_ids": [
                1,
                2
            ],
            "letter_file_name": ""
        },
        "agree_policy": True
    }


    urli = 'https://sit.connectatchangi.com'
    apiurl='/api/Booking/'
    apiurlcommit = '/api/Booking/commit/'
    urltest =urli+apiurl
    committest = urli + apiurlcommit
    print(urltest)
    responsett = requests.post(url=urltest, headers=headers, json=datatest)
    print(responsett.text)
    token = responsett.json()["data"]
    print(token)

    transaction_id=token['transaction_id']
    payment_url=token['payment_url']
    reservation_id=token['reservation_id']
    print(transaction_id)
    print(payment_url)
    print(reservation_id)
    d = webdriver.Chrome()
    d.get(payment_url)
    d.implicitly_wait(10)
    #d.find_element_by_xpath("//a[@class='list-group-item']").click()
    d.find_element_by_id('card-name').send_keys('test')
    d.find_element_by_id('cc-no').send_keys('4111111111111111')
    d.find_element_by_id('cc-ccv').send_keys('123')
#    d.find_element_by_id('cc-mail').send_keys('ray_liao@epam.com')
    el=d.find_element_by_id('exp-month')
    for option in el.find_elements_by_tag_name('option'):
        if option.text == '8':
            option.click()
            break
    ey=d.find_element_by_id('exp-year')
    for option in ey.find_elements_by_tag_name('option'):
        if option.text == '2021':
            option.click()
            break
    d.find_element_by_id('cc-combine-pay').click()
    sleep(3)
    d.quit()

    commitdata ={
  "reservation_id": "44273191-6b30-47d5-7317-08d8a678eeab",
  "transaction_id": "AS10001C00007139",
}
    commitdata['transaction_id']= transaction_id
    commitdata['reservation_id'] = reservation_id
    print(commitdata['transaction_id'])
    print(committest)
    responsettcommit = requests.post(url=committest, headers=headers, json=commitdata)
    print(responsettcommit.text)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
