from injury.py import getHTML

def handler(namefirst):
    for key in getHTML():
        if key == namefirst:
            return self.html[key]
