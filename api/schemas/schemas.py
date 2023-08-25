from typing import Optional, Dict
from pydantic import BaseModel

class DetailsPersonProposedInsured(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[str] = None
    relationship_with_proposer: Optional[str] = None
    premium_tier: Optional[str] = None
    basic_sum_insured: Optional[str] = None

class UserDetails(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    age: Optional[str] = None
    gender: Optional[str] = None
    child: Optional[str] = None
    landmark: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    nationality: Optional[str] = None
    dob: Optional[str] = None
    marital_status: Optional[str] = None
    mobile_no: Optional[str] = None
    email_id: Optional[str] = None
    profession: Optional[str] = None
    eia_no: Optional[str] = None
    policy_type: Optional[str] = None
    policy_period: Optional[str] = None
    policy_period_from: Optional[str] = None
    policy_period_to: Optional[str] = None
    sum_insured: Optional[str] = None
    details_person_proposed_insured: Dict[str, DetailsPersonProposedInsured] = {}
    place: Optional[str] = None
    date: Optional[str] = None

    class Config:
        orm_mode = True
        # schema_extra = {
        #     "example": {
        #         "name": "John",
        #         "address": "123 Main St",
        #         "age": "30",
        #         "gender": "Male",
        #         "child": "Jane",
        #         "landmark": "Near Park",
        #         "city": "Cityville",
        #         "state": "Stateland",
        #         "pincode": "12345",
        #         "nationality": "Country",
        #         "dob": "1990-01-01",
        #         "marital_status": "Single",
        #         "mobile_no": "123-456-7890",
        #         "email_id": "john@example.com",
        #         "profession": "Engineer",
        #         "eia_no": "EIA123",
        #         "policy_type": "Health",
        #         "policy_period": "1 Year",
        #         "policy_period_from": "2023-01-01",
        #         "policy_period_to": "2023-12-31",
        #         "sum_insured": "100000",
        #         "details_person_proposed_insured": {
        #             "1": {
        #                 "name": "Jane",
        #                 "gender": "Female",
        #                 "dob": "1995-05-05",
        #                 "height": "5ft 6in",
        #                 "weight": "130 lbs",
        #                 "relationship_with_proposer": "Daughter",
        #                 "premium_tier": "Silver",
        #                 "basic_sum_insured": "50000"
        #             }
        #         },
        #         "place": "City",
        #         "date": "2023-08-25"
        #     }
        # }
