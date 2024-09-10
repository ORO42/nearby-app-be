from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str | None = None
    bio: str | None = None

    job_title: str | None = None
    company: str | None = None

    is_paused: bool = False
    location_radius_ft: int = 10000

    instagram_link: str | None = None
    meta_link: str | None = None
    tiktok_link: str | None = None
    personal_website_link: str | None = None
    behance_link: str | None = None
    dribbble_link: str | None = None
    medium_link: str | None = None
    x_link: str | None = None
    youtube_link: str | None = None
    pinterest_link: str | None = None
    linkedin_link: str | None = None
    twitch_link: str | None = None

    user_details_completed: bool = False
    user_interests_completed: bool = False
    user_job_completed: bool = False


class UserUpdate(BaseModel):
    name: str | None = None
    bio: str | None = None

    job_title: str | None = None
    company: str | None = None

    is_paused: bool = False
    location_radius_ft: int = 10000

    instagram_link: str | None = None
    meta_link: str | None = None
    tiktok_link: str | None = None
    personal_website_link: str | None = None
    behance_link: str | None = None
    dribbble_link: str | None = None
    medium_link: str | None = None
    x_link: str | None = None
    youtube_link: str | None = None
    pinterest_link: str | None = None
    linkedin_link: str | None = None
    twitch_link: str | None = None

    user_details_completed: bool = False
    user_interests_completed: bool = False
    user_job_completed: bool = False


class UserInDB(BaseModel):
    id: str

    name: str
    bio: str | None = None

    job_title: str | None = None
    company: str | None = None

    is_paused: bool = False
    location_radius_ft: int = 10000

    instagram_link: str | None = None
    meta_link: str | None = None
    tiktok_link: str | None = None
    personal_website_link: str | None = None
    behance_link: str | None = None
    dribbble_link: str | None = None
    medium_link: str | None = None
    x_link: str | None = None
    youtube_link: str | None = None
    pinterest_link: str | None = None
    linkedin_link: str | None = None
    twitch_link: str | None = None

    user_details_completed: bool = False
    user_interests_completed: bool = False
    user_job_completed: bool = False

    class Config:
        from_attributes = True
