from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    minimum_engagement_rate = 1.2

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, 5000.0, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * self.minimum_engagement_rate