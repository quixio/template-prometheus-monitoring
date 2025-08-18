from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

PUSHGATEWAY_URL = os.getenv("PUSHGATEWAY_URL")
PUSHGATEWAY_PROXY_PW = os.getenv("PUSHGATEWAY_PROXY_PASSWORD")

# Authenticate requests
def authenticate(req):
    auth = req.authorization
    return auth and auth.username == 'admin' and auth.password == PUSHGATEWAY_PROXY_PW

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    if not authenticate(request):
        return Response('Authentication required', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    # Forward request to Pushgateway
    resp = requests.request(
        method=request.method,
        url=f"{PUSHGATEWAY_URL}/{path}",
        headers={key: value for key, value in request.headers if key.lower() != 'host'},
        data=request.get_data(),
        params=request.args,
        allow_redirects=False,
    )

    # Send response back to client
    excluded_headers = ['content-encoding', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)