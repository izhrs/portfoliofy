# Portfoliofy

Portfoliofy is a Django REST Framework (DRF)-powered backend built to support a personal portfolio website. It handles essential backend functionalities like sending contact emails, managing project and testimonial sections, and serving as a fully featured personal blog platform. The backend is designed to be robust, scalable, and integrates seamlessly with modern tools and services.

## Features

-   **Contact Form Integration**

    -   Handles sending emails from the portfolio's contact form.
    -   Sends acknowledgment emails to users.
    -   Notifications for the admin.

-   **Project Management**

    -   API endpoints to manage and display projects dynamically on the frontend.
    -   Optimized for showcasing detailed project portfolios.

-   **Testimonial Management**

    -   API endpoints to display testimonials dynamically on the frontend.

-   **Personal Blog Platform**

    -   Fully featured blogging system.
    -   Create, edit, delete, and retrieve blog posts.
    -   Handles categories, posts and featured post.

-   **Admin Panel Enhancements**

    -   Beautiful and functional admin interface with [Django Unfold](https://unfoldadmin.com).

-   **Media Management**

    -   Media files are stored and served through [Cloudinary](https://cloudinary.com/) for fast and reliable delivery.

-   **Database Management**

    -   Uses [Neon Postgres](https://neon.tech/) for an efficient and scalable database solution.

-   **Deployment**
    -   Hosted on [Vercel](https://vercel.com/) for fast and reliable delivery.

---

## Tech Stack

-   **Backend**: Django, Django REST Framework
-   **Database**: Neon Postgres
-   **Media Storage**: Cloudinary
-   **Admin Interface**: Django Unfold
-   **Deployment**: Vercel

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/izharxyz/portfoliofy.git
    cd portfoliofy
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**

    Create a `.env` file in the root directory and add the following:

    ```bash
     # replace the values with your own

     ENV=development
     FRONTEND_URL=http://localhost:3000
     SECRET_KEY="secret--C%aiaAxqo75mSYPeeFgjYk^mjgpnP"
     ALLOWED_HOSTS="localhost,127.0.0.1,.vercel.app"
     CORS_ORIGIN_WHITELIST="http://localhost:3000,https://your-frontend-url.vercel.app"

     DATABASE_URL='postgres://postgres:password@localhost:5432/portfoliofy'

     EMAIL_HOST=smtp.resend.com
     EMAIL_PASS=re_secret-C%aiaAxqo75mSYPeeFgjYk^mjgpnP
     EMAIL_PORT=2587
     EMAIL_USER=resend
     DEFAULT_FROM_EMAIL="name@domain.con"

     CLOUDINARY_CLOUD_NAME=FgjYk^mjgpnP
     CLOUDINARY_API_KEY=788907654321234
     CLOUDINARY_API_SECRET=eseaiaAxqo75mSYPemjgpnP
    ```

5. **Run Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a Superuser**

    ```bash
     python manage.py createsuperuser
    ```

7. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

-   **Contact Form**

    -   `/api/v1/contact/` - POST request to send an email from the contact form.

-   **Projects**

    -   `/api/v1/projects/` - GET request to retrieve all projects.

-   **Testimonials**

    -   `/api/v1/testimonials/` - GET request to retrieve all testimonials.

-   **Blog**
    -   `/api/v1/blog/posts/` - GET request to retrieve all blog posts.
    -   `/api/v1/blog/posts/<slug>/` - GET request to retrieve a single blog post.
    -   `/api/v1/blog/posts/featured` - GET request to retrieve featured blog posts.
    -   `/api/v1/blog/categories/` - GET request to retrieve all blog categories.
    -   `/api/v1/blog/categories/<slug>/` - GET request to retrieve a single blog category.

## License

This project is licensed under a custom MIT License. See the [LICENSE](LICENSE) file for more information.
