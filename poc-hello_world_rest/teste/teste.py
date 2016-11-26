from web

urls = (
    '/', 'index'
)

class index:
        
    def GET(self):
        return 'Hello World!'

if __name__ == '__main__':
    app = web.aplication(urls, globals())
    app.run()