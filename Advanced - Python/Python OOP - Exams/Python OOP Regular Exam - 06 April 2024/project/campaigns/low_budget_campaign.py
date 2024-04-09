from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    minimum_engagement_rate = 0.9

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, 2500.0, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * self.minimum_engagement_rate