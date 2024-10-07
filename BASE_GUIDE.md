# Next.js - Django - Postgress  
# FullStack Project Template  
# Setup Guide


---
This guide will walk you through setting up a basic React - Next.js project using JavaScript. We'll explain each step in detail to help you understand what we're doing and why it's necessary.


## 0. Prerequisites

### Install Node.js

Next.js is built on top of Node.js, so you'll need to install it first.
1. Go to [Node.js official website](https://nodejs.org/).
2. Download and install the **LTS (Long Term Support)** version.

### Install Visual Studio Code (VS Code)
We recommend using VS Code as it's a popular, free code editor with excellent JavaScript support.

1. Visit [Visual Studio Code](https://code.visualstudio.com/).
2. Download and install **VS Code**.

---

## TASK 1. SETUP YOUR FRONTEND AND BACKEND 



### Step 1: Create and Setup Your Django Backend Folders 

1. In your choose location create a folder **"base_project"**.
2. Inside of that folder `base_project`, create a new folder **"datastore"**.
- This folder will holder your backend code and django datastore ORM 
3. Open up VS Code and drag the datastore folder `datastore` inside VS Code. Or in VS Code open the `datastore` folder
- **IMPORTANT** Make sure drag or open the `datastore` folder NOT the  **base_project** inside VS Code. 
4. Now click ***File*** in the top left corner of VS Code and click ***Save Workshop As...***, and select the datastore folder. 
- You should now have a `datastore.code-workspace` json type file in the root directory 
5. Make sure you are Inside your Datastore `datastore` and create a folder called **"src"**
6. Navigate inside the `src` folder

```bash
cd src
```

### Step 2: Setup Your Django Backend 

1. inside the SRC folder `datastore/src/` 

2. Install these python packages below:
comehere 


```bash
  pip install django djangorestframework django-cors-headers psycopg2-binary dj-database-url python-dotenv rav
```
or 

```bash
pip install -r requirements.txt
```

3. Start a new Django admin project with `django-admin startproject core .` dont forget the "." so you dont create an extra (two `core`) folders.
 
```bash
  django-admin startproject core .
```
4. Create a new Django api app
- This will create the api folder
  
```bash
  python manage.py startapp api
```

### Updated Project Folder Structure Backend 1.

If everything was set up correctly, your project folder structure should look like this:

```markdown
C: datastore
└───src
    ├───api
    │   └───migrations
    └───core
        └───__pycache__

```


### Step 3: Test Backend is Setup and Running

1. Navigate back out of the the `src` folder, to the `datastore`,
2. Create a yaml file called **"rav"**

```bash 
rav.yaml
```

3. Inside the `rav.yaml` file copy the code below. 
- This code will be used to run our commands for the backend similar to node's  "npm run ... " scripts 
- This file will contain all the commonds for our backend django run commands

```bash 
scripts:
  server:
    - cd src &&  python manage.py runserver 8001
  makemigrations:
    - cd src && python manage.py makemigrations
  migrate:
    - cd src && python manage.py migrate
  shell:
    - cd src && python manage.py shell
  curl_auth: |
    curl -X POST -H "Content-Type: application/json" -d '{"username": "cfe", "password": "learncode"}' http://127.0.0.1:8001/api/token/pair
  curl_protect: |
    curl -X GET -H "Authorization: Bearer <curl_auth-access-token>" http://127.0.0.1:8001/api/me
```

2. Back in the terminal run the command  rav run server
- This will run the script in the rav file to run our django server locally at port 8001

```bash 
rav run server
```
3. Open your web browser and go to [http://localhost:8001](http://localhost:8001). You should see the default django app start page.

You shoud now see the defult django start page with text saying **The install worked successfully! Congratulations!**


### Step 4: Setup Your Nextjs frontend

1. Navigate back out of the `datastore` folder
- You should now be outside of the Datastore folder and inside your `base_project` folder and ready to create your frontend appliacation.

```bash
cd ..
```

2. Now that you are in the `base_project` folder. Use `npx` to create a new Next.js project with JavaScript:

```bash
npx create-next-app@latest 
```

3. When prompted, choose the following options:
    -  **Want is your projects name**   interface
    ```bash
    interface
    ```
    - **Would you like to use TypeScript?** No
    - **Would you like to use ESLint?** Yes
    - **Would you like to use Tailwind CSS?** Yes
    - **Would you like to use src/ directory?** Yes
    - **Would you like to use App Router?** Yes   
    - **Would you like to customize the default import alias?** No

These choices set up a basic Next.js project with ESLint and Tailwind CSS, using the new App Router.

Wait for the installation to complete. This may take a few minutes.

### Updated Project Folder Structure Front and Backends 1.

If everything was set up correctly, your project folder structure should look like this:
**BUT**
You won't see it in VS Code until you open a ***New VS code Window*** and open the `interface` folder 

```markdown
C:base_porject.
├───datastore
│   └───src
│       ├───api
│       │   └───migrations
│       └───core
│           └───__pycache__
└───interface
    ├───.next
    ├───node_modules
    └───src
        └───app
            └───fonts
```

### Step 5: Test Frontend is Setup and Running 

1. Open a new VS Code window, and drag the interface folder `interface` inside VS Code. Or click ***file*** in the top left corner and click ***Open Folder*** and  open the `interface` folder
- **IMPORTANT** Make sure drag or open the `interface` folder NOT the  **base_project** inside VS code. 
- This folder will holder your frontend code and nextjs application  


### Note 
You should now have two VS code Windows open, one for the backend called Datastore and the other for the frontend called Interface.


2. In the VS Code window for your Interface, click ***File*** in the top left corner of VS Code and click ***Save Workshop As...***, and select the datastore folder. 
- You should now have a `interface.code-workspace` json type file in the root directory 

3. Open up a new terminal and run the command  npm run dev
- This will run the script in the package.json file to run the server locally at port 3000/3001

```bash 
npm run dev
```
4. Open your web browser and go to [http://localhost:3000](http://localhost:3000). You should see the default Next.js welcome page.

You shoud now see the defult Next JS start page with text saying
**Next.js** logo
**1. Get started by editing src/app/page.js. ....**


## TASK 1 COMPLETE: FRONTEND AND BACKEND IS ALL SETUP!!. 



## TASK 2. FRONTEND(NEXTJS) FILE UPDATES AND CONFIGURATION FOR PRODUCTION READY APPLICAION
If everything was set up correctly, your project folder structure should look like this:

```
C: interface.
├───node_modules
└───src
    ├───app
    │   └───fonts
    └───styles
```

**Folder and File Breakdown:**

- **node_modules/**: Contains all the dependencies for your project.
- **src/**: Contains your application source code.
  - **app/**: Where you define your routes and pages.
    - **fonts/**: Contains your global font files.
    - **favicon.ico**: The default icon that appears in the browser tab when users visit your site. It helps in branding your application by showing a small image or logo next to the page title.
    - **globals.css**: Global styles for your app.
    - **layout.js**: Defines the root layout for the entire application, providing a consistent structure and layout across all pages. It includes common components such as navigation bars, footers, and global styles.
    - **page.js**: The homepage of your app.
- **.eslintrc.json**: ESLint configuration for linting and code quality.
- **.gitignore**: Specifies which files and folders should be ignored by Git.
- **next.config.js**: Next.js configuration file.
- **package.json**: Contains project metadata and dependencies.
- **package-lock.json**: Auto-generated file that records the exact versions of installed dependencies, ensuring a consistent environment across different installations.
- **postcss.config.mjs**: Configuration file for PostCSS, which is used to process and transform your CSS (required for Tailwind CSS integration).
- **tailwind.config.js**: Configuration file for Tailwind CSS, where you can customize the default theme, plugins, and other Tailwind options.

---

### Step 1: Modify and update files and folders  

1. Create a new folder called `styles` inside the `app` folder: `src/app/styles/`.

2. Move the `globals.css` file into the new `styles` folder: `src/app/styles/globals.css`.

3. Open the `page.js` file located at `src/app/page.js` and replace all its content with the following code:

```javascript
import styles from './styles/Home.module.css'
import Head from 'next/head'

export default function Home() {
    return (
    <div className={styles.container}>
        <Head>
            <title>Base React Project</title>
            <meta name="description" content="A Next.js React application" />
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className={styles.main}>
            <h1 className={styles.title}>
                Welcome to Base React Project!
            </h1>
            <br/>

            <p className={styles.description}>
                Get started by editing{' '}
                <code className={styles.code}>src/app/page.js</code>
            </p>
            <br/>
        </main>

        <footer className={styles.footer}>
            <a
                href="https://nextjs.org"
                target="_blank"
                rel="noopener noreferrer"
            >
                Powered by Next.js
            </a>
        </footer>
    </div>
    )
}
```

4. Open the `layout.js` file located at `src/app/layout.js` and replace all its content with the following code:

```javascript
import './styles/globals.css';

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`antialiased`}>
        {children}
      </body>
    </html>
  );
}
```


5. Replace the code inside `global.css` now located at `src/app/styles/global.css` with the following:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #ffffff;
  --foreground: #171717;
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #0a0a0a;
    --foreground: #ededed;
  }
}

@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
} 

@font-face {
  font-family: 'GeistMono';
  src: url('./fonts/GeistMonoVF.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Geist';
  src: url('./fonts/GeistVF.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

html,
body {
  padding: 0;
  margin: 0;
  font-family: 'Geist', -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,
    Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
}

a {
  color: inherit;
  text-decoration: none;
}

* {
  box-sizing: border-box;
}
```

6. Inside the `layout.js` file, update the file path for `globals.css` as follows:

- From `import ".globals.css";`
- To `import "./styles/globals.css";`


7. Create a new file inside `styles` called `Home.module.css` at `src/app/styles/Home.module.css` 

```bash
Home.module.css
```

- Add the following code to the file:

```css
.container {
    min-height: 100vh;
    padding: 0 0.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.main {
    padding: 5rem 0;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.footer {
    width: 100%;
    height: 100px;
    border-top: 1px solid #eaeaea;
    display: flex;
    justify-content: center;
    align-items: center;
}

.footer a {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-grow: 1;
}

.title {
    margin: 0;
    line-height: 1.15;
    font-size: 4rem;
    text-align: center;
}

.description {
    text-align: center;
    line-height: 1.5;
    font-size: 1.5rem;
}

.code {
    background: #910909;
    color: #eaeaea;
    border-radius: 5px;
    padding: 0.75rem;
    font-size: 1.1rem;
    font-family: Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono,
        Bitstream Vera Sans Mono, Courier New, monospace;
}
```

8. Move the `fonts` folder into the `styles` folder. Move the fonts folder from `src/app/fonts` to `src/app/styles/fonts`.

9. Save all these file changes.

10. Refresh your browser at [http://localhost:3000](http://localhost:3000). You should now see a custom welcome page titled "Welcome to Base React Project!"


### Updated Project Folder Structure Frontend 1.

Your project folder structure should now look like this:

```markdown
C: interface.
├───.next
├───node_modules
├───public
│   ├───fonts
│   └───favicon.ico
└───src
    └───app
        ├───styles
        │   ├───globals.css
        │   └───Home.module.css
        ├───layout.js
        └───page.js
```

**Folder and File Breakdown:**

- **node_modules/**: Contains all the dependencies for your project.
- **public/**: Stores static assets like images and fonts.
  - **fonts/**: Contains your global font files.
  - **favicon.ico**: The default icon that appears in the browser tab when users visit your site, helping with branding by showing a small image or logo next to the page title.
- **src/**: Contains your application source code.
  - **app/**: Where you define your routes and pages.
    - **layout.js**: Defines the root layout for the entire application, providing a consistent structure and layout across all pages. It includes common components such as navigation bars, footers, and global styles.
    - **page.js**: The homepage of your app.
    - **styles/**: Contains your global and modular CSS files.
        - **globals.css**: Global styles for your app.
        - **Home.module.css**: Module-specific styles for the homepage.
- **.eslintrc.json**: ESLint configuration for linting and code quality.
- **.gitignore**: Specifies which files and folders should be ignored by Git.
- **next.config.js**: Next.js configuration file.
- **package.json**: Contains project metadata and dependencies.
- **package-lock.json**: Auto-generated file that records the exact versions of installed dependencies, ensuring a consistent environment across different installations.
- **postcss.config.mjs**: Configuration file for PostCSS, which is used to process and transform your CSS (required for Tailwind CSS integration).
- **tailwind.config.js**: Configuration file for Tailwind CSS, where you can customize the default theme, plugins, and other Tailwind options.


### Step 2: Update Configuration and Environment Variables

1. In the root of your project, locate the `.eslintrc.json` and the `next.config.js` file. Replace their contents with the following configuration:

#### `.eslintrc.json`

```json
{
  "extends": ["next/core-web-vitals"]
}
```

#### `next.config.js`
1. MUST: Rename your file from `next.config.mjs` to `next.config.js`. removing the `m` from the file name 
Remove all the code in `next.config.ms` and replace it with the following:

```javascript

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = nextConfig;
```

### Step 3:  PostCSS and Tailwind CSS Configuration


1. MUST: Rename your file from `postcss.config.mjs` to `postcss.config.js`. removing the `m` from the file name. 
Configure PostCSS and Tailwind CSS for processing your CSS files. Remove all the code in `postcss.config.mjs` and replace it with the following:

#### `postcss.config.js`

```javascript

module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

In the `tailwind.config.js`, remove all the tailwind config content and replace it with the code below:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
    },
  },
  plugins: [],
};
```



### Updated Project Folder Structure Frontend 2.

After implementing the above steps, the folder structure for the project should look like this:

```markdown
C:interface.
├───.next
├───node_modules
├───public
│   └───fonts
└───src
    └───app
        └───styles
```

**Folder and File Breakdown:**

- **node_modules/**: Contains all the dependencies for your project.
- **public/**: Stores static assets like images.
  - **fonts/**: Contains your global font files.
  - **favicon.ico**: The default icon that appears in the browser tab when users visit your site. It helps in branding your application by showing a small image or logo next to the page title.
- **src/**: Contains your application source code.
  - **app/**: Where you define your routes and pages.
    - **layout.js**: Defines the root layout for the entire application, providing a consistent structure and layout across all pages. It includes common components such as navigation bars, footers, and global styles.
    - **page.js**: The homepage of your app.
    - **styles/**: Contains your global and modular CSS files.
        - **globals.css**: Global styles for your app.
        - **Home.module.css**: Module-specific styles for the homepage.
- **.eslintrc.json**: ESLint configuration for linting and code quality.
- **.gitignore**: Specifies which files and folders should be ignored by Git.
- **next.config.js**: Next.js configuration file.
- **package.json**: Contains project metadata and dependencies.
- **package-lock.json**: Auto-generated file that records the exact versions of installed dependencies, ensuring a consistent environment across different installations.
- **postcss.config.mjs**: Configuration file for PostCSS, which is used to process and transform your CSS (required for Tailwind CSS integration).
- **tailwind.config.js**: Configuration file for Tailwind CSS, where you can customize the default theme, plugins, and other Tailwind options.


## FRONTEND BASE SETUP COMPLETE!

To complete the React Base Project Template, there is a list of tasks still needed to get the project template finished.

# Tasks 

1. Upgrade frontend Structure Base Architecture (RSC - Container and Presentational)
2. Deploy Appliacations Front and backends (railway) push to github
3. Database setup (neon postgres)
4. Attach database to backend project and frontend 
6. Base Styles for Appliacation 
7. Static file uplaod Add image upload. 

- Part One complete 
- Start new Project follwoing part one steps 

8. Add Soical Authentication (w/ Clerk)

7. Error management (w/ Sentry)
9. Analytics (Posthog)
10. Rate limiting (Upstash)


Install all the Dependencies and  DevDependencies below

- ***Dependencies***
```bash
npm install @t3-oss/env-nextjs@^0.11.1 dotenv@^16.4.5  next@14.2.13 pg@^8.13.0 pg-pool@^3.7.0 postgres@^3.4.4 react@^18 react-dom@^18 zod@^3.23.8
```
- ***DevDependencies***
```bash
npm install autoprefixer css-loader@^7.1.2 eslint eslint-config-next@14.2.13 file-loader@^6.2.0 postcss@^8 style-loader@^4.0.0 tailwindcss@^3.4.1 --save-dev
```



## TASK 3. BACKEND(DJANGO) FILE UPDATES AND CONFIGURATION FOR PRODUCTION READY APPLICAION

### Step 1: Modify and update files and folders  

1. Inside the Core folder head to Setting file `datastore/core/settings.py` replace all the setting code with the below:

```py

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from decouple import config

# Load environment variables
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
SECRET_KEY = 'DJANGO_SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', 'False') == 'True'
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']


CORS_ALLOW_ALL_ORIGINS = True  # For development, restrict this in production

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# If you need to allow specific HTTP methods
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# If you need to allow specific headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# If you need to allow credentials (cookies, authorization headers)
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

```

---


2. Inside the Core folder head to Urls file `datastore/core/urls.py`,  replace all the url code with the below:
  These urls will point us to our admin dashboard for the dev team 
  And to our api endpoints to PUSH and GET data
  The redirect automatically directs from base URL `http://127.0.0.1:8001/`  to the API endpoint `http://127.0.0.1:8001/api/` 


```py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

```


3. Inside the Core folder head to WSGI file `datastore/core/wsgi.py`,  replace all the code with the below:

```py
import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

```



4. Inside the Api folder create a `urls.py` file should look like this `datastore/api/urls.py`,  

```bash
urls.py
```
- These urls are our API urls, will allow us to CREATE/SEND/PUSH and GET date from the Vercel Postges database.
- Below is a API to create user, and to retrieve a user using the user ID
- The **api_root** will take up to our datastore api home page / project root URL  
Copy all code below:

```py
from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy,  api_root

urlpatterns = [
    path('', api_root, name='api-root'), 
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
]
```

5. Inside the api folder head to models file `datastore/api/models.py`,  replace all the model code with the below:
- This code below creates the structure of the User object.

```py
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

6. Inside the api create a serializers file should look like this `datastore/api/serializers.py`, 

```bash
serializers.py
``` 
- This code purpose is to convert the data types in the models to Python data types that can be easily rendered into JSON, XML when sending or being recieved from an API. 
Copy the code below:

```py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']
```


7. Inside the api folder head to views file `datastore/api/views.py`,  replace all the views code with the below:
- This code below sets up the view for the root URL in your Django project 
- It also connects our models to the api urls  `models.py` --> `urls.py` Defining how the data from `models` is processed and presented
- 

```py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def api_root(request):
    return Response({"message": "Welcome to the Django API DataStore"})

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

8. Now head to your Manage file  `datastore/manage.py`,  replace all the manage code with the below:
  The manage.py does various administrative tasks  it will start up the development server, set up the admin, Run migrations.
  Sets up the Django environment in using the setting.py file. 
```py

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

```


### Step 2: Make Migrations and Migrate 

1. In the terminal I need to **Make Migrations**
- Make sure your in the root dir `datastore` and run the command **"rav run makemigrations "**
- This will run the `python manage.py makemigrations` 
- Make migrations will detects changes in your models (e.g., new fields, changed field types)
- Creates new migration files in your app's migrations folder

```bash 
rav run makemigrations 
```

2. Then after running make migration, will need to run **Migrate**
- Run the command **"rav run migrate"**
- This will run the `python manage.py migrate` 
- Migrate will Applies pending migrations to your database
- Creates or alters database tables to match your current model definitions
- Updates the database schema without losing existing data

```bash
rav run migrate
```

3. Run the command  **"rav run server"** again if your server is closed 
- This will run the script in the rav file to run our django server locally at port 8001

```bash 
rav run server
```
4. Open your web browser and go to [http://localhost:8001](http://localhost:8001). You should see the default django app start page.

You shoud now see  be redireted to the `api` endpoint `http://127.0.0.1:8001/api/` and see the defult Django REST framework page witha message  saying **{"message": "Welcome to the Django API DataStore"}**

Your Django backend is now set up and running with a database that matches your defined models. The User model you created earlier is now represented in your database.


### Step 3: Create superuser for your Admin 


1. In the terminal, make sure you're in the root directory `datastore`.

2. Run the command to create a superuser.
- This will run the `python manage.py createsuperuser` command.
- The createsuperuser command creates a user who has all permissions.

```bash
rav run createsuperuser
```

3. You will be prompted to enter the following information:
- Username (can be anything you choose)
- Email address (optional, you can leave this blank by pressing Enter)
- Password (enter a strong password)
- Password confirmation (re-enter the same password)
- If the passwords match and meet Django's requirements, you'll see a success message

Example:

```bash
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
```

4. To test your superuser account, run your server if it's not already running:
```bash
rav run server
```

5. Open your web browser and go to the **Admin**  [http://localhost:8001/admin](http://localhost:8001/admin)
- You should see the Django admin login page. Enter the username and password you just created.
- After logging in, you'll have access to the Django admin interface, where you can manage your database and application data.
- This superuser account will give you full access to manage your Django application through the admin interfaceenance tasks.


### Step 4: Add a Admin (Superuser) API Endpoint 


1. First, let's keep by updating the serializer file `datastore/api/serializers.py`:
- Import the built-in django auth model `from django.contrib.auth.models import User as AdminUser`
- Then create a Admin User Serializer class  

```python
from rest_framework import serializers
from .models import User
from django.contrib.auth.models import User as AdminUser

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['id', 'first_name', 'last_name', 'email', 'created_at']
      read_only_fields = ['id', 'created_at']


class AdminUserSerializer(serializers.ModelSerializer):
  class Meta:
      model = AdminUser
      fields = ['id', 'username', 'email', 'is_staff', 'is_superuser', 'date_joined']
      read_only_fields = ['id', 'date_joined', 'is_staff', 'is_superuser']
```

2. Update `datastore/api/views.py`
- Import the `AdminUserSerializer` from `api/serializers.py` 
- Import the built-in django auth model `from django.contrib.auth.models import User as AdminUser` 
- Create a Admin User List class 

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, AdminUserSerializer
from django.contrib.auth.models import User as AdminUser

@api_view(['GET'])
def api_root(request):
return Response({"message": "Welcome to the Django API DataStore"})

class UserListCreate(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class AdminUserList(generics.ListAPIView):
  queryset = AdminUser.objects.all()
  serializer_class = AdminUserSerializer
```

3. Update `datastore/api/urls.py`
- Import the `AdminUserList` from `api/views.py` 
- Add the `admin-user` path to the array list of paths 

```python
from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy, AdminUserList, api_root

urlpatterns = [
path('', api_root, name='api-root'),
path('users/', UserListCreate.as_view(), name='user-list-create'),
path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
path('admin-users/', AdminUserList.as_view(), name='admin-user-list'),
]
```

4. Run migrations to ensure all changes are applied:

```bash
rav run makemigrations
rav run migrate
```

5. Restart your server:

```bash
rav run server
```

### Step 5: Test the New Endpoints for User and Admin 

1. To view your custom users:
- Visit `http://127.0.0.1:8001/api/users/`
- This will show the users created with your custom User model

2. To view admin users (including superusers):
- Visit `http://127.0.0.1:8001/api/admin-users/`
- This will show all users created through Django's admin, including superusers

**Important Notes!**:

- The `/api/users/` endpoint allows creating new custom users.
- The `/api/admin-users/` endpoint is read-only for security reasons. Creating admin users should typically be done through Django's admin interface or management commands.
- In a production environment, you'd want to add authentication and proper permissions to these views to ensure data security.


### Updated Project Folder Structure Backend 2.

If everything was set up correctly, your project folder structure should look like this:

```markdown
C: datastore
├──src
    ├───api
    │   └───migrations
    └───core
        └───__pycache__
```

- **datastore/**: Root directory of your Django project.
  - **src/**: Contains the main project files.
    - **api/**: Your custom Django app for handling API requests.
      - **migrations/**: Contains database migration files.
        - **__init__.py**: Indicates that the migrations directory is a Python package.
      - **__init__.py**: Indicates that the api directory is a Python package.
      - **admin.py**: Configuration file for the Django admin interface.
      - **apps.py**: Configuration file for the api app.
      - **models.py**: Defines your data models (e.g., User model).
      - **serializers.py**: Defines serializers for converting model instances to JSON.
      - **tests.py**: Contains test cases for your api app.
      - **urls.py**: Defines URL patterns for your api views.
      - **views.py**: Contains view functions or classes that handle requests and return responses.
    - **core/**: The main Django project directory.
      - **__init__.py**: Indicates that core is a Python package.
      - **asgi.py**: ASGI configuration for deploying your project with ASGI servers.
      - **settings.py**: Contains all the configuration for your Django project.
      - **urls.py**: The main URL configuration for your entire project.
      - **wsgi.py**: WSGI configuration for deploying your project with WSGI servers.
    - **manage.py**: A command-line utility for interacting with your Django project.
  - **rav.yaml**: Configuration file for the rav command runner.
  - **requirements.txt**: Lists all Python dependencies for your project.


### Key Directories and Files:

- **src/api/**: This is where most of your custom code resides.
- **src/core/settings.py**: Central configuration file for the entire Django project.
- **src/core/urls.py**: Main URL routing file.
- **src/manage.py**: Used for running Django commands.
- **rav.yaml**: Custom command runner for your project.



## TASK 4. CONNECT FRONTEND(NEXTJS) AND BACKEND(DJANGO)

### Step 1: Update the Backend(Django) Configurations  

1. Let's start by updating the backend
- Update CORS settings in `datastore/src/core/settings.py`
- Make sure that the below setting are in place

```python
INSTALLED_APPS = [
    # ... other apps
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ... other middleware
]

CORS_ALLOW_CREDENTIALS = True
```

2.  Remove or comment out **CORS_ALLOW_ALL_ORIGINS = True**
- Add/Replace with  **CORS_ALLOWED_ORIGINS** to the local host 3000/3001  to the `setting.py` file

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",

]
```


### Step 2: Update the Backend(Django) API Functions and End Points


1. Update `datastore/src/api/views.py` to ensure it returns JSON responses
- Will be updating the **UserListCreate** to be able to create users, will be using function based views for more control, less abstraction. 
- Here's the updated `views.py` file with all views converted to function-based views:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, AdminUserSerializer
from django.contrib.auth.models import User as AdminUser

@api_view(['GET'])
def api_root(request):
    return Response({"message": "Welcome to the Django API DataStore"})

@api_view(['GET', 'POST'])
def user_list_create(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def admin_user_list(request):
    admin_users = AdminUser.objects.all()
    serializer = AdminUserSerializer(admin_users, many=True)
    return Response(serializer.data)
```


2. Now, you need to update your urls.py to include this new view. In your `datastore/src/api/urls.py`, add the following URL pattern:

```python
from django.urls import path
from .views import api_root, user_list_create, user_detail, admin_user_list

urlpatterns = [
    path('', api_root, name='api-root'),
    path('users/', user_list_create, name='user-list-create'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('admin-users/', admin_user_list, name='admin-user-list'),
]
```

### Step 3: Update the Frontend(NextJs) Configaration 

1. Update next.config.js

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${process.env.DJANGO_ENV_API_URL}/:path*`,
      },
    ];
  },
};

module.exports = nextConfig;
```


2. Create a .env.local file in the root of your Next.js project, that will be the end point your django backend. 

```bash
DJANGO_ENV_API_URL=http://127.0.0.1:8001/api/
```


### Step 4: Create the Frontend(NextJs) API End Points



1. In the App folder `src/app/`  create a new folder called **"API"** `src/app/api/`

2. In the API folder `src/app/api/` create a new file called **"axios"** `src/app/api/axios.js`. Copy the code below:
- This is your defualt End Point to your Django backend 


```javascript
import axios from 'axios';

const DJANGO_API_URL = 'http://127.0.0.1:8001/api/'

const axiosInstance = axios.create({
  baseURL: process.env.DJANGO_ENV_API_URL || DJANGO_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

export default axiosInstance;
```

3. Install axios in your Next.js project

```bash
npm install axios

```

4.  In the Api folder `src/app/api` Create a new folder called **"users"** `src/app/api/users/`
5.  In the Users folder `src/app/api/users` Create a new file called **"userListApi"** `src/app/api/users/userListApi.js`.  Copy the code below:
- This Endpoint will be used to get the list of users 


```javascript: 
import axiosInstance from '../axios';

const userListApi = async () => {
  console.log('fetching user data...')
    
  try {
    const response = await axiosInstance.get('/users/');
    console.log('API response:', response);
    return {
      status: 'success',
      data: response.data
    };
  } catch (err) {
    console.error("Error:", err);
    return {
      status: 'error',
      message: err.response?.data?.message || 'Failed to fetch users',
      error: err
    };
  }
};

export default userListApi;
```


6.  In the Users folder `src/app/api/users` Create a new file called **"userCreateApi"** `src/app/api/users/userCreateApi.js`.  Copy the code below:
- This Endpoint will be used to create a new users 

```javascript: 
import axiosInstance from '../axios';

const userCreateApi = async (newUser) => {
  try {
    const response = await axiosInstance.post('/users/', newUser);
    console.log('User creation response:', response);
    return {
      status: 'success',
      data: response.data
    };
  } catch (err) {
    console.error("Error creating user:", err);
    return {
      status: 'error',
      message: err.response?.data?.message || 'Failed to create user',
      error: err
    };
  }
};

export default userCreateApi;
```


### Step 5: Create Add New User Component 

1. In the App folder `src/app/` Create a new folder called **"Components"** `src/app/components/`.

2. In the Components folder `src/app/components/` create a new **JSX** file called **"UserList"** `src/app/components/UserList.jsx`. Copy the code below:
- **IMPORTANT** When changing a file to **JSX** must reload the server again `npm run dev`
- This is a Client Component so at the top of the file will be using `'use client';`
- The code below will import the **userListApi** and **userCreateApi**.
- The component will display the current users once one is created, and will include a form to create a user.

```javascript

'use client';

import { useState, useEffect } from 'react';
import userListApi from '../api/users/userListApi';
import userCreateApi from '../api/users/userCreateApi';

export default function UserList() {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({ first_name: '', last_name: '', email: '' });
  const [isLoading, setIsLoading] = useState(false);
  const [createIsLoading, setCreateIsLoading] = useState(false);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    setIsLoading(true);

    try {
      const response = await userListApi();
      if (response.status === 'success') {
        setUsers(response.data);
      } else {
        setUsers([]);
      }
    } catch (err) {
      console.error(err);
      setUsers([]);
    } finally {
      setIsLoading(false);
    }
  };

  const createUser = async () => {
    setCreateIsLoading(true);
    try {
      const response = await userCreateApi(newUser);
      if (response.status === 'success') {
        setNewUser({ first_name: '', last_name: '', email: '' });
        fetchUsers(); // Refetch users after creating a new one
      } 
    } catch (err) {
      console.error(err);
    } finally {
      setCreateIsLoading(false);
    }
  };

  const handleInputChange = (e) => {
    setNewUser({ ...newUser, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    createUser();
  };

  return (
    <div>
      <h2>User List</h2>
      {isLoading ? (
        <p>Loading users...</p>
      ) : users.length > 0 ? (
        <ul>
          {users.map((user) => (
            <li key={user.id}>
              {user.first_name} {user.last_name} - {user.email}
            </li>
          ))}
        </ul>
      ) : (
        <>
        <br/>
        <p>User List Pending...</p>
        </>
      )}
      <br/>

      <h3>Add New User</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="first_name"
          value={newUser.first_name}
          onChange={handleInputChange}
          placeholder="First Name"
          required
        />
        <input
          type="text"
          name="last_name"
          value={newUser.last_name}
          onChange={handleInputChange}
          placeholder="Last Name"
          required
        />
        <input
          type="email"
          name="email"
          value={newUser.email}
          onChange={handleInputChange}
          placeholder="Email"
          required
        />
        <button type="submit" disabled={createIsLoading}>
          {createIsLoading ? 'Creating...' : 'Add User'}
        </button>
      </form>
    </div>
  );
}
```


### Step 6: Add User Component to Welcome(Home) Page 

1. Update Page.js `src/app/page.js` import the **UserList** from the component folder `'./components/UserList'`
2. Add the Userlist component **<UserList/>** to the <main> under the <br/> 
- Page.js is a Server Component

```javascript
import styles from './styles/Home.module.css'
import Head from 'next/head'
import UserList from './components/UserList';

export default function Home() {
    return (
    <div className={styles.container}>
        <Head>
            <title>Base React Project</title>
            <meta name="description" content="A Next.js React application" />
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className={styles.main}>
            <h1 className={styles.title}>
                Welcome to Base React Project!
            </h1>
            <br/>
            <p className={styles.description}>
                Get started by editing{' '}
                <code className={styles.code}>src/app/page.js</code>
            </p>
            <br/>
            <UserList/>
        </main>
       
        <footer className={styles.footer}>
            <a
                href="https://nextjs.org"
                target="_blank"
                rel="noopener noreferrer"
            >
                Powered by Next.js
            </a>
        </footer>
    </div>
    )
}
```


1. Run your Next.js development server if not running 

```bash
npm run dev
```

2. Open your web browser and go to the [http://localhost:3000/](http://localhost:3000/)
- You should now see a form on the screen allowing the user to enter a **First Name**, **Last Name** and **Email** 
With a **Add User Button** 

3. To test that the API connection is running make sur that your backend server is still running
- Go over to your backend project window in VS code and Ensure your Django server is running on port 8001

```bash
rav run server
```

4. Now that your Frontend and Backend are both running, Go back to your web browser and go to [http://localhost:3000/](http://localhost:3000/)

5. Enter a **First Name**, **Last Name** and **Email**  and then press ***Add User***
- You should now see your new user above the form under **User List**

6. To see that it has updated your API  view your custom users by going to [http://127.0.0.1:8001/api/users/](http://127.0.0.1:8001/api/users/)
- This should now show the users you created! 


### FRONTEND AND BACKEND ARE NOW CONNECTED!


### Updated Project Folder Structure Frontend 3.
If everything was set up correctly, your project folder structure should look like this:

```markdown
C: interface.
├───.next
├───node_modules
└───src
    └───app
        ├───api
        │   └───users
        ├───components
        └───styles
            └───fonts
```

**Folder and File Breakdown:**

- **node_modules/**: Contains all the dependencies for your project.
- **src/**: Contains your application source code.
  - **app/**: Where you define your routes and pages.
    - **api/**: Contains API-related files and functions.
      - **users/**: User-specific API functions 
    - **components/**: Reusable React components
    - **layout.js**: Defines the root layout for the entire application, providing a consistent structure and layout across all pages.
    - **page.js**: The homepage of your app.
    - **styles/**: Contains your global and modular CSS files.
      - **fonts/**: Contains your global font files.
      - **globals.css**: Global styles for your app.
      - **Home.module.css**: Module-specific styles for the homepage.
- **.eslintrc.json**: ESLint configuration for linting and code quality.
- **.gitignore**: Specifies which files and folders should be ignored by Git.
- **.env.local**: Contains environment variables for local development.
- **next.config.js**: Next.js configuration file.
- **package.json**: Contains project metadata and dependencies.
- **package-lock.json**: Auto-generated file that records the exact versions of installed dependencies.
- **postcss.config.mjs**: Configuration file for PostCSS (required for Tailwind CSS integration).
- **tailwind.config.js**: Configuration file for Tailwind CSS, for customizing the default theme and plugins.




## TASK 5. IMPROVE FRONTEND ARCHITECTURE 

- To improve the frontend architecture for production, will be using a combination of the React Server Components (RSC) architecture with Container and Presentational components best practises. 
-  React Server Components architecture will identify components that require interactivity and mark them as client components and keep sensitive data and business logic and mark them as server components
- Create distinct Container and Presentational components for each major feature in your app. Container Components (Server Components), Presentational Components (Client Components).
- Container components focus on data fetching, state management, and business logic, implement these as server components (.server.js)
- Presentational components are purely UI-focused, receiving data and callbacks via props, implement these as client components (.client.js)



### Step 1: Create the Navigation Component

1. In the Component folder `src/app/components/` create a **JSX** file called **"Navigation.client"** `src/app/components/Navigation.client.jsx`. Copy the code below
- The 'use client' directive marks this as a Client Component, enabling client-side interactivity

```javascript

'use client';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

export default function Navigation() {
  const router = useRouter();
  return (
    <nav>
      <Link href="/pages/login">Login</Link>
      <Link href="/">Home</Link>
      <Link href="/pages/about">About</Link>
    </nav>
  );
}

``` 


### Step 2: Create a Footer Component

1. In the Component folder `src/app/components/` create a **JSX** file called **"Footer.client"** `src/app/components/Footer.client.jsx`. Copy the code below


```javascript
'use client';

import styles from '../styles/Home.module.css'

export default function Footer() {
  return (
    <footer className={styles.footer}>
            <a
                href="https://nextjs.org"
                target="_blank"
                rel="noopener noreferrer"
            >
                Powered by Next.js
            </a>
        </footer>
  );
}

``` 

### Step 2: Update the Root Layout

1. Modify the Layout file `src/app/layout.js` to provide navigation bar across all pages
- import the Navigation from Components 

```javascript 
import './styles/globals.css';
import Navigation from './components/Navigation.client';

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`antialiased`}>
        <Navigation />
        {children}
      </body>
    </html>
  );
}
```



### Step 3: Update the Home Pag(Page.js)

1. Update the Page file `` by removing the Footer from the bottom. 

```javascript 
import styles from './styles/Home.module.css'
import Head from 'next/head'
import UserList from './components/UserList';

export default function Home() {
    return (
    <div className={styles.container}>
        <Head>
            <title>Base React Project</title>
            <meta name="description" content="A Next.js React application" />
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className={styles.main}>
            <h1 className={styles.title}>
                Welcome to Base React Project!
            </h1>
            <br/>
            <p className={styles.description}>
                Get started by editing{' '}
                <code className={styles.code}>src/app/page.js</code>
            </p>
            <br/>
            <UserList/>
        </main>
       
    </div>
    )
}
```

### Step 4: Create the About Page

1. In the App folder `src/app`  create a new folder called  **"Pages"** `src/app/pages`
2. In the Pages folder `src/app/pages`  create a new folder called  **"About"** `src/app/pages/about`
3. In the About folder ``src/app/about``  create a **JSX** file called **"Page"** `src/app/pages/about/page.jsx` and a another **JSX** file called **"About.client"** `src/app/pages/about/About.client.jsx`. Copy the code below:
- The `src/app/pages/about/page.jsx` is for routing to the about page using NextJs Page Router. 
- The  `src/app/pages/about/About.client.jsx` holds the about page UI component. 
- This separates the server-side container (page.js) from the client-side presentation (About.client.js).


`src/app/pages/about/page.jsx`
```javascript 
import About from './About.client';

export default function AboutPage() {
  return <About />;
}

```


`src/app/pages/about/About.client.jsx`
```javascript 
'use client';

export default function About() {
  return (
    <div>
      <h1>About Us</h1>
      <p>This is the about page content.</p>
    </div>
  );
}

```


### Step 5: Create the Login Page

1. In the Pages folder `src/app/pages`  create a new folder called  **"Login"** `src/app/pages/login`
2. In the About folder `src/app/login`  create a **JSX** file called **"Page"** `src/app/pages/login/page.jsx` and a another **JSX** file called **"About.client"** `src/app/pages/about/Login.client.jsx`. Copy the code below:
- The `src/app/pages/login/page.jsx` is for routing to the about page using NextJs Page Router. 
- The  `src/app/pages/about/Login.client.jsx` holds the about page UI component. 
- This separates the server-side container (page.js) from the client-side presentation (About.client.js).


`src/app/pages/login/page.jsx`
```javascript 
import { cookies } from 'next/headers';
import Login from './Login.client';

export default function LoginPage() {
  const cookieStore = cookies();
  const token = cookieStore.get('token');

  return <Login initialToken={token?.value} />;
}

```


`src/app/pages/about/Login.client.jsx`
```javascript 
'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function Login({ initialToken }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Implement login logic here
    router.push('/');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />
      <button type="submit">Login</button>
    </form>
  );
}

```


### Step 6: Create API Routes using Nextjs Routes

- Aim is to improve the API Endpoint route to connect to our Django backend 
- Will be modifying the API folder and file Structure to use the the api routes
- A basic handling of tokens and cookies 


1. In the User folder inside Api `src/app/api/` rename the file **axios** to **"fetchApi"** `src/app/api/fetchApi.js`. Copy the code below:
- Will now act as middleware between your Next.js frontend and Django backend, handling tokens/cookies and API requests.
- Reads the token from cookies for each request.
- Sends the token to the Django backend 
- Sets/updates the token in cookies 

```javascript 
import { cookies } from 'next/headers';

const DJANGO_API_URL = process.env.DJANGO_ENV_API_URL || 'http://localhost:8001/api/' || 'http://127.0.0.1:8001/api/';


export default async function fetchApi(endpoint, options = {}) {
  const cookieStore = cookies();
  const token = cookieStore.get('token');

  const headers = {
    'Content-Type': 'application/json',
    ...(token && { 'Authorization': `Bearer ${token.value}` }),
    ...options.headers
  };

  try {
    const response = await fetch(`${DJANGO_API_URL}${endpoint}`, {
      ...options,
      headers,
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    // Set or update token if it's in the response
    if (data.token) {
      cookies().set('token', data.token, { 
        httpOnly: true, 
        secure: process.env.NODE_ENV === 'production'
      });
    }

    return data;
  } catch (error) {
    console.error("Fetch error:", error);
    throw error;  
  }
}

```


2. In the User folder inside APi `src/app/api/users/`  create a file called **"Route"** `src/app/api/users/route.js`. Copy the code below:
- This will replace our `userListApi.js` and `userCreateApi.js`
- Now we are using NextJS App Router when you make a fetch request to , `http://localhost:8001/api/` you're not directly calling/importing the route.js file. 
- Instead, you're making a request to a URL path.
- Next.js intercepts this request. It looks at the URL path ('/api/users') and maps it to files in your project structure.
- Next.js will finds the **Route** file `app/api/users/route.js`. This file exports functions that correspond to HTTP methods (GET, POST, etc.)



```javascript
import { NextResponse } from 'next/server';
import fetchApi from '../fetchApi';

export async function GET() {
    try {
      const data = await fetchApi('users/');
      return NextResponse.json(data);
    } catch (error) {
      console.error("Error fetching users:", error);
      return NextResponse.json(
        { message: 'Failed to fetch users', error: error.message },
        { status: 500 }
      );
    }
}
  
export async function POST(request) {
    try {
      const body = await request.json();
      const data = await fetchApi('users/', {
        method: 'POST',
        body: JSON.stringify(body),
      });
      return NextResponse.json(data, { status: 201 });
    } catch (error) {
      console.error("Error creating user:", error);
      return NextResponse.json(
        { message: 'Failed to create user' },
        { status: 500 }
      );
    }
  }
```

3. Remove the **userListApi** file `src/app/api/users/userListApi.js`. and remove the **userCreateApi** file.  `src/app/api/users/userCreateApi.js`
- Will be removing these files as both these functions are now being covered in the **Route** file. 




4. We'll now integrating the new API User `route.js` with your existing **UserList** Component `src/app/components/UserList.js`
- First lets rename the `UserList.js` to `UserList.client.jsx`. 
- Now lets update the UserList.client.jsx file to use the new API routes. Replace the existing Userlist code with the code below:

```bash
UserList.client.jsx
```

- As you will see in the **fetchUsers** andd **createUser** functions. The **await fetch('/api/users')** you're not directly calling any file. Instead, you're making a request to a URL path. 
- When you make a GET request to '/api/users', Next.js automatically calls the exported GET function in your route.js file.
- Similarly, when you make a POST request to '/api/users', Next.js calls the exported POST function in route.js.


```javascript 
'use client';

import { useState, useEffect } from 'react';

export default function UserList() {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({ first_name: '', last_name: '', email: '' });
  const [isLoading, setIsLoading] = useState(false);
  const [createIsLoading, setCreateIsLoading] = useState(false);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    setIsLoading(true);
  
    try {
      const response = await fetch('/api/users');
      console.log({response});
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Failed to fetch users');
      }
      const data = await response.json();
      setUsers(data);
    } catch (err) {
      console.error("Error fetching users:", err);
      setUsers([]);
      // Optionally set an error state here to display to the user
    } finally {
      setIsLoading(false);
    }
  };

  const createUser = async () => {
    setCreateIsLoading(true);
    try {
      const response = await fetch('/api/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newUser),
      });
      if (!response.ok) {
        throw new Error('Failed to create user');
      }
      setNewUser({ first_name: '', last_name: '', email: '' });
      fetchUsers(); // Refetch users after creating a new one
    } catch (err) {
      console.error(err);
    } finally {
      setCreateIsLoading(false);
    }
  };

  const handleInputChange = (e) => {
    setNewUser({ ...newUser, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    createUser();
  };

  return (
    <div>
      <h2>User List</h2>
      {isLoading ? (
        <p>Loading users...</p>
      ) : users.length > 0 ? (
        <ul>
          {users.map((user) => (
            <li key={user.id}>
              {user.first_name} {user.last_name} - {user.email}
            </li>
          ))}
        </ul>
      ) : (
        <>
        <br/>
        <p>User List Pending...</p>
        </>
      )}
      <br/>

      <h3>Add New User</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="first_name"
          value={newUser.first_name}
          onChange={handleInputChange}
          placeholder="First Name"
          required
        />
        <input
          type="text"
          name="last_name"
          value={newUser.last_name}
          onChange={handleInputChange}
          placeholder="Last Name"
          required
        />
        <input
          type="email"
          name="email"
          value={newUser.email}
          onChange={handleInputChange}
          placeholder="Email"
          required
        />
        <button type="submit" disabled={createIsLoading}>
          {createIsLoading ? 'Creating...' : 'Add User'}
        </button>
      </form>
    </div>
  );
}
```


### Updated Project Folder Structure Frontend 4.

If everything was set up correctly, your project folder structure should look like this:

```markdown
C: interface.
├───.next
├───node_modules
└───src
    └───app
        ├───api
        │   └───users
        ├───components
        ├───about
        ├───login
        └───styles
            └───fonts
```

**Folder and File Breakdown:**

- **node_modules/**: Contains all the dependencies for your project.
- **src/**: Contains your application source code.
  - **app/**: Where you define your routes and pages.
    - **api/**: Contains API-related files and functions.
      - **fetchApi.js**: Central utility for making API requests to the Django backend.
      - **users/**: User-specific API routes.
        - **route.js**: Handles user-related API requests (GET, POST, etc.).
    - **components/**: Reusable React components.
      - **UserList.client.jsx**: Client component for displaying and managing users.
    - **about/**: About page related files.
      - **page.js**: Server component for the About page.
      - **About.client.jsx**: Client component for the About page content.
    - **login/**: Login page related files.
      - **page.js**: Server component for the Login page.
      - **Login.client.jsx**: Client component for the Login form.
    - **layout.js**: Defines the root layout for the entire application.
    - **page.js**: The homepage of your app.
    - **styles/**: Contains your global and modular CSS files.
      - **fonts/**: Contains your global font files.
      - **globals.css**: Global styles for your app.
      - **Home.module.css**: Module-specific styles for the homepage.
- **.eslintrc.json**: ESLint configuration for linting and code quality.
- **.gitignore**: Specifies which files and folders should be ignored by Git.
- **.env.local**: Contains environment variables for local development.
- **next.config.js**: Next.js configuration file.
- **package.json**: Contains project metadata and dependencies.
- **package-lock.json**: Auto-generated file that records the exact versions of installed dependencies.
- **postcss.config.mjs**: Configuration file for PostCSS (required for Tailwind CSS integration).
- **tailwind.config.js**: Configuration file for Tailwind CSS, for customizing the default theme and plugins.







## TASK 6: ADD FRONTEND AND BACKEND REPOSITORIES TO GITHUB

### Step 1: Improve Enviroment Variables and Configurations Frontend(NextJS)


1. Inside the root directory change the name of the `.env.local` file to **".env"** remove the **.local** 
- This will allow us to begin to use this in production enviroment. 

2. In the .env.local file in the root of your Next.js project, will update the end point for your django backend.
- From **DJANGO_ENV_API_URL** to **"DJANGO_BASE_URL"** .

```bash
DJANGO_BASE_URL=http://localhost:8001/
```


3.  Inside our SRC folder `src` create a folder called **"Config"** and inside that Config folder `src/config` create a file called **"Defaults"**  `src/config/defaults.jsx`
- This will now be the enviroment there you will access the endpoints from instead of directly from the  .env.local file 

```javascript
export const DJANGO_BASE_URL=process.env.DJANGO_BASE_URL
export const DJANGO_API_ENDPOINT=`${DJANGO_BASE_URL}/api/`
export const DJANGO_API_ENDPOINT_LOCAL = 'http://localhost:8001/api/' || 'http://127.0.0.1:8001/api/'
```

4.  Inside the root directory  `next.config.js` update the enviroment variable by importing the default config file. Copy and replace with the code below:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${process.env.DJANGO_BASE_URL}/:path*`,
      },
    ];
  },
};

module.exports = nextConfig;
```

5.  Inside the Api folder `src/app/api/` update the fetchApi file `src/app/api/fetchApi.js`. 
- Import the default config file **DJANGO_API_ENDPOINT** and **DJANGO_API_ENDPOINT_LOCAL** from  `import {DJANGO_API_ENDPOINT} from "@/app/config/defaults"`
- Copy and replace the **DJANGO_API_URL** with the code below :

```javascript

import { cookies } from 'next/headers';
import {DJANGO_API_ENDPOINT, DJANGO_API_ENDPOINT_LOCAL} from "@/app/config/defaults" 

const DJANGO_API_URL = DJANGO_API_ENDPOINT || DJANGO_API_ENDPOINT_LOCAL

```


### Step 2: Improve Enviroment Variables and Configurations Backend(Django)

1. Open back up your Backend project and inside the root directory create a **".env"** file. Copy the code below:

```bash
DJANGO_SECRET_KEY='DJANGO_SECRET_KEY'
DJANGO_DEBUG=1
CORS_ALLOWED_ORIGINS="http://localhost:3000,http://127.0.0.1:3000",

```

2. Inside the Core folder `datastore/src/core/`, Replace the content of the Settings file `datastore/src/core/settings.py`. With the code below:
- Will be updating the **SECRET_KEY**, **DEBUG** and **CORS_ALLOWED_ORIGINS** to use the enviroment variables using/importing the libabry ***decouple*** 
- The **CORS_ALLOWED_ORIGINS** will perform a method to decouple the string in the .env file 


```python
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str)

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)


ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

CORS_ALLOWED_ORIGINS = []
ENV_CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=str, default="")
for origin in ENV_CORS_ALLOWED_ORIGINS.split(","):
    CORS_ALLOWED_ORIGINS.append(f"{origin}".strip().lower())

```


3. To get your own **SECRET_KEY**  in the terminal write the command  python -c "import secrets;print(secrets.token_urlsafe(54))"
- This will give you a new secert key.

```bash
python -c "import secrets;print(secrets.token_urlsafe(54))"
```


4. Copy your secret key to your .env file and update your **DJANGO_SECRET_KEY** 
- Should look something like this below:

```bash
DJANGO_SECRET_KEY=vq0Ey5FbPdC2Zl54kJ5jkgdJ0SsqcdPwwWj4bWYM9jTfUdJ5gu8kH9C_h3g23rww22a
```




### Step 3: Initialise Git for Backend Project
1. Lets start with the backend, open your terminal in VS Code.
2. Make sure you are at the  root directory of your project called **Datastore**:
3. Initialise a new Git repository:

```bash
git init
```

Create a `.gitignore` in the root directory and copy the content below:

```.gitignore
# Python
__pycache__/
*.py[cod]

# Django
*.log
*.pot
*.pyc
db.sqlite3
media/

# Environments
.env
.venv
env/
venv/

# IDE
.vscode/
.idea/

# OS generated files
.DS_Store
Thumbs.db
```

4. Add Your Files to the Staging Area
Add all your files to the staging area:
```bash
git add .
```
*The `.` indicates that you want to add all files in the current directory.*

5. Commit your changes with a descriptive message:
```bash
git commit -m "Initial commit"
```

6. *** Create a New Repository on GitHub *** 
  1. Go to GitHub and log in to your account.
  2. Click the "+" icon in the upper right corner and select **New repository**.
  3. Name your repository (e.g., `base_datastore`).
  4. Optionally, add a description.
  5. Choose whether the repository should be public or private.
  6. **Do not** initialise the repository with a README, `.gitignore`, or license (since you already have files in your local repo).
  7. Click **Create repository**.

7.  Link Your Local Repository to GitHub
In your terminal, link your local repository to the newly created GitHub repository. Replace `<USERNAME>` with your GitHub username and `<REPOSITORY_NAME>` with the name of your repository:

```bash
git remote add origin https://github.com/<USERNAME>/<REPOSITORY_NAME>.git
```
*Example:*
```bash
git remote add origin https://github.com/johndoe/base_datastore.git
```

8. Push Your Code to GitHub
Push your local commits to GitHub:

```bash
git push -u origin master
```

### Step 4: Initialise Git for Frontend Project

1. Now the Frontend, open your terminal in VS Code for the frontend project.
2. Make sure you are at the root directory of your project called **Interface**:
3. Initialise a new Git repository:

```bash
git init
```

Create a `.gitignore` in the root directory and copy the content below:

```.gitignore
# Dependencies
/node_modules

# Next.js
/.next/
/out/

# Production
/build

# Debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Local env files
.env*.local

# Misc
.DS_Store
*.pem
```

4. Add Your Files to the Staging Area
Add all your files to the staging area:
```bash
git add .
```
*The `.` indicates that you want to add all files in the current directory.*

5. Commit your changes with a descriptive message:
```bash
git commit -m "Initial commit"
```

6. *** Create a New Repository on GitHub *** 
  1. Go to GitHub and log in to your account.
  2. Click the "+" icon in the upper right corner and select **New repository**.
  3. Name your repository (e.g., `base_interface`).
  4. Optionally, add a description.
  5. Choose whether the repository should be public or private.
  6. **Do not** initialise the repository with a README, `.gitignore`, or license (since you already have files in your local repo).
  7. Click **Create repository**.

7.  Link Your Local Repository to GitHub
In your terminal, link your local repository to the newly created GitHub repository. Replace `<USERNAME>` with your GitHub username and `<REPOSITORY_NAME>` with the name of your repository:

```bash
git remote add origin https://github.com/<USERNAME>/<REPOSITORY_NAME>.git
```
*Example:*
```bash
git remote add origin https://github.com/johndoe/base_datastore.git
```

8. Push Your Code to GitHub
Push your local commits to GitHub:

```bash
git push -u origin master
```



### TASK 6 COMPLETE: FRONTEND AND BACKEND ARE UPLOAD TO GITHUB.


## TASK 7:  DEPOLY FRONTEND AND BACKEND TO RAILWAY 



Authentication Helper (src/lib/auth.js):

```javascript

import { cookies } from 'next/headers';

export function getToken() {
  const cookieStore = cookies();
  return cookieStore.get('token')?.value;
}

export function setToken(token) {
  cookies().set('token', token, { httpOnly: true, secure: process.env.NODE_ENV === 'production' });
}

```












































































2. ***Commit django***  
- Head back to the root directory `Base_Project_Template` 
- Perform a git commit to save your django folders and files:
```bash
  cd ..
  git add .
  git commit -m "add django"
  git push -u origin master
```


### Step 4: Make Django Migrations and Run the server

1. ***Run migrations *** 
- Head back into your datastore directory `Base_Project_Template/datastore` 
- Then run makemigrations and then run migrate in the terminal
-  **makemigrations** Detects changes in your models (added, modified, or deleted fields).
   Creates new migration files based on these changes.
   It doesn't change your database, just prepares the instructions.
-  **migrate** Applies the pending migrations to your database, 
   Executes the SQL commands to modify your database schema
   Keeps track of which migrations have been applied
   Ensures your database schema matches the current state of your models
```bash
cd datastore 
python manage.py makemigrations
python manage.py migrate
```


















Local Development
For local development, you'll need to run both servers:
Django: python manage.py runserver (runs on http://localhost:8000)
Next.js: npm run dev (runs on http://localhost:3000)

Will need to set up a proxy in your Next.js development server to forward API requests to Django.


Next.js API Configuration
In your Next.js app, when making API calls to your Django backend, use a base URL that includes /api/:
javascript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000/api';

// Example API call
const response = await fetch(`${API_URL}/users/`);








2. **Commit database updates**  
Before heading into the database folder lets commit your changes
Perform a git commit to save your environment changes:
```bash
  git add .
  git commit -m "Add database"
  git push -u origin master
```


6. **Add Environment Variables in Vercel** 
   - Copy the `POSTGRES_URL=postgress...`  and head back Vercel
   - Go into your project and click **Settings**
   - On the sidebar to the left find and click **Environment Variables**

   In Vercel, paste the key-value pair as shown below (replace with actual credentials later):

``` js
   | Key           |  Value                                               |
   |---------------|------------------------------------------------------|
   | POSTGRES_URL  | postgres://username:password@localhost:5432/mydb_dev |

```















## Step 14: While developing  

Update next.config.mjs to the code below

``` js
/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    typescript: {ignoreBuildErrors: true},
    eslint: {ignoreDuringBuilds: true}
  };

export default nextConfig;
```

In the package.json update the script dev commond to  -- turbo like below, This will improve build time during development 

``` json
 "scripts": {
    "dev": "next dev --turbo",

 }
```


### New Folder File Structure

After implementing the above steps, the folder structure for the Frontend should look like this:



C:interface.
├───.next
├───node_modules
└───src
    └───app
        ├───api
        │   └───users
        ├───components
        └───styles
            └───fonts




















