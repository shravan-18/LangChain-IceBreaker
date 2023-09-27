import os
import requests
import json

PROXYCURL_API_KEY = "8DzPi_mRUz3L2RVZsnJeyQ"
json_file_path = "D:\VIT Material\VIT material\Courses\Langchain\Github\ice_breaker\\third_parties\data.json"


def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape info from LinkedIn profiles,
    Manually scrapt the info from the LinkedIn profile"""

    # Don't uncomment this until final try
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f"Bearer {PROXYCURL_API_KEY}"}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()

    """# Open the JSON file and load its contents into a Python variable
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")"""

    return data
