from wsgiref.simple_server import make_server
from app import application


if __name__ == "__main__":
    print("Serving on port 8000...")
    # Respond to requests
    make_server("localhost", 8000, application).serve_forever()
