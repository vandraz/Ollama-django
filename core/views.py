from django.http import HttpResponse
from django.shortcuts import render

def landing_page(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to My Platform</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { text-align: center; background: white; padding: 3rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; font-size: 2.5rem; margin-bottom: 1rem; }
            p { color: #7f8c8d; font-size: 1.2rem; margin-bottom: 2rem; }
            .btn { background-color: #3498db; color: white; padding: 0.8rem 2rem; text-decoration: none; border-radius: 5px; font-weight: bold; transition: background 0.3s; }
            .btn:hover { background-color: #2980b9; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the AI Platform 🦞</h1>
            <p>Built with Django and managed by Claw.</p>
            <a href="#" class="btn">Get Started</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
