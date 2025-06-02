# 10 advanced_python_programs.py

# 1. Multithreaded Web Scraper
def multithreaded_scraper():
    import threading
    import requests
    from bs4 import BeautifulSoup

    urls = ["https://example.com", "https://example.org", "https://example.net"]

    def fetch(url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        print(f"{url}: {soup.title.string}")

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# 2. Socket Chat App (Client/Server split required)
def run_chat_app_server():
    import socket, threading
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    clients = []

    def handle(client):
        while True:
            try:
                msg = client.recv(1024)
                broadcast(msg, client)
            except:
                clients.remove(client)
                client.close()
                break

    def broadcast(msg, sender):
        for client in clients:
            if client != sender:
                client.send(msg)

    print("Server running on port 12345...")
    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f"Connected with {addr}")
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# 3. Decorator Access Control
def access_control():
    def require_login(func):
        def wrapper(user, *args, **kwargs):
            if not user.get("is_logged_in"):
                raise PermissionError("Login required")
            return func(user, *args, **kwargs)
        return wrapper

    @require_login
    def view_profile(user):
        return f"Profile of {user['name']}"

    user = {"name": "Ram", "is_logged_in": True}
    print(view_profile(user))

# 4. Custom Context Manager
def custom_context_manager():
    class FileManager:
        def __init__(self, filename, mode):
            self.file = open(filename, mode)
        def __enter__(self):
            return self.file
        def __exit__(self, exc_type, exc_value, traceback):
            self.file.close()

    with FileManager("test.txt", "w") as f:
        f.write("Hello from context manager!")

# 5. LRU Cache
def lru_cache_demo():
    from collections import OrderedDict

    class LRUCache:
        def __init__(self, capacity):
            self.cache = OrderedDict()
            self.capacity = capacity

        def get(self, key):
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            return -1

        def put(self, key, value):
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))

# 6. Data Analysis Pipeline
def data_analysis():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.DataFrame({'Age': [22, 25, 47, 52, 46], 'Income': [50000, 54000, 120000, 110000, 105000]})
    print(df.describe())
    df['Age'].hist()
    plt.show()

# 7. Flask REST API
def flask_api():
    from flask import Flask, jsonify, request

    app = Flask(__name__)

    @app.route('/greet', methods=['POST'])
    def greet():
        data = request.json
        return jsonify(message=f"Hello, {data['name']}!")

    app.run(debug=True)

# 8. Singleton with Metaclass
def singleton_metaclass():
    class Singleton(type):
        _instances = {}
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]

    class DBConnection(metaclass=Singleton):
        pass

    a = DBConnection()
    b = DBConnection()
    print(a is b)

# 9. Asynchronous API Calls
def async_api_calls():
    import aiohttp
    import asyncio

    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()

    async def main():
        async with aiohttp.ClientSession() as session:
            html = await fetch(session, 'https://example.com')
            print(html[:100])

    asyncio.run(main())

# 10. Binary Tree Traversal
def binary_tree_traversal():
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=" ")
            inorder(node.right)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    inorder(root)

# -------------------------------
# MAIN MENU TO DEMO FUNCTIONS
# -------------------------------
if __name__ == "__main__":
    print("Choose a program to run:")
    print("1. Multithreaded Web Scraper")
    print("2. Chat Server")
    print("3. Access Control Decorator")
    print("4. Custom Context Manager")
    print("5. LRU Cache")
    print("6. Data Analysis")
    print("7. Flask API")
    print("8. Singleton Pattern")
    print("9. Async API Calls")
    print("10. Binary Tree Traversal")

    choice = input("Enter 1-10: ")

    if choice == '1':
        multithreaded_scraper()
    elif choice == '2':
        run_chat_app_server()
    elif choice == '3':
        access_control()
    elif choice == '4':
        custom_context_manager()
    elif choice == '5':
        lru_cache_demo()
    elif choice == '6':
        data_analysis()
    elif choice == '7':
        flask_api()
    elif choice == '8':
        singleton_metaclass()
    elif choice == '9':
        async_api_calls()
    elif choice == '10':
        binary_tree_traversal()
    else:
        print("Invalid choice")
