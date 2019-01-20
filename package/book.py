from flask_restful import Resource, Api, request
from package.model import conn
from pyfingerprint.pyfingerprint import PyFingerprint
import package.fingerprint_search as fsearch


class BookAppointment(Resource):
    def get(self):
        """Api to retive all the patient from the database"""
        fingerprint_id = fsearch.search()
        patients = conn.execute("SELECT * FROM patient  where pat_fingerprint_id = ?",(fingerprint_id,)).fetchall()
        return patients