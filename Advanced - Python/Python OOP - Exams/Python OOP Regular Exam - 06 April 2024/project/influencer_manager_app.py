from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    influencer_types = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }

    campaign_types = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    @staticmethod
    def find_object(value, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == value:
                return obj

        return None

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if not self.influencer_types.get(influencer_type):
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self.find_object(username, "username", self.influencers)
        if influencer:
            return f"{username} is already registered."

        self.influencers.append(self.influencer_types[influencer_type](username, followers, engagement_rate))
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if not self.campaign_types.get(campaign_type):
            return f"{campaign_type} is not a valid campaign type."

        campaign = self.find_object(campaign_id, "campaign_id", self.campaigns)
        if campaign:
            return f"Campaign ID {campaign_id} has already been created."

        self.campaigns.append(self.campaign_types[campaign_type](campaign_id, brand, required_engagement))
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.find_object(influencer_username, "username", self.influencers)
        campaign = self.find_object(campaign_id, "campaign_id", self.campaigns)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment <= 0:
            return

        campaign.approved_influencers.append(influencer)
        campaign.budget -= influencer_payment
        influencer.campaigns_participated.append(campaign)

        return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        output = {}
        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                output[campaign] = output.get(campaign, 0) + influencer.reached_followers(campaign.__class__.__name__)

        return output

    def influencer_campaign_report(self, username: str):
        influencer = self.find_object(username, "username", self.influencers)

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        total_reached_followers = self.calculate_total_reached_followers()
        sorted_campaigns = sorted(self.campaigns, key=lambda campaign: (len(campaign.approved_influencers), -campaign.budget))

        output = ["$$ Campaign Statistics $$"]
        for campaign in sorted_campaigns:
            append_data = (f"  * Brand: {campaign.brand}, "
                           f"Total influencers: {len(campaign.approved_influencers)}, "
                           f"Total budget: ${campaign.budget:.2f}, "
                           f"Total reached followers: {total_reached_followers[campaign]}"
                           )
            output.append(append_data)

        return "\n".join(output)
