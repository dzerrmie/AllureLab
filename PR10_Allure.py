import requests
import pytest
import json
import allure

@allure.title("Test user api.")
@allure.description("Those test make requests and test the users api.")
@allure.tag("AllurePython", "EPIC", "wow")


#CREATE_USER
class Steps_CREATE():
    
    @allure.step("Check request code from request.")
    def step1(self, r):
        assert r.status_code == requests.codes.created
    
    @allure.step("Check response types after request.")
    def step2(self, r):
        assert r.headers.get('content-type') == 'application/json; charset=utf-8'
    
    @allure.step("Check object for some data.")
    def step3(self, r_dict):
        assert 'name' in r_dict
        assert 'job' in r_dict
        assert 'id' in r_dict
        assert 'createdAt' in r_dict


#DELETE_USER
class Steps_DELETE():
    @allure.step("Check request code from request.")
    def step1(self, r):
        assert r.status_code == requests.codes.no_content


#SINGLE_USER
class Steps_SINGLE():
    @allure.step("Check request code from request.")
    def step1(self, r):
        assert r.status_code == requests.codes.ok
    
    @allure.step("Check response types after request.")
    def step2(self, r):
        assert r.headers.get('content-type') == 'application/json; charset=utf-8'
    
    @allure.step("Check object for some data.")
    def step3(self, r_dict):
        assert 'data' in r_dict
        assert 'support' in r_dict
        
        assert 'id' in r_dict['data']
        assert 'email' in r_dict['data']
        assert 'first_name' in r_dict['data']
        assert 'last_name' in r_dict['data']
        assert 'avatar' in r_dict['data']
        
        assert 'url' in r_dict['support']
        assert 'text' in r_dict['support']


#SINGLE_UPDATE
class Steps_UPDATE():
    @allure.step("Check request code from request.")
    def step1(self, r):
        assert r.status_code == requests.codes.ok
    
    @allure.step("Check response types after request.")
    def step2(self, r):
        assert r.headers.get('content-type') == 'application/json; charset=utf-8'
    
    @allure.step("Check object for some data.")
    def step3(self, r_dict):
        assert 'name' in r_dict
        assert 'job' in r_dict
        assert 'updatedAt' in r_dict

def test_user_create():
    url = "https://reqres.in/api/users/2"
    r = requests.post(url, data={'name': 'Alexander','job': 'internetTroll'})
    r_dict = r.json()
    
    steps = Steps_CREATE()
    steps.step1(r)
    steps.step2(r)
    steps.step3(r_dict)

def test_user_delete():
    url = "https://reqres.in/api/users/2"
    r = requests.delete(url)
    
    steps = Steps_DELETE()
    steps.step1(r)
    
def test_user_single():
    url = "https://reqres.in/api/users/2"
    r = requests.get(url)
    r_dict = r.json()
    
    steps = Steps_SINGLE()
    steps.step1(r)
    steps.step2(r)
    steps.step3(r_dict)
    
def test_user_update():
    url = "https://reqres.in/api/users/2"
    r = requests.put(url, data={'name': 'Alexander', 'job': 'internetTroll'})
    r_dict = r.json()
    
    steps = Steps_UPDATE()
    steps.step1(r)
    steps.step2(r)
    steps.step3(r_dict)
    