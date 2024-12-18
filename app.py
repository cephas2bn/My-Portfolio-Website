import os
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
import requests

app = Flask(__name__)
app.secret_key = "portfolio_secret"

# Flask-Mail Configuration (Using Gmail as an example)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # SMTP server for Gmail
app.config['MAIL_PORT'] = 587                # Port for secure TLS connections
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'cephasfn@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'ycku omvh yiqn nzni'         # generate app password with

mail = Mail(app)

@app.route("/")
def home():
   # Work experience data
    work_experience = [
        {
            "title": "Safety ANd Security Monitor",
            "company": "Eastern Health, Health Science Center",
            "location": "St John's, Newfoundland, Canada",
            "date": "January 2024 – Present",
            "description": "Patient healthcare Support planning.",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "title": "Mine GIS and Database Manager",
            "company": "Managem Group Ltd.",
            "location": "SMM Tri-K Mine, Guinea",
            "date": "April 2020 – August 2023  · 3 yrs 8 months",
            "description": "Led GIS and database management for mining projects, optimizing database structures and improving resource planning.",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "title": " GIS and Database Engineer",
            "company": "Ghana Manganese Company (GMC)",
            "location": "Nsuta Mine,  Tarkwa, Ghana, West Africa",
            "date": "September 2016 – April 2020 · 4 yrs 7 months",
            "description": "Provides GIS support to Mine Geology Department and Manage database on a daily basis.",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "title": " GIS Intern",
            "company": "Aberdeen City Council",
            "location": "Aberdeen, United Kingdom",
            "date": "July 2015 - September 2015 · 3 months",
            "description": "Accelerate Aberdeen Project: To create a smart and responsive web mapping platform that will support planning and decision making, and create opportunities for smarter investments within the city of Aberdeen.",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "title": " Assistant GIS Specialist",
            "company": "Global Communities Ghana",
            "location": "Takoradi, Ghana",
            "date": "November 2013 - February 2014 · 4 mos",
            "description": "Using ArcGIS 10.1 to Manage Property Information in the Sekondi-Takoradi Metropolis, Captrure New Data for the Street Naming Project In STMA, Updating Property records in the SNPA System",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "title": " Assistant Lecturer, Civil Eng Dept",
            "company": "Sunyani Technical University - STU",
            "location": "Sunyani, Ghana",
            "date": "September 2012 - August 2013 · 1 year",
            "description": "Teaching assistant for 1. Principles of surveying 2. Building Mathematics 3. Instructor for Construction Survey 4. Engineering Surveying for Civil Eng.",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        }
    ]

    # Education data
    education = [
        {
            "degree": "Master of Data Science (MDSC)",
            "institution": "Memorial University of Newfoundland",
            "location": "St John's, NL",
            "year": "Graduated September 2024",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "degree": "M.Sc. Geographical Information Systems (GIS)",
            "institution": "University of Aberdeen",
            "location": "Aberdeen, United Kingdom",
            "year": "2014 – 2015",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "degree": "B.Sc. Geomatic Engineering",
            "institution": "University of Mines and Technology (UMaT)",
            "location": "Tarkwa, Ghana",
            "year": "2008 – 2012",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        }
    ]

    # Skills data
    skills = [
        "Python Programming", "Machine Learning", "Database Management",
        "GIS Software: ESRI ArcGIS, QGIS", "Data Visualization: Power BI, Excel",
        "Cloud Services: Microsoft Azure, AWS", "Spatial Data Analysis",
        "R Programming", "Deep Learning", "Reinforcement Learning", "Feature Engineering",
        "Natural Language Processing (NLP)", "Computer Vision", "Predictive Modeling",
        "Hypothesis Testing", "Experimental Design", "Statistical Data Analysis", "Multivariate Statistics", 
        "Big Data", "Data Mining", "Data Analysis", "Data Privacy", "Data Manipulation",
        "Optimization", "Oracle Database", "Database Design", "Database Administration",
        "GIS Implementation", "GIS Products", "Remote Sensing", "Spatial Analysis",
        "Geostatistics", "Spatial Data Management", "Geographic Information Systems (GIS)",
        "Geographic Information Science", "GPS (Global Positioning Systems)",
         "Surveying", "Geological Mapping", "Mineral Exploration", "Client Requirements Analysis",
        "Mining", "Minerals",  "Environmental Awareness", "Problem Solving",
        "Project Management", "Strategic Planning", "Communication", "Teamwork", "Customer Service", 
        "Business Strategy", "Team Leadership", "Team Management", "Budgeting",
        "Supervisory Skills", "Negotiation", "Data Visualization: Tableau", "AutoCAD",
        "Microsoft Office (Word, Excel, PowerPoint)", "Azure Databricks"
    ]

    # Certifications data
    certifications = [
        {"name": "AWS Certified Cloud Practitioner", "date": "2023"},
        {"name": "Microsoft Azure Fundamentals", "date": "2022"}
    ]

    # Volunteer work
    volunteer_work = [
        {
            "role": "Science and Mathematics Teacher",
            "organization": "Dispensational Victory Academy",
            "location": "Inchaban, Ghana",
            "date": "June 2006 – July 2008 | 2 years 2 months",
            "description": "Volunteered to teach Mathematics and Science for the Junior High School."
        },
        {
            "role": "Pupil Teacher",
            "organization": "Dispensational Victory Academy",
            "location": "Inchaban, Ghana",
            "date": "Feb 2014 - Jul 2014 and  May 2009 – August 2009  10 Months",
            "description": "Volunteered to teach Mathematics and Science for the Junior High School during vacation periods."
        }
    ]

    #   recommendations
    recommendations = [
        {
            "name": "Francis Fosu, P.Geo",
            "title": "Exploration and Mineral Resource Manager at Ghana Manganese Company Ltd.",
            "text": "Cephas applies geoscience principles accurately and shows strong professional judgment...",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "name": "Dr. Ir. Raquel Serrano Calvo",
            "title": "Research Associate, Specialist in Earth Observation",
            "text": "Cephas has a dedicated attitude towards GIS and responsibility, discipline, and teamwork...",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "name": "Gordon Wright",
            "title": "Economic Development Specialist",
            "text": "Cephas interned with us on a GIS implementation for economic development, delivering above expectations...",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
        {
            "name": "Simon Peter Okyere",
            "title": "Surveyor at Nexxis Engineering Ltd",
            "text": "Cephas is a brilliant fellow in class and on project work, delivering accurate results...",
            "linkedin": "https://www.linkedin.com/in/cephasaforson/"
        },
    ]

    return render_template(
        "home.html",
        work_experience=work_experience,
        education=education,
        skills=skills,
        certifications=certifications,
        volunteer_work=volunteer_work,
        recommendations=recommendations
    )

@app.route("/projects")
def projects():
    github_username = "cephas2bn"
    url = f"https://api.github.com/users/{github_username}/repos"
    response = requests.get(url)
    projects = response.json()
    
    project_list = [
        {
            "name": "Financial Transaction Fraud Detection",
            "description": "A portfolio project demonstrating real-time fraud detection for financial transactions using machine learning.",
            "link": "https://github.com/cephas2bn/Financial_Transaction_Fraud_Detection",
        },
        {
            "name": "Credit Risk Assessment",
            "description": "Assessing credit client risks using data-driven machine learning models for decision-making.",
            "link": "https://github.com/cephas2bn/Credit_Risk_Assessment",
        },
        {
            "name": "Titanic Survival Prediction",
            "description": "A portfolio project predicting passenger survival on the Titanic using logistic regression.",
            "link": "https://github.com/cephas2bn/Titanic_Survival_Prediction",
        },
        {
            "name": "StartUp Profit Prediction",
            "description": "Predicting startup profits based on investment data using regression techniques.",
            "link": "https://github.com/cephas2bn/StartUpProfitPrediction",
        },
        {
            "name": "Healthcare Sentiment Analysis",
            "description": "A portfolio project analyzing healthcare sentiment using Python and machine learning.",
            "link": "https://github.com/cephas2bn/healthcare_sentiment_analysis",
        },
        {
            "name": "AI Document Bot",
            "description": "An AI-powered document question-answering system implemented with NLP techniques.",
            "link": "https://github.com/cephas2bn/AI_Document_Bot",
        }
    ]
    return render_template("projects.html", projects1=project_list, projects=projects)

# Route for the About Me Page
@app.route("/about")
def about():
    # Dynamically fetch all CV files in the 'static/files' directory
    files_folder = os.path.join(app.static_folder, "files")
    cv_files = [file for file in os.listdir(files_folder) if file.lower().endswith(('.pdf', '.docx'))]
    return render_template("about.html", cv_files=cv_files)

# Route for the Gallery Page
@app.route("/gallery")
def gallery():
    image_folder = os.path.join(app.static_folder, "images/gallery")
    images = [f"images/gallery/{file}" for file in os.listdir(image_folder) if file.endswith((".jpg", ".png", ".jpeg"))]
    return render_template("gallery.html", images=images)

# Route for the Contact Page

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message_content = request.form.get("message")

        # Create an email message
        subject = f"Message from {name} via Portfolio Contact Form"
        msg_body = f"Name: {name}\nEmail: {email}\nMessage:\n{message_content}"

        try:
            msg = Message(subject=subject,
                          sender=email,  # Reply-To email
                          recipients=["cephasfn@gmail.com"])  # Replace with your email
            msg.body = msg_body
            mail.send(msg)
            flash("Your message has been sent successfully!", "success")
            return redirect(url_for("contact"))
        except Exception as e:
            print(e)  # Log the error
            flash("An error occurred while sending your message. Please try again.", "danger")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

