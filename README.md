
# 📝 My Personal Blog Website

A simple and responsive personal blog website built using **Python, Flask, HTML, and CSS**. This project fetches blog posts from an external API and dynamically displays them on a homepage. Users can click the **Read More** button to view the full content of individual blog posts.

## 🚀 Features

- **Dynamic Homepage:** Displays all blog posts fetched from an external API.
- **Individual Blog Pages:** View the complete content of a selected blog post.
- **Flask Routing:** Uses Flask routes to navigate between the homepage and individual blog pages.
- **API Integration:** Fetches blog data using the Requests library.
- **Jinja2 Templating:** Dynamically displays blog content using Flask's template engine.
- **Responsive Design:** Simple and clean user interface using CSS.
- **Static Files Support:** Includes a static folder for images and other assets.

## 🛠️ Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- Jinja2
- Requests Library
- Npoint API

## 📂 Project Structure

```text
EXERCISE/
│
├── templates/
│   ├── index.html
│   └── post.html
│
├── main.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd EXERCISE
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install Required Libraries

```bash
pip install flask requests
```

### 5. Run the Application

```bash
python main.py
```

### 6. Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

## 🔗 Application Routes

| Route | Description |
|---|---|
| `/` | Displays all blog posts |
| `/blog/<number>` | Displays an individual blog post based on its ID |

## 🔄 How It Works

1. When a user visits the homepage, Flask sends a GET request to the Npoint API.
2. The API returns blog posts in JSON format.
3. Flask passes the blog data to `index.html` using `render_template()`.
4. Jinja2 loops through all posts and displays their titles and subtitles.
5. When the user clicks **READ MORE**, they are redirected to the corresponding blog page.
6. Flask retrieves the selected post using its ID.
7. The complete blog content is displayed using `post.html`.

## 📡 API Integration

This project uses the following API endpoint to retrieve blog posts:

```text
https://api.npoint.io/c790b4d5cab58020d391
```

The API provides blog data, including:

- `id`
- `title`
- `subtitle`
- `body`

## 👨‍💻 Author

**Vishnu K V**

Personal Blog Website Project

⭐ If you like this project, feel free to star the repository!
