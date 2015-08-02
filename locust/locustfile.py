from locust import HttpLocust, TaskSet, task

username = 'admin'
password = '123456'

class MyTaskSet(TaskSet):
    
    def on_start(self):
        csrftoken = self.client.get('accounts/login').cookies['csrftoken']
        self.client.post("accounts/login/", 
                  {"id_username":username, 
                   'id_password':password}, 
                   headers={"X-CSRFToken": csrftoken})
    
    @task(5)
    def index(self):
        self.client.get("")

    @task(1)
    def addProperty(self):
        self.client.get("addProperty/")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 4000
    max_wait = 10000