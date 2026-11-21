from managed_deepagents import define_deep_agent

from middleware.brand_lint import brand_lint
from tools.brand import get_brand
from tools.slack_tools import publish_design

agent = define_deep_agent(
    name="design-studio",
    model="google_genai:gemini-3.8-flash",
    tools=[get_brand, publish_design],
    interrupt_on={"publish_design": True},
    middleware=[brand_lint],
)

