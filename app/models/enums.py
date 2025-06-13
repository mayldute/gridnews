import enum


class UserRoleEnum(str, enum.Enum):
    user = 'user'
    admin = 'admin'


class NewsTypeEnum(str, enum.Enum):
    news = 'news'
    article = 'article'
    interview = 'interview'


class EventStatusEnum(str, enum.Enum):
    upcoming = 'upcoming'
    completed = 'completed'
    cancelled = 'cancelled'
