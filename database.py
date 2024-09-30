import sqlalchemy 
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv() 
db_connection_string = os.getenv('DB_CONNECTION_STRING')
engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        
        for row in result:
            # Use _mapping to convert each row into a dictionary
            jobs.append(dict(row._mapping))
        
        return jobs
    

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id} ;"))
    rows = result._allrows()
  if len(rows) == 0:
    return None
  else:
    return rows[0]._mapping


       
    
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url )")
        
        conn.execute(query, job_id = job_id,
                     full_name = data['full_name'],
                     email = data['email'],
                     linkedin_url = data['linkedin_url'],
                     education = data['education'],
                     work_experience = data['work_experience'],
                     resume_url = data['resume_url']
                    )
 
#code trial
# def add_application_to_db(job_id, data):
#     try:
#         with engine.connect() as conn:
#             query = text("""
#                 INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
#                 VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
#             """)
#             conn.execute(query, 
#                          job_id=job_id,
#                          full_name=data['full_name'],
#                          email=data['email'],
#                          linkedin_url=data['linkedin_url'],
#                          education=data['education'],
#                          work_experience=data['work_experience'],
#                          resume_url=data['resume_url'])
#     except Exception as e:
#         print(f"Error adding application: {e}")  # Print the error for debugging
 
       
def see_applicants():
  with engine.connect() as conn:
    result = conn.execute(text("select * from applications"))
    result_dicts = []
    for row in result._allrows():
      result_dicts.append(dict(row._mapping))

    return result_dicts   

def add_job_to_db(data):
    with engine.connect() as conn:
        query = text("INSERT INTO jobs (id, title, location, salary, currency, responsibilities, requirements) VALUES (:id, :title, :location, :salary, :currency, :responsibilities, :requirements)")
        
        conn.execute(query, id=data['id'],
                     title=data['title'], 
                     location=data['location'], 
                     salary=data['salary'],
                     currency=data['currency'], 
                     responsibilities=data['responsibilities'], 
                     requirements=data['requirements'])
               
        