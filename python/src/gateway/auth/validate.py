import os, requests

def token(request):
    encoded_jwt = request.headers["Authorization"]
    if not encoded_jwt:
        return None, ("missing credentials", 401)
    # encoded_jwt = encoded_jwt.split(" ")[1]
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}" + "/validate",
        headers={"Authorization": encoded_jwt}
    )
    print("helo from token")
    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)