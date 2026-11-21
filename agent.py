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
    subagents=[
        {
            "name": "critic",
            "description": (
                "Reviews one finished design against the brand guidelines and returns "
                "a short list of concrete fixes. Give it the design's file path and what it's for."
            ),
            "system_prompt": (
                "You are a senior brand designer reviewing one design. Read it with "
                "read_file: the PNG in /workspace/out/ if there is one, otherwise the SVG. "
                "Return only a numbered list of at most five concrete fixes, most "
                "important first, or 'No changes needed.' Don't redesign it or praise it."
            ),
            "tools": [get_brand],
            "skills": ["/skills/brand-guidelines/"],
        },
    ],
)

