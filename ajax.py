class GET:
    def __init__(self,url):
        self.url = url
        self.success = lambda data: print(data)
        self.fail = lambda status: print('Request failed.  Returned status of ' + status)
        self.data = False

    def run(self):
        data = self.data
        if data:
            self.url += "?"
            for key,value in data.items():
                self.url += "{}={}&".format( encodeURIComponent(key),encodeURIComponent(value) )
        xhr = __new__ (XMLHttpRequest())
        xhr.open('GET',self.url)
        xhr.onload = lambda : self.success(xhr.responseText) if xhr.status == 200 else self.fail(xhr.status)
        xhr.send();
