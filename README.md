# transcrypt-ajax
ajax in transcrypt without jquery.

This is a work in progress, right now only GET requests are supported. POST is coming soon.

USAGE:

```python
import ajax

def recvd(data):
    alert(data)

def fetch_remote_resource():
    request = ajax.GET('data.json')
    request.data = { 'foo':1, 'bar':2 }
    request.success = lambda data: recvd(data)
    request.run()
```
