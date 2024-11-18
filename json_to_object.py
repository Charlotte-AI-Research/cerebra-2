"""
{
 "event_details": {
   "event_name": "",
   "event_location": "",
   "start_date": "",
   "start_time": "",
   "end_date": "",
   "end_time": "",
   "event_description": "",
   "event_purpose": "",
   "benefit_to_community": "",
   "expected_total_attendance": {
     "unc_charlotte_students": 0,
     "all_others": 0
   },
   "expected_student_attendance": 0,
   "open_to_all_students": true,
   "charge_for_attendance": false
 },
 "budget_request": {
   "contracted_services": [
     {
     "total_requested_amount": 0
     "items":[{
     "amount_requested":0,
     "description": "Printed items such as programs, posters, flyers, etc.",
     "vendor": {
           "name": "Union Station or Repros",
           "quote": 10
         }
   }]
   }
 ],
   "printing": {
     "total_requested_amount": 0,
     "items":[{
     "amount_requested":0,
     "description": "Printed items such as programs, posters, flyers, etc.",
     "vendor": {
           "name": "Union Station or Repros",
           "quote": 10
         }
   }],

   "advertising": {
     "total_requested_amount": 0,
     "items":[{
     "description": "Marketing or advertising expenses including social media, publications, etc.",
     "vendor": {
           "name": "",
           "quote": ""
         }
     }]
   },

   "space_equipment": {
     "total_requested_amount": 0,
     "description": "Reserved University spaces, services, technicians, or equipment.",
     "requested_items": {
       "space_facility_rental": false,
       "equipment_rental": false,
       "technicians_staff": false
     }
   },


   "program_supplies": {
     "total_amount_requested": 0,
     "items":[{
     "amount_requested": 0,
     "description": "Supplies crucial to the event's success, items from outside vendors.",
     "note": "Items cannot be sold or destroyed, must be stored in SAFC."
   }]
   },

   "food_beverage": {
     "total_amount_requested": 0,
     "items":[{
     "amount_requested": 0,
     "description": "Food and beverage expenses, must be ordered through Chartwells.",
     #"limit_note": "Cannot exceed half of the overall budget."
   }],


   "total_budget": 0,
   "budget_limit_note": "Must not exceed $2,500 for a single event or $4,000 for joint events."
 }
}
"""
import json

from generation.generate import create_justification


class Event:
    def __init__(self):
        self.event_name:str = None
        self.event_location: str = None
        self.start_date: str = None
        self.start_time: str = None
        self.end_date: str = None
        self.end_time: str = None
        self.event_description: str = None
        self.event_purpose: str = None
        self.benefit_to_community: str = None
        self.items_requested: list = None
        self.total_budget: float = 0.00

    def calculate_total_costs(self):
        print(55)

    def create_justifications(self):
        for item in self.items_requested:
            catagory = item.catagory
            event_description = self.event_description
            for subitem in item.sub_items:
                justification: str = create_justification(catagory, event_description, subitem)
                item.justification+= justification + " "

    def to_json(self)-> dict:
        json = {}
        #alert user that certain catagories are empty!
        return json

    def from_json(self,obj):
        object = load(obj)
        self(*object)

    def from_file_json(self,file_location):
        obj = open(file_location)
        object = load(obj)
        self(*object)

class Item:
    def __init__(self):
        self.catagory = ""
        self.cost = 0.00
        self.sub_items = [] #"Sweet Tea, "Hamburger Box Qt 24, ..."
        self.vendor = ""
        self.justification = "" # We need to create a justification for each item in the items list



event1 = Event()
event1.event_name = "CAIR General Body Meeting 2"
