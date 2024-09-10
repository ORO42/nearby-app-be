from sqlalchemy import Boolean, Column, Integer, String
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)  # This will be the Auth0 user_id

    name = Column(String)
    bio = Column(String)

    job_title = Column(String)
    company = Column(String)

    is_paused = Column(Boolean, default=False)
    location_radius_ft = Column(Integer, default=10000)

    instagram_link = Column(String)
    meta_link = Column(String)
    tiktok_link = Column(String)
    personal_website_link = Column(String)
    behance_link = Column(String)
    dribbble_link = Column(String)
    medium_link = Column(String)
    x_link = Column(String)
    youtube_link = Column(String)
    pinterest_link = Column(String)
    linkedin_link = Column(String)
    twitch_link = Column(String)

    user_details_completed = Column(Boolean, default=False)
    user_interests_completed = Column(Boolean, default=False)
    user_job_completed = Column(Boolean, default=False)
