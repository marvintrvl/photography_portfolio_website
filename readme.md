# Django Photography Portfolio Website

This is a Django project for creating a photography portfolio website. It allows you to showcase your photos in different categories and subcategories.

## Installation

1. Clone the repository:
    - Create an empty GitHub repository 
    - Clone my repository and add it to your own, empty repository:

    ```bash
    git clone https://github.com/marvintrvl/photography-portfolio-website.git
    git remote remove origin
    git init
    git remote add origin <your_empty_repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd photography-portfolio-website
    ```

3. Create a virtual environment and activate it:

    ```bash
    python -m venv myenv
    source env/bin/activate  # For Linux/Mac
    .\myenv\Scripts\activate  # For Windows
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Adjust the HTML templates:

    - Open the `templates` directory.
    - Modify the HTML templates based on the provided comments to customize the look and feel of your website.

6. Add your photos into categories and subcategories:

    - Open the `/photos/static/` directory.
    - Create directories for your desired categories and subcategories.
    - Add your photos into the respective subcategories.
    - Important: Name folder exactly like the name of the category and put the subcategories in them and ONLY add photos in the subcategories

7. Run the script to add the photos to the database:

    - Navigate to /photography_portfolio_website/ (ROOT Directory) and then run this command

    ```bash
    python manage.py import_photos
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your web browser and visit `http://127.0.0.1:8000/` to see your photography portfolio website.

10. (Optional) Create a superuser account for the database interface:

    ```bash
     python manage.py createsuperuser
    ```
11. Hosting it on pythonanywhere for free
    - Create a user account under [text](https://www.pythonanywhere.com/registration/register/beginner/)
    - Follow instructions here and choose Manual Configuration: [text](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
    - Hint: replace 
    ```bash
    path = '/home/myusername/mysite'
    the os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    ```
    with:
    ```bash
    path = '/home/myusername/photography_portfolio_website'
    the os.environ['DJANGO_SETTINGS_MODULE'] = 'photo_website.settings'
    ```

    - Configure static files with:

    ```bash
    URL: /static/ Directory: /home/your_username/photography_portfolio_website/static/	 
    URL: /media/ Directory: /home/your_username/photography_portfolio_website/media/
    ```
