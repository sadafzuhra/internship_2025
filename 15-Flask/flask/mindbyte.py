from flask import Flask

#WSGI
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Mindbyte,it's a home page."

@app.route('/about')
def about():
    return "<html><body><h1>Feed your mind, one byte at a time.<h1><body><html>"

@app.route('/index')
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Mindbyte</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    body {
      margin: 0;
      font-family: 'Inter', sans-serif;
      background-color: #f9f9f9;
      color: #333;
    }
    header {
      background-color: #4f46e5;
      color: white;
      padding: 1.5rem 2rem;
      text-align: center;
    }
    .hero {
      text-align: center;
      padding: 4rem 2rem;
      background-color: #eef2ff;
    }
    .hero h1 {
      font-size: 3rem;
      margin-bottom: 1rem;
    }
    .hero p {
      font-size: 1.25rem;
      max-width: 600px;
      margin: 0 auto;
    }
    .features {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      padding: 3rem 2rem;
    }
    .feature {
      background: white;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }
    .feature h3 {
      color: #4f46e5;
    }
    footer {
      text-align: center;
      padding: 1.5rem;
      background: #f1f1f1;
      font-size: 0.9rem;
    }
  </style>
</head>
<body>

  <header>
    <h1>Mindbyte</h1>
    <p>Feed your mind, one byte at a time.</p>
  </header>

  <section class="hero">
    <h1>Microlearning Made Simple</h1>
    <p>Mindbyte helps you learn faster with bite-sized lessons you can absorb anytime, anywhere. Perfect for students, professionals, and curious minds.</p>
  </section>

  <section class="features">
    <div class="feature">
      <h3>⚡ Quick Lessons</h3>
      <p>Each topic is distilled into a concise format so you learn the essentials in minutes.</p>
    </div>
    <div class="feature">
      <h3>🎯 Smart Goals</h3>
      <p>Set daily goals and track your learning progress with ease.</p>
    </div>
    <div class="feature">
      <h3>📚 Curated Topics</h3>
      <p>From science to soft skills, explore a wide range of curated, high-impact topics.</p>
    </div>
  </section>

  <footer>
    &copy; 2025 Mindbyte. All rights reserved.
  </footer>

</body>
</html>

"""

@app.route('/feature')
def feature():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Mindbyte – Features</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    body {
      margin: 0;
      font-family: 'Inter', sans-serif;
      background-color: #f9f9f9;
      color: #333;
    }
    header {
      background-color: #4f46e5;
      color: white;
      padding: 1.5rem 2rem;
      text-align: center;
    }
    nav {
      margin-top: 0.5rem;
    }
    nav a {
      color: white;
      margin: 0 1rem;
      text-decoration: none;
      font-weight: 500;
    }
    .container {
      padding: 3rem 2rem;
      max-width: 1000px;
      margin: auto;
    }
    .container h1 {
      text-align: center;
      margin-bottom: 2rem;
      color: #4f46e5;
    }
    .feature-box {
      background: white;
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 2rem;
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
    }
    .feature-box h2 {
      margin-top: 0;
      color: #3b3b98;
    }
    .feature-box p {
      font-size: 1.1rem;
      line-height: 1.6;
    }
    footer {
      text-align: center;
      padding: 1.5rem;
      background: #f1f1f1;
      font-size: 0.9rem;
      margin-top: 3rem;
    }
  </style>
</head>
<body>

  <header>
    <h1>Mindbyte</h1>
    <nav>
      <a href="index.html">Home</a>
      <a href="features.html">Features</a>
      <a href="about.html">About</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>

  <section class="container">
    <h1>Explore Mindbyte's Features</h1>

    <div class="feature-box">
      <h2>⚡ Bite-Sized Lessons</h2>
      <p>Mindbyte delivers compact, powerful lessons designed to be completed in just a few minutes. Perfect for busy learners who want to make consistent progress without overwhelming study sessions.</p>
    </div>

    <div class="feature-box">
      <h2>🎯 Personalized Learning Goals</h2>
      <p>Set daily or weekly goals to stay motivated and on track. Whether you're brushing up on skills or diving into a new topic, Mindbyte helps you stay focused and accountable.</p>
    </div>

    <div class="feature-box">
      <h2>🧠 Topic Variety</h2>
      <p>From science and tech to soft skills and creativity, our curated topics cover a wide spectrum to satisfy curious minds and support personal growth.</p>
    </div>

    <div class="feature-box">
      <h2>📊 Progress Tracking</h2>
      <p>Track your learning journey with clear visuals and insights. Celebrate milestones and see how your consistency turns into knowledge gains.</p>
    </div>

    <div class="feature-box">
      <h2>📱 Mobile-Friendly Experience</h2>
      <p>Mindbyte is built for modern learners — access your lessons on any device, anytime. Whether you’re on a quick break or commuting, your learning goes with you.</p>
    </div>
  </section>

  <footer>
    &copy; 2025 Mindbyte. All rights reserved.
  </footer>

</body>
</html>
"""


if __name__== "__main__":
    app.run(debug=True)

    

