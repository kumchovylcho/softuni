from abc import ABC, abstractmethod


class BaseCampaign(ABC):
    unique_campaign_ids = set()

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers = []

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        if value <= 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")

        if value in self.unique_campaign_ids:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")

        self.unique_campaign_ids.add(value)
        self.__campaign_id = value

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass