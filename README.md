# RecipeBook

---
## Setup Instructions


### Prerequisites

Ensure you have the following installed on your system:
- [Docker](https://www.docker.com/) (you may want to use docker desktop)
- [Docker Compose](https://docs.docker.com/compose/install/) (if not included with Docker)

### Steps

1. **Clone the Repository**
   ```bash
   git clonehttps://github.com/ethanelliot7/recipe-book-backend.git
   cd recipe-book-backend

### running with docker
2. **Create an .env file and add the following**
   ```.env
   POSTGRES_DB=your_database_name
   POSTGRES_USER=your_database_user
   POSTGRES_PASSWORD=your_database_password
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```
3. **Build and Start the Containers**
   ```bash
   # Run the following command to build the Docker images and start the containers:
   docker-compose up --build
   ```
4. **Access the Application**
Once the containers are up and running, open your browser and navigate to:  
[http://localhost:8000](http://localhost:8000)


5. **Run Migrations (First-Time Setup)**
If this is the first time running the project, apply the database migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```
6. **Create a Superuser (Optional)**
To access the Django admin panel, create a superuser by running:
   
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
   
7. **Stop the Containers**
When you're done working with the project, stop the containers with:
   ```bash
   docker-compose down
   ```