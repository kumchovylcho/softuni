from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    initial_payment_percentage = 0.45
    campaign_type_multipliers = {
        "HighBudgetCampaign": 1.2,
        "LowBudgetCampaign": 0.9
    }

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * self.initial_payment_percentage

    def reached_followers(self, campaign_type: str):
        return int((self.followers * self.engagement_rate) * self.campaign_type_multipliers[campaign_type])
