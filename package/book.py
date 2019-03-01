from flask_restful import Resource, Api, request
from package.model import conn
from pyfingerprint.pyfingerprint import PyFingerprint
import package.fingerprint_search as fsearch
import json

class BookAppointment(Resource):
    def get(self):
        """Api to retive all the patient from the database"""
        fingerprint_id = fsearch.search()
        patients = conn.execute("SELECT pat_id FROM patient  where pat_fingerprint_id = ?",(fingerprint_id,)).fetchall()
        #pat = json.loads(patients[0])
        print type(patients[0])
        idnew =  str(patients[0]['pat_id'])
        appointment = conn.execute('''INSERT INTO appointment(pat_id) VALUES(?)''', (idnew)).lastrowid
        conn.commit()
        return appointment