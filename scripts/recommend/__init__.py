"""Fix Recommendations module - actionable repair suggestions."""

from .recommender import RecommendationGenerator
from .templates import (
    get_code_fix_template,
    get_infra_fix_template,
    get_interference_fix_template
)